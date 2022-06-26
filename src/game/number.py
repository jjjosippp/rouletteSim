from enum import Enum, auto
from typing import List

TABLE_WIDTH = 3
MAX_NUMBER = 36

class Colour(Enum):
  RED = auto()
  BLACK = auto()
  GREEN = auto()

class Number:
  def __init__(self, n: int) -> None:
    self.n: int = n
    self. colour = Colour.getColour(n)
    
  @staticmethod
  def getColour(num: int) -> Colour:
    reds: List[int] = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if num == 0:
      return Colour.GREEN
    elif num in reds:
      return Colour.RED
    else:
      return Colour.BLACK
  
  @staticmethod
  def x(n: int) -> int: return (n - 1) % 3
  @staticmethod
  def y(n: int) -> int: return (n - 1) // 3