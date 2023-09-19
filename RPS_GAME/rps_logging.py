import random as r
import logging as log
from time import time

# Κατασκευή Logger και μορφοποίηση του
logger = log.getLogger("RPS_Logger")
logger.setLevel(log.INFO)
sh = log.StreamHandler()
formatter = log.Formatter('%(levelname)s: %(message)s')
sh.setFormatter(formatter)
logger.addHandler(sh)

logger.debug('Έναρξη του προγράμματος!!')

mvs = {0: 'R', 1: 'S', 2: 'P'}

r.seed(time() * 1000)


def valid(move):
    return move in mvs.values()


class Player:
    def __init__(self):
        self.Computer_Score = 0
        self.Player_Score = 0
        self.Player_Move = " "
        self.Computer_Move = " "

    def Test_Winner(self, pm, cm):
        self.Player_Move = pm
        self.Computer_Move = cm
        if str(pm) == str(cm):
            return
        elif (str(pm) == 'R' and str(cm) == 'S') or (
                str(pm) == 'S' and str(cm) == 'P') or (
                str(pm) == 'P' and str(cm) == 'R'):
            self.Player_Score += 1
        else:
            self.Computer_Score += 1

    def Check_Winner(self):
        if str(self.Player_Move) == str(self.Computer_Move):
            return
        elif (str(self.Player_Move) == 'R' and str(self.Computer_Move) == 'S') or (
                str(self.Player_Move) == 'S' and str(self.Computer_Move) == 'P') or (
                str(self.Player_Move) == 'P' and str(self.Computer_Move) == 'R'):
            self.Player_Score += 1
        else:
            self.Computer_Score += 1

    def Choices(self):
        rounds = int(input('Δωσε αριθμό γύρων: \n'))
        for i in range(rounds):
            self.Player_Move = input('\nΔώστε μία από τις παρακάτω επιλογές (R, P, S):\n')
            # Μετατροπή γραμμάτων σε κεφαλαία για να αποκλείσουμε το
            # ενδεχόμενο να ληφθεί ως λάθος η επιλογή των πεζών σωστών γραμμάτων
            self.Player_Move = self.Player_Move.upper()
            while not valid(self.Player_Move):
                logger.warning('Η επιλογή σας είναι λανθασμένη!!!')
                self.Player_Move = input('Δώστε μία από τις παρακάτω επιλογές (R, P, S):\n')
                self.Player_Move = self.Player_Move.upper()
            self.Computer_Move = mvs[r.randint(0, 2)]
            self.Check_Winner()
            ms1 = str(i + 1) + 'ος γύρος:'
            ms2 = '\tΟ υπολογιστής έπαιξε: ' + self.Computer_Move + '\tΟ παίκτης έπαιξε: ' + self.Player_Move + '\n'
            ms3 = 'Το σκορ είναι:\t Υπολογιστής: ' + str(self.Computer_Score) + '\t Παίκτης: ' + str(self.Player_Score)
            logger.info(ms1 + ms2 + ms3)
        if self.Player_Score == self.Computer_Score:
            ms4 = 'Φέρατε ισοπαλία με τον Υπολογιστή!!'
        elif self.Player_Score > self.Computer_Score:
            ms4 = 'Συγχαρητήρια!! Κερδίσατε τον Υπολογιστή!!'
        else:
            ms4 = 'Δυστυχώς σας κέρδισε ο Υπολογιστής!!'
        logger.info(ms4)


def main():
    rps_game = Player()
    rps_game.Choices()


logger.debug('Τέλος προγράμματος!!')

if __name__ == '__main__':
    main()
