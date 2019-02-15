import unittest
from nqueens.queen import Queen
from nqueens.threat import Threat


class TestQueen(unittest.TestCase):

    def setUp(self):
        self.queen = Queen(1, 2)

    def testGetPosition(self):
        self.assertEqual(self.queen.getPosition(), (1, 2))
