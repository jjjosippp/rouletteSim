from random import Random
from dataclasses import dataclass

@dataclass
class Player:
  name: str

class Play:
  def __init__(self, random: Random) -> None:
    self.random = random