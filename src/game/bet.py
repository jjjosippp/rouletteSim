from enum import Enum, auto

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

class Bet:
  pass