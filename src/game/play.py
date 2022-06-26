from random import Random
from dataclasses import dataclass

@dataclass
class Money:
  pence: int
  
  def pounds(self) -> float:
    self.pence / 100

@dataclass
class Player:
  name: str

class Play:
  def __init__(self, random: Random) -> None:
    self.random = random