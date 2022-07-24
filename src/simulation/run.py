from game import play, bet, number
from typing import Tuple
import itertools
import random
from functools import reduce

MONEY_PER_BET = 100

def straightUps() -> list[int]: return [n for n in range(0, 37)]

def splits() -> list[(int, int)]:
    horizontal = [[(n, n+1), (n, n-1)] for n in range(2, 36, 3)]
    vertical = [[(n, n+3), (n+1, n+4), (n+2, n+5)] for n in range(1, 32, 3)]
    horizontalFlattened = list(itertools.chain.from_iterable(horizontal))
    verticalFlattened = list(itertools.chain.from_iterable(vertical))
    return horizontalFlattened + verticalFlattened

def streets() -> list[int]: return list(range(1, 35, 3))

def corners() -> list[(int, int)]:
    return [(n, n + 4) for n in range(1, 32)] + [(n, n + 4) for n in range(2, 33)]

def lines() -> list[(int, int)]: return [[n, n+1] for n in range(1, 32, 3)]

def dozens() -> list[int]: return list(range(1, 4))

def columns() -> list[int]: return list(range(1, 4))


def makeBet(betType: bet.BetType, nums: list[int]) -> bet.Bet:
    return (play.Player("TestPlayer"), bet.Bet(betType=betType, money=bet.Money(MONEY_PER_BET), chosenNumbers=nums))

def makeBets() -> Tuple[list[bet.Bet], int]:
    betsLists = [
        [makeBet(bet.BetType.STRAIGHT_UP, [x]) for x in straightUps()],
        [makeBet(bet.BetType.SPLIT, x) for x in splits()],
        [makeBet(bet.BetType.STREET, [x]) for x in streets()],
        [makeBet(bet.BetType.CORNER, x) for x in corners()],
        [makeBet(bet.BetType.LINE, x) for x in lines()],
        [makeBet(bet.BetType.DOZEN, [x]) for x in dozens()],
        [makeBet(bet.BetType.COLUMN, [x]) for x in columns()],
        [makeBet(bet.BetType.EVEN, []), makeBet(bet.BetType.ODD, [])],
        [makeBet(bet.BetType.RED, []), makeBet(bet.BetType.BLACK, [])],
        [makeBet(bet.BetType.LOW, []), makeBet(bet.BetType.HIGH, [])],
        [makeBet(bet.BetType.BASKET, [])],
    ]
    bets = sum(betsLists, [])
    return (bets, MONEY_PER_BET * len(bets))

# Let's test what happens when we place the same bet on every single field!
if __name__ == '__main__':
    (bets, moneyBet) = makeBets()
    p = play.Play(random.Random())
    results = p.playRound(bets)
    winnings = reduce(lambda r, pm: pm[1].pence + r, results, 0)
    losses = -(winnings - moneyBet)
    print(f"Betting {moneyBet/100} quid, you have won {winnings/100}, which means you lost {losses/100}. This is {losses/moneyBet*100:.2f}% of the money bet :)")