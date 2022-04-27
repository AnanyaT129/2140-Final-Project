import unittest
import numpy as np
import collections
from scrabble_classes import PlayerClass, BagClass, BoardClass, WordClass

class TestPlayerMethods(unittest.TestCase):

    def setUp(self):
        self.bag = BagClass()
        self.player_a_start = self.bag.bag[-7:]
        self.player_a_start.reverse()
        self.player_b_start = self.bag.bag[-14:-7]
        self.player_b_start.reverse()
        self.player_a = PlayerClass("a", self.bag)
        self.player_b = PlayerClass("b", self.bag)

    def test_get_score(self):
        self.assertEqual(self.player_a.get_score(), self.player_a.score)
        self.assertEqual(self.player_b.get_score(), self.player_b.score)

    def test_update_score(self):
        self.player_a.update_score(6)
        self.assertEqual(self.player_a.get_score(), 6)
        self.player_b.update_score(0)
        self.assertEqual(self.player_b.get_score(), self.player_b.score)
    
    def test_get_letters(self):
        self.assertEqual(self.player_a.get_letters(), self.player_a_start)
        self.assertEqual(self.player_b.get_letters(), self.player_b_start)
    
    def test_remove_letters(self):
        self.player_a.remove_letter(self.player_a_start[-1])
        self.player_b.remove_letter(self.player_b_start[-1])
        self.assertEqual(collections.Counter(self.player_a.get_letters()), 
                         collections.Counter(self.player_a_start[:-1]))
        self.assertEqual(collections.Counter(self.player_b.get_letters()),
                         collections.Counter(self.player_b_start[:-1]))
    
    def test_replenish_letters(self):
        a_next = self.bag.bag[-1]
        b_next = self.bag.bag[-2]
        self.player_a.replenish_letters(self.bag)
        self.player_b.replenish_letters(self.bag)
        self.player_a_start[:-1].append(a_next)
        self.player_b_start[:-1].append(b_next)
        self.assertEqual(self.player_a.get_letters(), self.player_a_start)
        self.assertEqual(self.player_b.get_letters(), self.player_b_start)

class TestBagMethods(unittest.TestCase):
    def setUp(self):
        self.bag = BagClass()
    
    def test_initialize(self):
        self.assertEqual(len(self.bag.bag), 100) 
    
    def test_remove_tile(self):
        last = self.bag.bag[-1]
        self.assertEqual(self.bag.remove_tile(), last)
    
    def test_get_bag_size(self):
        self.assertEqual(self.bag.get_bag_size(), len(self.bag.bag))

class TestBoardMethods(unittest.TestCase):
    def setUp(self):
        self.board = BoardClass()
    def test_board_scores(self):
        scores = [[2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2], 
                  [1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1],
                  [1, 1, 2, 1, 1, 3, 1, 1, 1, 3, 1, 1, 2, 1, 1],
                  [1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 1, 2, 1, 1, 1],
                  [1, 3, 1, 1, 2, 1, 1, 3, 1, 1, 2, 1, 1, 3, 1],
                  [1, 1, 3, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1, 1],
                  [1, 1, 1, 3, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 1],
                  [3, 1, 1, 1, 3, 1, 1, 2, 1, 1, 3, 1, 1, 1, 3],
                  [1, 1, 1, 3, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 1],
                  [1, 1, 3, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1, 1],
                  [1, 3, 1, 1, 2, 1, 1, 3, 1, 1, 2, 1, 1, 3, 1],
                  [1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 1, 2, 1, 1, 1],
                  [1, 1, 2, 1, 1, 3, 1, 1, 1, 3, 1, 1, 2, 1, 1],
                  [1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1],
                  [2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2]]
        scores = np.array(scores)
        self.assertTrue(np.array_equal(self.board.board_scores, scores, equal_nan=True))
        self.assertSequenceEqual(self.board.board_scores.tolist(), scores.tolist())
    
    def test_place_word(self):
        self.board.place_word("was", "down", (7,7))
        self.board.place_word("sole", "right", (7, 9))
        new_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 'W', 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 'A', 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 'S', 'O', 'L', 'E', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertSequenceEqual(self.board.board_letters, new_board)
        self.assertFalse(self.board.place_word("emergency", "down", (15, 15)))
        self.assertFalse(self.board.place_word("emergency", "down", (10, 9)))
    
class TestWordMethods(unittest.TestCase):
    def setUp(self):
        self.bag = BagClass()
        self.player1 = PlayerClass("a", self.bag)
        self.board = BoardClass()
        self.word1 = WordClass("word", (7,7), "down", self.player1)
        self.word2 = WordClass("alksjd", (7,7), "down", self.player1)
        self.word3 = WordClass("wind", (6,4), "down", self.player1)
        self.word4 = WordClass("emergency", (11,11), "down", self.player1)

    def test_dictionary_check(self):
        self.assertTrue(self.word1.word_checker())
        self.assertFalse(self.word2.word_checker())

    def test_repeats(self):
        self.board.guesses.append("word")
        self.board.guesses.append("wind")
        self.board.guesses.append("wind")
        self.assertTrue(self.word1.check_repeat(self.board))
        self.assertFalse(self.word3.check_repeat(self.board))
    
    def test_valid_first_word(self):
        self.assertTrue(self.word1.valid_first_word(self.board))
        self.assertFalse(self.word3.valid_first_word(self.board))
    
    def test_calculate_points(self):
        self.assertEqual(self.word1.calculate_points(self.board), 16)
        self.assertEqual(self.word3.calculate_points(self.board), 10)
        self.assertEqual(self.word4.calculate_points(self.board), 0)

if __name__ == '__main__':
    unittest.main()