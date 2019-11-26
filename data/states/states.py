from .enemyphase import EnemyPhase
from .levelinit import LevelInit
from .levelselect import LevelSelect
from .playerphase import PlayerPhase
from .unitattack import UnitAttackPhase
from .unitphase import UnitPhase

states = {
    "EnemyPhase": EnemyPhase,
    "Level_Init": LevelInit,
    "Level_Select": LevelSelect,
    "Player_Phase": PlayerPhase,
    "UnitAttackPhase": UnitAttackPhase,
    "UnitPhase": UnitPhase,
}
