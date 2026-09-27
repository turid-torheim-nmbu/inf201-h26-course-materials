from pathlib import Path

import pandas as pd


def parse_header(file_path: Path) -> dict[str, str]:
    """Parses metadata key-value pairs from the file header.

    Reads line-by-line and terminates immediately when non-header data is
    reached, ensuring memory-efficient O(1) performance on massive files.

    Args:
        file_path: Path to file with header
    Returns:
        dict of extracted metadata
    """
    metadata: dict[str, str] = {}

    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            # Header metadata lines begin with '##'
            if line.startswith("##"):
                # Strip "##" from the start of the line
                clean_line: str = line.lstrip("#").strip()
                # Look for "<key>=<value>" in the line
                if "=" in clean_line:
                    key, value = clean_line.split("=", 1)
                    metadata[key] = value
            else:
                # Stop reading as soon as the '##' header section ends
                break

    return metadata


def generate_sequencing_manifest(
    seq_dir: str | Path = "raw_sequencing_data",
    output_csv: str | Path = "psa_study/sequencing_manifest.csv",
) -> pd.DataFrame:
    """Scans a directory of sequencing files, parses header metadata and exports a mapping csv."""
    input_path: Path = Path(seq_dir)
    manifest_records: list[dict[str, str | int]] = []

    # Iterate over all relevant files in the input folder
    # Use vcf files as example here
    for vcf_file in input_path.glob("*.vcf"):
        metadata: dict[str, str] = parse_header(vcf_file)

        # study and patient id get type str | None, in case they are not found in the metadata
        study_id: str | None = metadata.get("study_id")
        raw_patient_id: str | None = metadata.get("patient_id")

        # Create unique_id the same was as in task 1
        # Add data from this patient to the record
        if study_id and raw_patient_id:
            patient_id: int = int(raw_patient_id)
            unique_id: str = f"{study_id}_{patient_id:03d}"

            manifest_records.append({
                "unique_id": unique_id,
                "study_id": study_id,
                "patient_id": patient_id,
                "sequencing_file_path": str(vcf_file),
            })

    # Save summary manifest
    manifest_df: pd.DataFrame = pd.DataFrame(manifest_records)

    # Sort manifest by unique_id
    manifest_df = manifest_df.sort_values(by=["unique_id"]).reset_index(drop=True)

    # Create output directory and save csv file
    out_file: Path = Path(output_csv)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    manifest_df.to_csv(out_file, index=False)

    return manifest_df


if __name__ == "__main__":
    generate_sequencing_manifest()
