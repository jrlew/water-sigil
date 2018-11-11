# fe-pygame
Fire Emblem/Advance Wars mashup built using PyGame

Uses Python 3
Run with 'python main.py'

### TODOs ###
Clean up usage of state in class methods
Come up with a better name than state
Clean up Intro and Level classes
Create base class for terrain and units to cover entities with image/position
Use ^ class instead of Units for Indicator base to remove stats

=====Classes=====
1.Soldier (1 point cardinal)
2.Mage (1 point diag)
3.Pikeman (2 point cardinal)
4.Archer (1 point, cardinal, only attacks 2 spaces away)
5.


====Movement System====

Turn Point pool - spend to activate a units turn. Each unit has unique movement pattern/distance.
e.g. spend 1 turn point to move a pikeman up 2 squares, or to move a swordsman to the side 1 square.

DISTANT FUTURE- Add a unit recruitment system. You play as a hedge knight that hires mercenaries for each job. Visit the tavern with a set amount of money, and buy units/items for the upcoming battle.

Unit Directional system (maybe)

Attack system- 