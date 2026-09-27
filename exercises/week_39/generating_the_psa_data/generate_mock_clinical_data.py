# Generate mock clinical data for student assignments
# Turid Torheim, NMBU

from datetime import datetime, timedelta
import random
from pathlib import Path

import numpy as np
import pandas as pd


def generate_study_records(study_id: str, id_range: range, missing_pct: float) -> list[dict]:
    """
    Generate mock clinical data for studies of PSA level in patients after prostatectomy.

    Args:
        study_id: A string giving the id of the study the data comes from
        id_range: Range used to generate possible patient ids
        missing_pct: A float indicating the fraction of patient ids that should be missing (between 0 an 1)
    Return:
        A list of the generated clinical data
    """

    # Generate list of patient ids for the study
    all_possible_ids = list(id_range)
    num_missing = int(round(len(all_possible_ids) * missing_pct))
    missing_ids = set(random.sample(all_possible_ids, num_missing))
    active_patient_ids = [pid for pid in all_possible_ids if pid not in missing_ids]

    # Specify first and last possible surgery date, as well as the end date of the study
    surgery_start = datetime(2005, 1, 10)
    surgery_end = datetime(2009, 11, 25)
    study_end = datetime(2024, 12, 31)

    # The generated clinical data will be collected in records (list[dict])
    records = []

    for pid in active_patient_ids:
        # Generate random surgery date within the specified interval
        days_span = (surgery_end - surgery_start).days
        surgery_date = surgery_start + timedelta(days=random.randint(0, days_span))

        # Generate date of birth, assuming age 45–75 at time of surgery
        age_years = random.randint(45, 75)
        dob = surgery_date - timedelta(days=int(age_years * 365.25) + random.randint(0, 364))

        # Assume ~30% relapse rate
        # Check if this patient will relapse, and of so generate a month of relapse
        # (between 12 and 60 months post surgery)
        will_relapse = np.random.rand() < 0.30
        relapse_month = random.randint(12, 60) if will_relapse else None

        # Assume ~10% dropout rate between years 3 and 7 (months 36–84)
        # Check if patient will drop out, and if so generate drop out month
        will_dropout = np.random.rand() < 0.10
        dropout_month = random.randint(36, 84) if will_dropout else None

        # Follow-up schedule: Months 2, 4, 6, 8, 10, 12, then every 12 months
        followup_months = [2, 4, 6, 8, 10, 12]
        current_m = 24
        while True:
            test_date = surgery_date + timedelta(days=int(current_m * 30.4375))
            if test_date > study_end:
                break
            followup_months.append(current_m)
            current_m += 12

        # Patient will be removed from the study after two consecutive high PSA values
        consecutive_high_count = 0

        for m in followup_months:
            if will_dropout and m > dropout_month:
                break

            # Assume 5% chance of missing an appointment
            if np.random.rand() < 0.05:
                continue

            # Generate a PSA test date, and check whether we are still within the duration of the study
            psa_date = surgery_date + timedelta(days=int(m * 30.4375))
            if psa_date > study_end:
                continue

            # Generate PSA measurement
            if not will_relapse or m < relapse_month:
                # Remission / baseline (< 0.1 ng/mL)
                psa_val = max(0.01, round(np.random.normal(0.03, 0.015), 2))
            else:
                # Exponential growth post-relapse
                months_post_relapse = m - relapse_month
                growth = 0.15 * np.exp(0.07 * months_post_relapse)
                psa_val = round(growth + np.random.normal(0, 0.05), 2)
                psa_val = max(0.10, psa_val)

            # Append this dict (corresponding to one follow up appointment for one patient) to the records list
            records.append({
                "study_id": study_id,
                "patient_id": pid,
                "date_of_birth": dob.strftime("%Y-%m-%d"),
                "surgery_date": surgery_date.strftime("%Y-%m-%d"),
                "psa_value": psa_val,
                "psa_date": psa_date.strftime("%Y-%m-%d"),
            })

            # Check consecutive high values (> 1.0)
            if psa_val > 1.0:
                consecutive_high_count += 1
            else:
                consecutive_high_count = 0

            # Stop follow-up after two consecutive readings > 1.0
            if consecutive_high_count >= 2:
                break

    return records


def generate_multi_study_dataset(seed: int = 42) -> pd.DataFrame:
    """Generate a multi-study mock clinical dataset"""

    # Set the seeds for random number generating in numpy and random
    # This makes the results reproducible
    np.random.seed(seed)
    random.seed(seed)

    # Configuration for the three studies
    studies_config = [
        {"study_id": "A12", "id_range": range(1, 50), "missing_pct": 0.10},
        {"study_id": "B41", "id_range": range(1, 120), "missing_pct": 0.15},
        {"study_id": "C08", "id_range": range(1, 45), "missing_pct": 0.05},
    ]

    # Generate data for each study separately, then combine them
    all_records = []
    for config in studies_config:
        study_records = generate_study_records(
            study_id=config["study_id"],
            id_range=config["id_range"],
            missing_pct=config["missing_pct"],
        )
        all_records.extend(study_records)

    # Combine into a single pandas DataFrame
    df = pd.DataFrame(all_records)

    # Shuffle rows to combine studies naturally (optional, but realistic)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

    return df


# Execute generation and export to CSV
save_path = Path(<directory>, "psa_clinical_data.csv")
df = generate_multi_study_dataset()
df.to_csv(save_path, index=False)
