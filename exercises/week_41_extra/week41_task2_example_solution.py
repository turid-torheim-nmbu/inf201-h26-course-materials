from pathlib import Path


def read_log_file(file_path: Path) -> str:
    """Reads a binary log file, handling UTF-8 BOM, UTF-16, and Latin-1 fallbacks."""
    raw_bytes = file_path.read_bytes()

    # Detect UTF-16 Byte Order Marks
    if raw_bytes.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw_bytes.decode("utf-16")

    # Try UTF-8 (handling potential BOM via utf-8-sig)
    try:
        return raw_bytes.decode("utf-8-sig")
    except UnicodeDecodeError:
        # Latin-1 maps all 256 bytes to Unicode code points, ensuring lossless fallback
        return raw_bytes.decode("latin-1")


if __name__ == "__main__":

    logs_dir = Path("sample_logs")

    keep_content = []
    for log_path in logs_dir.glob("*.txt"):
        print(f"Reading: {log_path.name}")

        # Extraxt content from log
        content = read_log_file(log_path)
        assert not content.startswith(
            "\ufeff"
        ), f"BOM was not stripped in {log_path.name}"

        # Split by line and decide which lines to keep
        for line in content.splitlines():
            if line.startswith("["):
                keep_content.append(line)

    # Save to a UTF-8 file with a BOM
    save_file = Path("collected_log_file.txt")
    with open(save_file, "w", encoding="utf-8-sig") as file:
        for item in keep_content:
            file.write(f"{item}\n")
    print(f"All logs written to {save_file}")
