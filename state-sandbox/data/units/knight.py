"""
Placeholder
"""

class Knight():
    def __init__(self, teamColor):
        self.info = {
            "image_active_path": "characters/{team}/knight/{team}-knight.png".format(team=teamColor),
            "image_inactive_path": "characters/{team}/knight/{team}-knight-inactive.png".format(team=teamColor),
            "idle_1_path": "characters/{team}/knight/{team}-knight-idle1.png".format(team=teamColor),
            "idle_2_path": "characters/{team}/knight/{team}-knight-idle2.png".format(team=teamColor),
            "stats": {
                "name": "Knight",
                "hp": 20,
                "strength": 6,
                "defense": 3,
                "accuracy": 110,
                "evasion": 20,
                "movement": 3,
                "min_attack_range": 1,
                "max_attack_range": 1,
            },
        }
