import argparse
import json
from pathlib import Path

DOCKS_FILE = Path(__file__).parent / "docks.json"


def load_docks():
    return json.loads(DOCKS_FILE.read_text())


def check_dock(dock, length, breadth, draft, tide):
    reasons = []
    if length > dock["length"]:
        reasons.append(f"length {length} > {dock['length']}")
    if breadth > dock["breadth"]:
        reasons.append(f"breadth {breadth} > {dock['breadth']}")
    water_over_sill = dock["sill_depth"] + tide
    if draft > water_over_sill:
        reasons.append(f"draft {draft} > water over sill {water_over_sill:.2f}")
    return reasons


def main():
    parser = argparse.ArgumentParser(description="GRSE Dock Finder (baseline)")
    parser.add_argument("--length", type=float, required=True, help="Vessel length (m)")
    parser.add_argument("--breadth", type=float, required=True, help="Vessel breadth (m)")
    parser.add_argument("--draft", type=float, required=True, help="Vessel draft (m)")
    parser.add_argument("--tide", type=float, required=True, help="Tide height above chart datum (m)")
    args = parser.parse_args()

    for dock in load_docks():
        reasons = check_dock(dock, args.length, args.breadth, args.draft, args.tide)
        if reasons:
            print(f"[NOT SUITABLE] {dock['name']}: " + "; ".join(reasons))
        else:
            print(f"[SUITABLE]     {dock['name']}")


if __name__ == "__main__":
    main()
