import unittest
from Poker import (
    is_pair, is_three_of_a_kind, is_straight,
    is_flush, is_full_house, is_four_of_a_kind,
    is_royal_flush, test_combination
)


class TestPokerGame(unittest.TestCase):

    def test_is_pair(self):
        self.assertTrue(is_pair([0, 1, 2, 3, 0]))
        self.assertFalse(is_pair([0, 1, 2, 3, 4]))

    def test_is_three_of_a_kind(self):
        self.assertTrue(is_three_of_a_kind([0, 1, 2, 0, 0]))
        self.assertFalse(is_three_of_a_kind([0, 1, 2, 3, 4]))

    def test_is_straight(self):
        self.assertTrue(is_straight([0, 1, 2, 3, 4]))
        self.assertFalse(is_straight([0, 1, 2, 4, 5]))

    def test_is_flush(self):
        self.assertTrue(is_flush([0, 1, 2, 3, 4]))
        self.assertFalse(is_flush([0, 13, 26, 39, 2]))

    def test_is_full_house(self):
        self.assertTrue(is_full_house([0, 0, 1, 1, 1]))
        self.assertFalse(is_full_house([0, 1, 2, 3, 4]))

    def test_is_four_of_a_kind(self):
        self.assertTrue(is_four_of_a_kind([0, 13, 26, 39, 1]))
        self.assertFalse(is_four_of_a_kind([0, 1, 2, 3, 4]))

    def test_is_royal_flush(self):
        self.assertTrue(is_royal_flush([8, 9, 10, 11, 12]))
        self.assertFalse(is_royal_flush([0, 1, 2, 3, 4]))




if __name__ == '__main__':
    unittest.main()
