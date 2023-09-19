import tkinter as tk
import rps
from tkinter import ttk, messagebox

moves = {'Rock': 'R', 'Paper': 'P', 'Scissors': 'S'}
outcome = {'p': 'Player', 'c': 'Computer', 't': 'Tie Game'}


def play():
    # Ελέγχω αν ο αριθμός των γύρων είναι 0.
    if int(rpsobject.rounds) == 0:
        messagebox.showerror('Error in Rounds', 'Παρακαλώ συμπληρώστε τους γύρους!')
        return
    playermove = player.get()
    if int(rpsobject.round_cnt) == int(rpsobject.rounds):
        resultBox.config(text=str(rpsobject))
        return
    rpsobject.round(moves[playermove])
    # Εμφανίζω στο παράθυρο την κίνηση του υπολογιστή
    comp.config(state='normal')
    comp.delete(0, 'end')
    comp.insert(0, rpsobject.get_Computer_Move())
    comp.config(state='readonly')
    resultBox.config(text='Winner:' + str(outcome[rpsobject.winner]))


def setRounds():
    # Εισαγωγή αριθμού γύρων παιχνιδιού
    if len(rnds.get()) == 0:
        messagebox.showerror('Unfill blank', 'Παρακαλώ συμπληρώστε τους γύρους!')
        return
    rpsobject.set_Rounds(int(rnds.get()))


# Main Window
root = tk.Tk()
root.configure(bg="#ff9966")
root.geometry('750x530')
root.title("Rock Paper Scissors Game")
root.resizable(width=False, height=False)
rpsobject = rps.Player()

# First Frame
frame_1 = tk.Frame(master=root, bg="#ff9966")
lab = tk.Label(master=frame_1, width=19, justify=tk.CENTER, bg="#ff9966", fg='#00394d', bd=5,
               text='Επιλέξτε γύρους:', font=("calibri", 15))
rnds = tk.Entry(master=frame_1, width=12, justify=tk.CENTER, fg='#00394d', bd=5)
roundButton = tk.Button(master=frame_1, width=20, bg='#ff4d4d', fg='#00394d', bd=3, text='Rounds', command=setRounds,
                        font=("calibri", 13))
lab.grid(row=3, column=0, padx=7, pady=10)
rnds.grid(row=3, column=1, padx=7, pady=10)
roundButton.grid(row=3, column=2, padx=7, pady=10)
frame_1.pack()

# Second Frame
frame_2 = tk.Frame(master=root, bg="#ff9966")
label = tk.Label(master=frame_2, width=20, justify=tk.CENTER, fg='#00394d', bg="#ff9966", bd=5, text='Επιλέξτε κίνηση:',
                 font=("calibri", 15))
player = ttk.Combobox(master=frame_2, width=20, justify=tk.CENTER, values=('Rock', 'Paper', 'Scissors'),
                      font=("calibri", 15))
playbutton = tk.Button(master=frame_2, width=20, bg='#ff4d4d', fg='#00394d', bd=5, text='Play', command=play,
                       font=("calibri", 13))
label.grid(row=0, column=0, padx=10, pady=10)
player.grid(row=0, column=1, padx=10, pady=10)
playbutton.grid(row=0, column=2, padx=10, pady=10)
frame_2.pack()

# Third Frame
frame_3 = tk.Frame(master=root, bg="#ff9966")
lb = tk.Label(master=frame_3, width=25, justify=tk.CENTER, bg="#ff9966", fg='#00394d', bd=5, text='Κίνηση υπολογιστή: ',
              font=("calibri", 15))
comp = tk.Entry(master=frame_3, width=25, justify=tk.CENTER, fg='#00394d', bd=5, state='readonly')
lb.grid(row=1, column=0, padx=14, pady=10)
comp.grid(row=1, column=1, padx=14, pady=10)
frame_3.pack()

textheight = int(0.5 * root.winfo_screenheight())
resultBox = tk.Label(master=root, font=("calibri", 25), width=50, height=textheight, justify=tk.CENTER, bg='#00394d',
                     fg='#ff4d4d', text='Outcome')
resultBox.pack()


# Mainloop
def main():
    tk.mainloop()


if __name__ == '__main__':
    main()
