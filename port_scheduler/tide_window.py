import argparse
import json
from pathlib import Path

from berth_finder import load_berths

TIDES_FILE = Path(__file__).parent / "tides.json"


def load_tides():
    return json.loads(TIDES_FILE.read_text())


def tide_windows(tides, depth, draft):
    windows = []
    start = None
    for reading in tides:
        if draft <= depth + reading["height"]:
            if start is None:
                start = reading["time"]
            end = reading["time"]
        elif start is not None:
            windows.append((start, end))
            start = None
    if start is not None:
        windows.append((start, end))
    return windows


def main():
    parser = argparse.ArgumentParser(description="Tide Window Calculator")
    parser.add_argument("--berth", required=True, help="Berth name")
    parser.add_argument("--draft", type=float, required=True, help="Vessel draft (m)")
    args = parser.parse_args()

    berth = next(b for b in load_berths() if b["name"] == args.berth)
    windows = tide_windows(load_tides(), berth["depth"], args.draft)

    print(f"{berth['name']} (depth {berth['depth']} m), draft {args.draft} m")
    if not windows:
        print("No safe tide window")
    for start, end in windows:
        print(f"  {start} -> {end}")


if __name__ == "__main__":
    main()
