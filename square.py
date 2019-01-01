class Square:
    def __init__(self):
        self.HasMine = False
        self.Opened = False
        self.flagged = False
        self.neighbors = []

    def open(self):
        self.Opened = True
        if self.neighborMineCount == 0:
            [s.open() for s in self.neighbors if not s.Opened]
        return self.HasMine

    @property
    def neighborMineCount(self):
        return sum(x.HasMine for x in self.neighbors)

    @property
    def closedNeighbors(self):
        return [s for s in self.neighbors if not s.Opened]

    def __str__(self):
        if not self.Opened: return "□"
        if self.HasMine: return "*"
        else: return str(self.neighborMineCount)

    def __repr__(self):
        return self.__str__()

