class HanoiTower:
    def __init__(self, size):
        self.size = size
        self.towers = [[], [], []]
        self.towers[0] = [x for x in range(size, 0, -1)]

    def playGame(self):
        print(self.towers)
        self.moveDisk(self.size, 0, 1, 2)

    def moveDisk(self, size, origin, buf, destination):
        if size == 1:
            item = self.towers[origin].pop()
            self.towers[destination].append(item)
            print(self.towers)
        else:
            self.moveDisk(size - 1, origin, destination, buf)
            self.moveDisk(1, origin, buf, destination)
            self.moveDisk(size - 1, buf, origin, destination)

game = HanoiTower(5)
game.playGame()
