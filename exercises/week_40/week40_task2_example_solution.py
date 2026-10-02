import json
import yaml
import pandas as pd

# Read the config yaml file using safe_load
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# Read data from excel and csv files using pandas
sensors_df = pd.read_excel("sensors.xlsx")
calib_df = pd.read_csv("calibrations.csv")

# Merge the dataframes sensors_df and calib_df
merged = pd.merge(sensors_df, calib_df, on="sensor_id")
# Filter out the overdue sensors
overdue = merged[merged["days_since_calibration"] > config["max_days_since_calibration"]]

# Convert to a dict and export this to the specified json file
result = overdue.to_dict(orient="records")
with open(config["output_file"], "w") as f:
    json.dump(result, f, indent=2)  # indent to make the file more readable
