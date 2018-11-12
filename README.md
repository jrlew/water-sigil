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

===== Classes =====
1.Soldier (1 point cardinal) 
2.Knight  (2 point cardinal)
2.Mage (1 point diag)
4.Archer (1 point, cardinal, only attacks 2 spaces away)
5.


==== Movement System ====

Turn Point pool - spend to activate a units turn. Each unit has unique movement pattern/distance.
e.g. spend 1 turn point to move a pikeman up 2 squares, or to move a swordsman to the side 1 square.

DISTANT FUTURE- Add a unit recruitment system. You play as a hedge knight that hires mercenaries for each job. Visit the tavern with a set amount of money, and buy units/items for the upcoming battle.

Unit Directional system (maybe)

==== Attack System ====


==== Artwork ====

file names are arranged as follows: ogbject-direction(if final tile in a given direction) - tile that comes next in said direction
        e.g. 'mountain-left-grass'     denotes that the object is a mountain, that it is the leftmost mountain of a cluster, and that the next tile to the left is a grass tile.
This is done because the tile arts should bleed into one another, therefore it's necessary to know which tile comes next.

It would be ideal if instead of labeling the next tile on every level file, we could simply decide the biome, and have that be understood as the default for the given page.
for example:  instead of 'mountain-bottom-grass'  we can call it 'mountain-bottom' and assume the next tile is grass because it's a grass stage. 
any tile that is an exception to the biome will follow the original naming convention 
----NOTE: the .png files will have to use more descriptive names. I'm only talking about var declarations on the intro/any following level files, to save space in the tile arrays.---