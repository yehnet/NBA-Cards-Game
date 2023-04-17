from Logic import *
from Cards import *


def main():
    mycards = playerCards()
    lineup = getMVPLineup(120, mycards)
    mycards.removeRoster(lineup[1])

    while len(mycards.players) >= 5:
        print()
        lineup = getLineup(5000, mycards)
        mycards.removeRoster(lineup[1])


if __name__ == "__main__":
    main()
