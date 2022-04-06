import unittest
from scrabble_module import PlayerClass, BagClass, BoardClass, WordClass

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
        self.assertEqual(self.player_a.get_letters(), self.player_a_start[:-1])
        self.assertEqual(self.player_b.get_letters(), self.player_b_start[:-1])
    
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
    

if __name__ == '__main__':
    unittest.main()