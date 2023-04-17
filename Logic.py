from Cards import *
from TopN import *


def getMVPLineup(cap, cards):

    rosters = TopRosters()
    MVP = cards.maxValPlayer
    cards.removePlayer(MVP.name)
    rosterSize = 4

    subsets = cards.findsubsets(rosterSize)

    for staff in subsets:
        points = MVP.value
        cost = 0
        roster = MVP.name + ", "

        for p in staff:
            cost += p.cost
            points += p.value
            roster += p.name + ", "

        if cost <= cap:
            roster = roster[:-2]
            rosters.insertElement((points, roster))

    return rosters.printRosters()


def getLineup(cap, cards):

    rosters = TopRosters()
    rosterSize = 5
    subsets = cards.findsubsets(rosterSize)

    for staff in subsets:

        points = 0
        cost = 0
        roster = ""

        for p in staff:
            cost += p.cost
            points += p.value
            roster += p.name + ", "

        if cost <= cap:
            roster = roster[:-2]
            rosters.insertElement((points, roster))

    return rosters.printRosters()
