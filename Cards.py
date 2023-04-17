import itertools
import pandas as pd


class Card:

    def __init__(self, name, cost, value, bonus) -> None:
        self.name = name
        bonus = (bonus / 100) + 1
        self.cost = cost
        self.value = value * bonus


class playerCards:

    def __init__(self):
        self.players = []

        df = pd.read_csv('MyCards.csv')

        maxVal = 0

        for index, row in df.iterrows():
            self.players.append(
                Card(row["Name"], row["Cost"], row["Projection"], row["Bonus"]))

            if maxVal < row["Projection"]:
                maxVal = row["Projection"]
                self.maxValPlayer = Card(
                    row["Name"], row["Cost"], row["Projection"], row["Bonus"])

    def findsubsets(self, n):
        return list(itertools.combinations(self.players, n))

    def removePlayer(self, playerName):

        found = -1

        for i, player in enumerate(self.players):
            if player.name == playerName:
                found = i
                break

        self.players.pop(found)

    def removeRoster(self, playerNames):
        for player in playerNames.split(', '):
            self.removePlayer(player)
