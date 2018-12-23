"""
Placeholder
"""

class Warden():
    def __init__(self, teamColor):
        self.info = {
            "image_active_path": "characters/{team}/warden/{team}-warden.png".format(team=teamColor),
            "image_inactive_path": "characters/{team}/warden/{team}-warden-inactive.png".format(team=teamColor),
            "idle_1_path": "characters/{team}/warden/{team}-warden-idle1.png".format(team=teamColor),
            "idle_2_path": "characters/{team}/warden/{team}-warden-idle2.png".format(team=teamColor),
            "stats": {
                "name": "Warden",
                "hp": 20,
                "strength": 6,
                "defense": 3,
                "accuracy": 110,
                "evasion": 20,
                "movement": 3,
            },
        }
