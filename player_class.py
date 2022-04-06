from bag_class import BagClass

# class containing functions to do with a player
#  - Update score
#  - Get score
#  - Remove letters
#  - Replenish letters

class PlayerClass:
    def __init__(self, name, bag):
        self.name = name
        self.score = 0
        self.letters = []
        self.skips = 0
        self.replenish_letters(bag)
    
    def update_score(self, points):
        self.score = self.score + points
    
    def get_score(self):
        return self.score
    
    def replenish_letters(self, bag):
        x = 7 - len(self.letters)
        for y in range(x):
            self.letters.append(bag.remove_tile())
    
    def get_letters(self):
        return self.letters
    
    def remove_letter(self, letter):
        self.letters.remove(letter)

bag1 = BagClass()
print(bag1.bag)
print(bag1.get_bag_size())

player1 = PlayerClass("Ananya", bag1)
print(player1.get_score())
player1.update_score(6)
print(player1.get_score())
print(player1.get_letters())
last_letter = player1.get_letters()[-1]

print(bag1.get_bag_size())

player1.remove_letter(last_letter)
print(player1.get_letters())

player1.replenish_letters(bag1)
print(player1.get_letters())
print(bag1.get_bag_size())