from Cards import Card


class TopRosters:

    size = 3

    def __init__(self, ):
        self.array = []

    def getMinIndex(self):
        minVal = self.array[0][0]
        minIndex = 0

        for i, roster in enumerate(self.array):
            if roster[0] < minVal:
                minIndex = i
                minVal = roster[0]

        return minIndex

    def insertElement(self, roster):
        if len(self.array) < self.size:
            self.array.append(roster)
        else:
            self.array = sorted(self.array, key=lambda x: x[0], reverse=True)
            if roster[0] > self.array[-1][0]:
                self.array[-1] = roster

    def printRosters(self):
        sortedArr = sorted(self.array, key=lambda x: x[0], reverse=True)

        for roster in sortedArr:
            print(roster)

        return sortedArr[0]
