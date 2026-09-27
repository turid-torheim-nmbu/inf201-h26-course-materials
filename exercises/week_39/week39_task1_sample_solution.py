# Script to set up folder and file structure for the clinical data
# Turid Torheim, NMBU

from pathlib import Path
import shutil

import pandas as pd


def organize_psa_dataset(input_csv: str | Path, output_dir: str | Path, clean_first: bool = False) -> None:
    """Parses combined dataset into nested folders and generates per-study summary files."""
    base_dir: Path = Path(output_dir)

    # Check if the output directory exists, and wipe it if clean_first is indicated
    if clean_first and base_dir.exists():
        shutil.rmtree(base_dir)

    # Create the base directory
    base_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    df: pd.DataFrame = pd.read_csv(input_csv)

    # Create unique_id for each patient, combining study_id and zero-padded patient_d
    df["unique_id"] = [f"{study}_{pid:03d}" for study, pid in zip(df["study_id"], df["patient_id"])]

    # Sort the dataframe by this unique id for tidier summary files
    df.sort_values(by="unique_id", inplace=True)

    # Create datetime object versions of the date columns for accurate date calculations
    df["surgery_date_dt"] = pd.to_datetime(df["surgery_date"])
    df["psa_date_dt"] = pd.to_datetime(df["psa_date"])

    # Iterate over studies to create study directories
    for study_id, study_df in df.groupby("study_id"):
        # groupby allows us to look at each study separately without creating new data frames
        # Create study directory psa_study/<study_id>
        study_dir: Path = base_dir / str(study_id)
        study_dir.mkdir(parents=True, exist_ok=True)

        study_summary_records: list[dict[str, str | int]] = []

        # Iterate over patient in the selected study
        for unique_id, patient_data in study_df.groupby("unique_id"):
            # Create patient directory: psa_study/<study_id>/<unique_id>/
            patient_dir: Path = study_dir / str(unique_id)
            patient_dir.mkdir(parents=True, exist_ok=True)

            # Sort patient_data by psa_date_dt for a tidier csv file
            patient_data_sorted = patient_data.sort_values(by="psa_date_dt")

            # Write individual patient data (dropping temporary datetime helper columns)
            export_cols = [c for c in patient_data_sorted.columns if c not in ["surgery_date_dt", "psa_date_dt"]]
            patient_file: Path = patient_dir / f"{unique_id}_psa_data.csv"
            patient_data_sorted[export_cols].to_csv(patient_file, index=False)

            # Calculate metrics for the summary file
            s_date = patient_data_sorted["surgery_date_dt"].iloc[0]  # This date is the same for all rows
            latest_psa_date = patient_data_sorted["psa_date_dt"].max()
            follow_up_days: int = (latest_psa_date - s_date).days

            # Relative path for the summary files
            patient_dir_rel = patient_dir.relative_to(base_dir)

            # Collect summary row for this patient
            study_summary_records.append({
                "unique_id": unique_id,
                "patient_id": patient_data_sorted["patient_id"].iloc[0],
                "study_id": study_id,
                "date_of_birth": patient_data_sorted["date_of_birth"].iloc[0],
                "surgery_date": patient_data_sorted["surgery_date"].iloc[0],
                "follow_up_days": follow_up_days,
                "number_of_psa_measurements": len(patient_data_sorted),
                "patient_folder_path": str(patient_dir_rel),
            })

        # Generate and save csv summary for this study
        summary_df: pd.DataFrame = pd.DataFrame(study_summary_records)
        summary_file: Path = study_dir / f"{study_id}_summary.csv"
        summary_df.to_csv(summary_file, index=False)


if __name__ == "__main__":
    project_path = Path(<path to project folder>)
    read_file = Path(<file_dir>, "psa_clinical_data.csv")
    output_path = Path(project_path, "psa_studies")
    organize_psa_dataset(read_file, project_path, clean_first=False)
