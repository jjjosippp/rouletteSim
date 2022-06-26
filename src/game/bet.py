from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List
from dataclasses import dataclass
from number import Number

@dataclass
class Money:
  pence: int
  
  def pounds(self) -> float:
    self.pence / 100
    
  def half(self) -> 'Money':
    return Money(self.pence // 2)
    
  def __mul__(self, x: int) -> 'Money':
    return Money(self.pence * x)

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
  money: Money
  
  def returns(self, rolled: Number) -> Money:
    losingReturns = 0 if self.odds != 1 else self.money.half
    winningReturns = self.money * (self.odds() + 1)
    return winningReturns if self.didWin(rolled) else losingReturns
  
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
  
  def didWin(self, rolled: Number) -> bool:
    match (self.betType, self.chosenNumbers):
      case (BetType.STRAIGHT_UP, [a]):
        return rolled.n == a
      case (BetType.SPLIT, pair):
        return rolled.n in pair
      case (BetType.STREET, [a]):
        return rolled.isStreet(a)
      case (BetType.CORNER, [a, b]):
        return rolled.isCorner(a, b)
      case (BetType.BASKET, []):
        return rolled.isBasket()
      case (BetType.LINE, [a, b]):
        return rolled.line(a, b)
      case (BetType.DOZEN, [a]):
        return rolled.isDozen(a)
      case (BetType.COLUMN, [a]):
        return rolled.isColumn(a)
      case (BetType.EVEN, []):
        return rolled.isEven()
      case (BetType.ODD, []):
        return rolled.isOdd()
      case (BetType.RED, []):
        return rolled.isRed()
      case (BetType.BLACK, []):
        return rolled.isBlack()
      case (BetType.LOW, []):
        return rolled.isLow()
      case (BetType.HIGH, []):
        return rolled.isHigh()