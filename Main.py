from Logic import *
from Cards import *


def main():
    mycards = playerCards()
    first = getMVPLineup(120, mycards)

    delete = first[1].split(', ')
    for player in delete:
        mycards.removePlayer(player)
    print()
    second = getLineup(5000, mycards)


if __name__ == "__main__":
    main()
