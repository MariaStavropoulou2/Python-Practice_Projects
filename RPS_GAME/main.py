import rps_logging as rps_1
import rps_gui as gui
import rps as rps_2

choice_1 = int(input("Με ποιον τρόπο θέλετε να τρέξει το πρόγραμμα; (1 για εκτέλεση στην γραμμή εντολών,2 για εκτέλεση "
                     "σε γραφικό περιβάλλων)\n"))

if choice_1 == 1:
    choice_2 = int(input("Πως θέλετε να εμφανίζονται τα μηνύματα;(1 μέσω logging, 2 μέσω απλής εκτύπωσης μηνυμάτων)\n"))
    if choice_2 == 1:
        rps_1.main()
    else:
        rps_2.main()
else:
    gui.main()
