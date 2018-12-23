from .levelinit import LevelInit
from .playerphase import PlayerPhase
from .unitphase import UnitPhase
from .unitattack import UnitAttackPhase
from .enemyphase import EnemyPhase


states = {
    "Level_Init": LevelInit,
    "Player_Phase": PlayerPhase,
    "UnitPhase": UnitPhase,
    "UnitAttackPhase": UnitAttackPhase,
    "EnemyPhase": EnemyPhase,
}
