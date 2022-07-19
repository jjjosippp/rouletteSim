from game import play, bet, number
from typing import Tuple
import itertools
import random

def straightUps() -> list(int): return [n for n in range(0, 37)]

def splits() -> list[(int, int)]:
    horizontal = [[(n, n+1), (n, n-1)] for n in range(2, 36, 3)]
    vertical = [[(n, n+3), (n+1, n+4), (n+2, n+5)] for n in range(1, 32, 3)]
    horizontalFlattened = list(itertools.chain.from_iterable(horizontal))
    verticalFlattened = list(itertools.chain.from_iterable(vertical))
    return horizontalFlattened + verticalFlattened

def streets() -> list[int]: return list(range(1, 35, 3))

def corners() -> list[(int, int)]:
    return [(n, n + 4) for n in range(1, 32)] + [(n, n + 4) for n in range(2, 33)]

def lines() -> list[(int, int)]: return [(n, n+1) for n in range(1, 32, 3)]

def dozens() -> list[int]: return list(range(1, 4))

def columns() -> list[int]: return list(range(1, 4))


def makeBet(betType: bet.BetType, nums: list[int]) -> bet.Bet:
    ...

def makeBets() -> list[bet.Bet]:
    ...

# Let's test what happens when we place the same bet on every single field!
if __name__ == '__main__':
    bets = makeBets()
    p = play.Play(random.Random(0))
    print(p.playRound(bets))