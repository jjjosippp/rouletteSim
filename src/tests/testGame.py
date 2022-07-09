import unittest
import random
from typing import Tuple
from game import play, bet, number

def makeBet(name: str, betAmount: int, betType: bet.BetType, nums: list[int]) -> Tuple[play.Player, bet.Bet]:
    return (play.Player(name), bet.Bet(betType, nums, betAmount))

class TestRoulette(unittest.TestCase):

    def test1(self):
        # Not very extensive 😅
        bets = [
            makeBet('Joe', 50, bet.BetType.SPLIT, [12, 14]),
            makeBet('James', 100, bet.BetType.EVEN, []),
            makeBet('James', 100, bet.BetType.DOZEN, [2]),
            makeBet('Joe', 200, bet.BetType.BLACK, []),
        ]
        p = play.Play(random.Random(0))
        assert(p.playRound(bets) == [(play.Player('Joe'), 0), (play.Player('James'), 200), (play.Player('James'), 300), (play.Player('Joe'), 400)])

if __name__ == "__main__":
    unittest.main()