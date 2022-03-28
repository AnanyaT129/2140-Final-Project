#This is a file used for testing code

#checks if the word checker works correctly 
from word_checker_class import WordChecker

word = input('Enter the word: ')
word1 = WordChecker(word)

print(word1.word_checker())

