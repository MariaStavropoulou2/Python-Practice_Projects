import unittest
import rps_logging as rps


class RPS_Test(unittest.TestCase):
    def test_game1(self):
        game = rps.Player()
        game.Test_Winner('R', 'S')
        self.assertGreater(int(game.Player_Score), int(game.Computer_Score), msg="Round 1 Win Player FAIL!")
        game.Test_Winner('R', 'P')
        self.assertEqual(int(game.Player_Score), int(game.Computer_Score), msg="Round 2 Win Computer FAIL!")
        game.Test_Winner('R', 'R')
        self.assertEqual(game.Player_Move, game.Computer_Move, msg="Round 3 Draw FAIL!")
        game.Test_Winner('P', 'S')
        game.Test_Winner('S', 'R')
        game.Test_Winner('S', 'P')
        game.Test_Winner('P', 'P')
        self.assertTrue(game.Player_Score == 2, msg="Finally Player Score Failed")
        self.assertTrue(game.Computer_Score == 3, msg="Finally Computer Score Failed")

    def test_game2(self):
        game = rps.Player()
        game.Test_Winner('P', 'S')
        self.assertGreater(int(game.Computer_Score), int(game.Player_Score), msg="Round 1 Win Player FAIL!")
        game.Test_Winner('S', 'P')
        self.assertEqual(int(game.Player_Score), int(game.Computer_Score), msg="Round 2 Win Computer FAIL!")
        game.Test_Winner('S', 'S')
        self.assertEqual(game.Player_Move, game.Computer_Move, msg="Round 3 Draw FAIL!")
        game.Test_Winner('P', 'P')
        game.Test_Winner('R', 'P')
        game.Test_Winner('P', 'S')
        game.Test_Winner('R', 'S')
        self.assertTrue(game.Player_Score == 2, msg="Finally Player Score Failed")
        self.assertTrue(game.Computer_Score == 3, msg="Finally Computer Score Failed")


if __name__ == '__main__':
    unittest.main()
