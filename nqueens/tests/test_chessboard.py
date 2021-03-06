import unittest
from nqueens.chessboard import Chessboard
from nqueens.threat import Threat


class TestChessboard(unittest.TestCase):

    def setUp(self):
        self.standardBoard = Chessboard.create(4)

    def testCreateOk(self):
        self.assertEqual(self.standardBoard.getSize(), 4)

    def testCreateInvalid(self):
        with self.assertRaises(ValueError):
            Chessboard.create(0)

    def testHasQueenOk(self):
        self.assertFalse(self.standardBoard.hasQueen(0, 0))

    def testPlaceQueens(self):
        self.standardBoard.placeQueen(1, 1)
        self.standardBoard.placeQueen(2, 2)
        self.assertTrue(self.standardBoard.hasQueen(1, 1))
        self.assertTrue(self.standardBoard.hasQueen(2, 2))

    def testPlaceDuplicateQueen(self):
        self.standardBoard.placeQueen(1, 1)
        with self.assertRaises(ValueError):
            self.standardBoard.placeQueen(1, 1)

    def testRemoveQueen(self):
        self.standardBoard.placeQueen(1, 1)
        self.standardBoard.removeQueen(1, 1)
        self.assertFalse(self.standardBoard.hasQueen(1, 1))

    def testCountQueens(self):
        self.assertEqual(self.standardBoard.getQueenCount(), 0)
        self.standardBoard.placeQueen(1, 1)
        self.assertEqual(self.standardBoard.getQueenCount(), 1)

    def testValidateEmpty(self):
        self.assertTrue(self.standardBoard.isValid())

    def testValidateHorizontal(self):
        self.standardBoard.placeQueen(0, 0)
        self.standardBoard.placeQueen(1, 0)
        self.assertFalse(self.standardBoard.isValid())

    def testValidateVertical(self):
        self.standardBoard.placeQueen(0, 0)
        self.standardBoard.placeQueen(0, 3)
        self.assertFalse(self.standardBoard.isValid())

    def testValidateDiagonal(self):
        self.standardBoard.placeQueen(0, 0)
        self.standardBoard.placeQueen(3, 3)
        self.assertFalse(self.standardBoard.isValid())

    def testIsSafeQueenPositionTrue(self):
        self.assertTrue(self.standardBoard.isSafeQueenPosition(0, 0))

    def testIsSafeQueenPositionFalse(self):
        self.standardBoard.placeQueen(0, 0)
        self.assertFalse(self.standardBoard.isSafeQueenPosition(0, 0))
