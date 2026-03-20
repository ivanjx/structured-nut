import subprocess
import time
import json
import os
from datetime import datetime, timezone

UPS_NAME = os.getenv("UPS_NAME", "myups@nut")
INTERVAL = int(os.getenv("INTERVAL", "10"))


def parse_value(value: str):
    """Try to convert to int/float, fallback to string."""
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def get_upsc_data():
    result = subprocess.run(
        ["upsc", UPS_NAME],
        capture_output=True,
        text=True,
    )

    data = {}
    for line in result.stdout.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip().replace(".", "_")] = parse_value(value.strip())

    return data


def main():
    print("Starting full NUT -> GELF forwarder...")

    while True:
        try:
            upsc_data = get_upsc_data()

            event = {
                "ups": UPS_NAME,
                **upsc_data
            }

            print(json.dumps(event), flush=True)

        except Exception as e:
            print(json.dumps({"error": str(e)}), flush=True)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
