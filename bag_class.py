# class containing functions to do with the bag of letters
#  - initializes bag
#  - gets number of tiles in bag
#  - removes letter from bag

import random

class BagClass:
    def __init__(self):
        self.bag = []
        self.initialize()

    def initialize(self):
        self.bag.extend(["A"] * 9)
        self.bag.extend(["B"] * 2)
        self.bag.extend(["C"] * 2)
        self.bag.extend(["D"] * 4)
        self.bag.extend(["E"] * 12)
        self.bag.extend(["F"] * 2)
        self.bag.extend(["G"] * 3)
        self.bag.extend(["H"] * 2)
        self.bag.extend(["I"] * 9)
        self.bag.extend(["J"] * 1)
        self.bag.extend(["K"] * 1)
        self.bag.extend(["L"] * 4)
        self.bag.extend(["M"] * 2)
        self.bag.extend(["N"] * 6)
        self.bag.extend(["O"] * 8)
        self.bag.extend(["P"] * 2)
        self.bag.extend(["Q"] * 1)
        self.bag.extend(["R"] * 6)
        self.bag.extend(["S"] * 4)
        self.bag.extend(["T"] * 6)
        self.bag.extend(["U"] * 4)
        self.bag.extend(["V"] * 2)
        self.bag.extend(["W"] * 2)
        self.bag.extend(["X"] * 1)
        self.bag.extend(["Y"] * 2)
        self.bag.extend(["Z"] * 1)
        self.bag.extend(["BLANK"] * 2)

        random.shuffle(self.bag)

    def remove_tile(self):
        self.bag.pop()

    def get_bag_size(self):
        return len(self.bag)

bag1 = BagClass()
print(bag1.bag)
print(bag1.get_bag_size())