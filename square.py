class Square:
    def __init__(self):
        self.HasMine = False
        self.opened = False
        self.flagged = False
        self.neighbors = []

    def open(self):
        self.opened = True
        if self.mineCount == 0:
            [s.open() for s in self.neighbors if not s.opened and not s.flagged]
        return self.HasMine

    def flag(self):
        self.flagged = True

    @property
    def mineCount(self):
        return sum(x.HasMine for x in self.neighbors)

    @property
    def closedNeighbors(self):
        return [s for s in self.neighbors if not s.opened and not s.flagged]

    @property
    def neighborFlagCount(self):
        return sum(f.flagged for f in self.neighbors)

    def __str__(self):
        if self.flagged: return "^"
        if not self.opened:
            return "□"
        if self.HasMine: return "*"
        else: return str(self.mineCount)

    def __repr__(self):
        return self.__str__()

