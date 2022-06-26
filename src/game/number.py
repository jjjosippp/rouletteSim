from enum import Enum, auto

TABLE_WIDTH = 3
MAX_NUMBER = 36

class Colour(Enum):
  RED = auto()
  BLACK = auto()
  GREEN = auto()

class Number:
  def __init__(self, n: int) -> None:
    self.n: int = n
  
  @staticmethod
  def x(n: int) -> int: return (n - 1) % 3
  @staticmethod
  def y(n: int) -> int: return (n - 1) // 3