import random as r
from time import time

mvs = {0: 'R', 1: 'S', 2: 'P'}
move_Parser = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

r.seed(time() * 1000)


def valid(move):
    return move in mvs.values()


class Player:
    def __init__(self):
        self.Computer_Score = 0
        self.Player_Score = 0
        self.rounds = 0
        self.round_cnt = 0
        self.Player_Move = " "
        self.Computer_Move = " "
        self.winner = " "

    def set_Rounds(self, rnds):
        self.Player_Score, self.Computer_Score, self.rounds, self.round_cnt = 0, 0, rnds, 1

    def Check_Winner(self):
        if str(self.Player_Move) == str(self.Computer_Move):
            self.winner = 't'
            return
        elif (str(self.Player_Move) == 'R' and str(self.Computer_Move) == 'S') or (
                str(self.Player_Move) == 'S' and str(self.Computer_Move) == 'P') or (
                str(self.Player_Move) == 'P' and str(self.Computer_Move) == 'R'):
            self.winner = 'p'
            self.Player_Score += 1
        elif (str(self.Computer_Move) == 'R' and str(self.Player_Move) == 'S') or (
                str(self.Computer_Move) == 'S' and str(self.Player_Move) == 'P') or (
                str(self.Computer_Move) == 'P' and str(self.Player_Move) == 'R'):
            self.winner = 'c'
            self.Computer_Score += 1
        else:
            return

    def Choices(self, pm):
        self.Player_Move = pm
        self.Computer_Move = mvs[r.randint(0, 2)]
        self.Check_Winner()

    def get_Computer_Move(self):
        return move_Parser[self.Computer_Move]

    def round(self, move):
        if int(self.round_cnt) == int(self.rounds):
            return
        self.Computer_Move = mvs[r.randint(0, 2)]
        self.Player_Move = move
        self.Check_Winner()
        self.round_cnt += 1

    def __str__(self):
        return f'Το σκορ είναι: Υπολογιστής: {self.Computer_Score} \t Παίκτης: {self.Player_Score}\n {"Συγχαρητήρια κερδίσατε!!" if self.Player_Score > self.Computer_Score else "Δυστυχώς σας κέρδισε ο υπολογιστής!" if self.Player_Score < self.Computer_Score else "Ισοπαλία!"}'


def main():
    rps_game = Player()
    rnd = input("Δωσε αριθμό γύρων: \n")
    for i in range(int(rnd)):
        rps_game.Choices(input('Δώστε μία από τις παρακάτω επιλογές (R, P, S):\n').upper())
        while not valid(rps_game.Player_Move):
            print('Η επιλογή σας είναι λανθασμένη!!!')
            rps_game.Choices(input('Δώστε μία από τις παρακάτω επιλογές (R, P, S):\n').upper())
        ms1 = str(i + 1) + 'ος γύρος:'
        ms2 = '\tΟ υπολογιστής έπαιξε: ' + rps_game.Computer_Move + '\tΟ παίκτης έπαιξε: ' + rps_game.Player_Move + '\n'
        ms3 = 'Το σκορ είναι:\t Υπολογιστής: ' + str(rps_game.Computer_Score) + '\t Παίκτης: ' + str(rps_game.Player_Score)
        print(ms1 + ms2 + ms3)
    if rps_game.Player_Score == rps_game.Computer_Score:
        ms4 = 'Φέρατε ισοπαλία με τον Υπολογιστή!!'
    elif rps_game.Player_Score > rps_game.Computer_Score:
        ms4 = 'Συγχαρητήρια!! Κερδίσατε τον Υπολογιστή!!'
    else:
        ms4 = 'Δυστυχώς σας κέρδισε ο Υπολογιστής!!'
    print(ms4)


if __name__ == '__main__':
    main()
