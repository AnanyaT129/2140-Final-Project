class PointValue:
    def __init__(self):
        self.scoreboard = [[3,1,2,1,3], [1,1,1,1,1], [3,1,3,1,3], [1,1,1,1,1], [3,1,2,1,3]]
        self.letter_value = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1., "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

    def calculate_points(self, word, direction, start):
        list_of_letters = [char for char in word.upper()]
        sum = 0
        try:
            if direction == "down":
                for x in range(len(word)):
                    sum += (self.scoreboard[start[0]+x][start[1]] * self.letter_value.get(list_of_letters[x]))
            else:
                for x in range(len(word)):
                    sum += (self.scoreboard[start[0]][start[1]+x] * self.letter_value.get(list_of_letters[x]))
            
            return sum
        except:
            return "Invalid"

#tests
value1 = PointValue()
print(value1.calculate_points("word", "down", (0,0))) #18
print(value1.calculate_points("word", "right", (0,0))) #17
print(value1.calculate_points("word", "right", (2,2))) #"Invalid"