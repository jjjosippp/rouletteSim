from random import Random
from typing import List, Tuple
from game.bet import Bet, Money
from game.number import Number, MAX_NUMBER
from dataclasses import dataclass

@dataclass
class Player:
  name: str

class Play:
  def __init__(self, random: Random) -> None:
    self.random = random
    
  def playRound(self, bets: List[Tuple[Player, Bet]]) -> List[Tuple[Player, Money]]:
    pass
  
  def rollNumber(self) -> Number:
    return Number(self.random.randint(0, MAX_NUMBER))