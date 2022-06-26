from dataclasses import dataclass
from enum import Enum, auto
from typing import List
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