def clean_readings(readings: list[float | None], threshold: float) -> list[float]:
    """Filters out None values and any reading strictly below the threshold."""
    return [r for r in readings if r is not None and r >= threshold]


def format_summary(name: str, original: list[float | None], cleaned: list[float]) -> str:
    """Generates a formatted report."""

    # Number of readings before and after cleaning the data
    original_count = len(original)
    cleaned_count = len(cleaned)

    # Get the ratio of clean readings
    if original_count > 0:
        valid_ratio = cleaned_count / original_count
    else:
        valid_ratio = 0.0

    # Get average of valid readings
    if cleaned_count > 0:
        avg_reading = sum(cleaned) / cleaned_count
    else:
        avg_reading = 0.0

    # Return formatted string
    return (
        f"{'--- SENSOR REPORT: ' + sensor_name.upper() + ' ---':<35}\n"
        f"{'Valid readings':<20}: {valid_ratio:>8.1%}\n"
        f"{'Average reading':<20}: {avg_reading:>8.2f}\n"
        f"{'Removed readings':<20}: {(original_count - cleaned_count):>8}"
    )


# Input for demonstration
sensor_name = "sensor name"
sensor_readings = [2.673, 3.876, 4.589, None, None, None, 6.111, 0.435, None, 0.005,
                   2.444, 10.897, 0.019, 10.222, 0.543, None, 8.097, 0.962, None, 1.005,
                   None, 0.765, 0.765, 0.765, 0.765, 7.937, 1.007, 4.405, None, None]
sensor_threshold = 0.200

# Clean up the sensor readings
sensor_readings_cleaned = clean_readings(sensor_readings, sensor_threshold)
# Print report
print(format_summary(sensor_name, sensor_readings, sensor_readings_cleaned))
