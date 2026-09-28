# Working with json and yaml files
# Turid Torheim

import json
import yaml

# Create some sensor readings
sensor_payload = {
    "station_id": "ST-1042",
    "location": {"latitude": 59.9139, "longitude": 10.7522, "elevation_m": 125},
    "is_operational": True,
    "last_maintenance": None,  # Will map to JSON 'null'
    "readings": [
        {"timestamp": "2026-09-26T10:00:00Z", "temp_c": 14.5, "humidity_pct": 62},
        {"timestamp": "2026-09-26T11:00:00Z", "temp_c": 15.2, "humidity_pct": 58},
    ]
}

# We want to write this to a json file
file_path = "sensor_data.json"
with open(file_path, "w", encoding="utf-8") as jfile:
    # json.dump() takes native Python data structures (dict, list, int, float, bool, None)
    # and serializes them automatically. jfile.write() would require a str.
    # 'indent=4' makes the output human-readable instead of putting everything into a single line
    json.dump(sensor_payload, jfile, indent=4)

# Read the json file and deserialise the content back to Python
with open(file_path, "r", encoding="utf-8") as f:
    # 'load' parses the JSON file and returns native Python dicts and lists
    loaded_data = json.load(f)
print(f"Loaded Object Type: {type(loaded_data)}")  # <class 'dict'>
print(loaded_data)

# Now let us write the data to a yaml file instad
# We could do this using a context (with) as for the json file,
# but let us do this on the fly instead
yaml.dump(sensor_payload, open('sensor_data.yml', 'w'))
