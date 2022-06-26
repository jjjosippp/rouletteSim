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
  def getColour(n: int) -> Colour:
    reds: List[int] = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if n == 0:
      return Colour.GREEN
    elif n in reds:
      return Colour.RED
    else:
      return Colour.BLACK
  
  @staticmethod
  def x(n: int) -> int: return (n - 1) % 3
  @staticmethod
  def y(n: int) -> int: return (n - 1) // 3
  
  def isEven(self) -> bool: return self.n % 2 == 0 and self.n != 0
  
  def isOdd(self) -> bool: return (not self.isEven) and self.n != 0
  
  def isRed(self) -> bool: return self.colour == Colour.RED
  
  def isBlack(self) -> bool: return self.colour == Colour.BLACK
  
  def isStreet(self) -> bool: return self.n in [0, 1, 2, 3]
  
  def isHigh(self) -> bool: return True if self.num >= 19 and self.num != 0 else False
  
  def isLow(self) -> bool: return True if self.num <= 18 and self.num != 0 else True