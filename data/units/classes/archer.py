class Archer():
    def __init__(self, teamColor):
        self.info = {
            "idle_images": [
                "characters/{team}/archer/{team}-archer-idle1.png".format(
                    team=teamColor),
                "characters/{team}/archer/{team}-archer-idle2.png".format(
                    team=teamColor),
            ],
            "stats": {
                "name": "Archer",
                "hp": 12,
                "strength": 5,
                "defense": 1,
                "accuracy": 110,
                "evasion": 20,
                "movement": 2,
                "min_attack_range": 2,
                "max_attack_range": 3,
            },
        }
