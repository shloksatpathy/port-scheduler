# Port Scheduling Software

Scheduling software for port authorities to plan vessel arrivals, berth allocation and departures.

Port authorities currently match vessels to berths using basic tools that check a vessel's dimensions (length, breadth, draft) against berth limits with manually entered tide data. This works for a single vessel but breaks down when many vessels compete for berths, arrival times shift, and tide windows change through the day. This project aims to build a scheduling tool that uses full tide data, vessel-specific draft at arrival and departure (laden vs. ballast), and visual timelines of berth occupancy. It should let the port simulate scenarios such as delayed or early arrivals, resolve berth conflicts, and generate schedule reports for shipping lines, agents and terminal operators, improving berth utilisation and reducing vessel waiting time.

## Baseline Berth Finder

`port_scheduler/` holds a baseline berth finder. You enter the vessel's dimensions and the tide height by hand, and it checks each berth:

- vessel length ≤ berth length
- vessel breadth ≤ berth breadth
- vessel draft ≤ berth depth (below chart datum) + tide height

```
python3 port_scheduler/berth_finder.py --length 180 --breadth 30 --draft 9.5 --tide 1.2
```

Berth data is in `port_scheduler/berths.json`. The values there are placeholders and need to be replaced with the real berth dimensions of the port.
