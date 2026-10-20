import argparse
import json
from pathlib import Path

BERTHS_FILE = Path(__file__).parent / "berths.json"


def load_berths():
    return json.loads(BERTHS_FILE.read_text())


def check_berth(berth, length, breadth, draft, tide):
    reasons = []
    if length > berth["length"]:
        reasons.append(f"length {length} > {berth['length']}")
    if breadth > berth["breadth"]:
        reasons.append(f"breadth {breadth} > {berth['breadth']}")
    water_depth = berth["depth"] + tide
    if draft > water_depth:
        reasons.append(f"draft {draft} > water depth {water_depth:.2f}")
    return reasons


def main():
    parser = argparse.ArgumentParser(description="Port Berth Finder (baseline)")
    parser.add_argument("--length", type=float, required=True, help="Vessel length (m)")
    parser.add_argument("--breadth", type=float, required=True, help="Vessel breadth (m)")
    parser.add_argument("--draft", type=float, required=True, help="Vessel draft (m)")
    parser.add_argument("--tide", type=float, required=True, help="Tide height above chart datum (m)")
    args = parser.parse_args()

    for berth in load_berths():
        reasons = check_berth(berth, args.length, args.breadth, args.draft, args.tide)
        if reasons:
            print(f"[NOT SUITABLE] {berth['name']}: " + "; ".join(reasons))
        else:
            print(f"[SUITABLE]     {berth['name']}")


if __name__ == "__main__":
    main()
