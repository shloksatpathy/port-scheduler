This is the repo for the docker software that will cater to the following needs as per the instructions of the GRSE problem statment mentioned in the IDEX challenge

Advanced Dock finder Tool for dock scheduling
The current Dock Finder used at GRSE is a basic tool that helps determine the suitable docks for vessels based on their dimensions (length, breadth, draft) and manually entered tide data. While functional, this version is limited in its capabilities, particularly when dealing with complex docking schedules, multiple stages of vessel docking, and fluctuating tide data. An AI based solution is envisaged to address these limitations by incorporating comprehensive tide data, vessel-specific draft requirements at various stages (such as launching, CST, and pre-delivery), and enhanced visualization features. This tool should allow the shipyard to simulate various scenarios, such as delays or advancements in docking schedules, and generate detailed reports that can be included in build plans and strategies submitted to vessel owners. The tool’s advanced features should significantly enhance the accuracy and efficiency of dock scheduling, enabling better resource management and planning at shipyard.

## Baseline Dock Finder

`dock_finder/` holds a baseline copy of the current basic Dock Finder. You enter the vessel's dimensions and the tide height by hand, and it checks each dock:

- vessel length ≤ dock length
- vessel breadth ≤ dock breadth
- vessel draft ≤ sill depth + tide height

```
python3 dock_finder/dock_finder.py --length 100 --breadth 17 --draft 5 --tide 1.2
```

Dock data is in `dock_finder/docks.json`. The values there are placeholders and need to be replaced with the real GRSE dock dimensions.
