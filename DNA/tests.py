import unittest
from funcs import brute_force, lcs, lcs_table


class MyTestCase(unittest.TestCase):
    # test brute force method
    def test_brute_force(self):
        seq1 = "AATCGAG"
        seq2 = "CCATCGG"
        self.assertEqual(brute_force(seq1, seq2), (5, "ATCGG"))

    # test lcs method
    def test_lcs(self):
        seq1 = "AATCGAG"
        seq2 = "CCATCGG"
        self.assertEqual(lcs(seq1, seq2), (5, "ATCGG"))

    # test lcs table method
    def test_lcs_table_list(self):
        self.assertEqual(
            lcs_table("ABCDE", "CEFGH"),
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 2, 2, 2, 2],
            ],
        )


if __name__ == "__main__":
    unittest.main()
