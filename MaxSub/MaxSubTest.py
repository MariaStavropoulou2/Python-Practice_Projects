import unittest
import MaxSub


class MyTestCase(unittest.TestCase):
    def test_Prefix(self):
        sequence = [2, 13, 18, -22, -12]
        sums = MaxSub.prefix(sequence)
        self.assertEqual(sums, [2, 15, 33, 11, -1])

    def test_Max_Sub_Slow(self):
        sequence = [2, 13, 18, -22, 12]
        mss = MaxSub.MaxSubSlow(sequence)
        self.assertEqual(mss, (33, 0, 2))

    def test_Max_Sub_Faster(self):
        sequence = [2, 13, 18, -22, 12]
        msfr = MaxSub.MaxSubFaster(MaxSub.prefix(sequence))
        self.assertEqual(msfr, (33, 0, 2))

    def test_Max_Sub_Fastest(self):
        sequence = [2, 13, 18, -22, 12]
        msfs = MaxSub.MaxSubFastest(sequence)
        self.assertEqual(msfs, (33, 0, 2))


if __name__ == "__main__":
    unittest.main()
