from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List
from dataclasses import dataclass

class BetType(Enum):
  STRAIGHT_UP = auto()
  SPLIT = auto()
  STREET = auto()
  CORNER = auto()
  BASKET = auto()
  LINE = auto()
  DOZEN = auto()
  COLUMN = auto()
  EVEN = auto()
  ODD = auto()
  RED = auto()
  BLACK = auto()
  LOW = auto()
  HIGH = auto()

@dataclass
class Bet:
  type: BetType
  chosenNumbers: List[int]
  
  def odds(self) -> int:
    oddsMap: Dict[BetType, int] = {
      BetType.STRAIGHT_UP: 35,
      BetType.SPLIT: 17,
      BetType.STREET: 11,
      BetType.CORNER: 8,
      BetType.BASKET:8,
      BetType.LINE: 5,
      BetType.DOZEN: 2,
      BetType.COLUMN: 2,
      BetType.EVEN: 1,
      BetType.ODD: 1,
      BetType.RED: 1,
      BetType.BLACK: 1,
      BetType.LOW: 1,
      BetType.HIGH: 1
    }
    return oddsMap[self.type]