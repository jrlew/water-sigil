"""
Placeholder
"""

class Warden():
    def __init__(self, teamColor):
        self.info = {
            "idle_1_path": "characters/{team}/warden/{team}-warden-idle1.png".format(team=teamColor),
            "idle_2_path": "characters/{team}/warden/{team}-warden-idle2.png".format(team=teamColor),
            "stats": {
                "name": "Warden",
                "hp": 24,
                "strength": 4,
                "defense": 1,
                "accuracy": 90,
                "evasion": 10,
                "movement": 2,
                "min_attack_range": 1,
                "max_attack_range": 1,
            },
        }
