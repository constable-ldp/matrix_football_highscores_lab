import unittest

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):
    # Tests
    def setUp(self):
        self.matrix = Matrix("9 8 7\n5 3 2\n6 6 7")


    # def test_extract_row_from_one_number_matrix(self):
    #     matrix = Matrix("1")
    #     self.assertEqual(matrix.row(1), [1])

    def test_rows(self):
        self.assertEqual([[9, 8, 7], [5, 3, 2], [6, 6, 7]], self.matrix.row())

    def test_columns__1(self):
        self.assertEqual([[9, 5, 6], [8, 3, 6], [7, 2, 7]], self.matrix.column())

    def test_matrix(self):
        new_matrix = Matrix("9 8 7 3\n5 3 2 3\n6 6 7 3")
        self.assertEqual([[9, 8, 7, 3], [5, 3, 2, 3], [6, 6, 7, 3]], new_matrix.row())
        self.assertEqual([[9, 5, 6], [8, 3, 6], [7, 2, 7], [3, 3, 3]], new_matrix.column())

    # Test can extract a given row

    # Test can extract a given row where numbers have different number of digits
    # Example matrix:
    #
    # 1 2
    # 10 20

    # Test can extract row from non-square matrix
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6

    # Test can extract a column

    # Test can extract column from a one number matrix

    # Test can extract a column from non-square matrix
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    #
    # 89 1903 3
    # 18 3 1
    # 9 4 800



