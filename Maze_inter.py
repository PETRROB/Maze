import tkinter as tk
from time import strftime

LARGE_FONT_S = ("Arial", 26, "bold")
DIG_FONT_S = ("Arial", 24, "bold")
DEF_FONT_S = ("Arial", 20)

BILA_1 = "#F8FAFF"
BILA = "#FFFFFF"
SV_MODRA = "#CCEDFF"
SV_SEDA = "#F5F5F5"
BOARD = "#25265E"

def start_game():
    print("You started a game!!!")

def score_board():
    print("Open your score board!")

def execute_game(root):
    print("You exit a game!!!")
    root.destroy()  # Close the Tkinter window

def update_time(label):
    time_string = strftime("%H:%M:%S %p")
    label.config(text=time_string)
    label.after(1000, update_time, label)  # Update every 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Labyrinth")
root.geometry("600x600")
root.resizable(0, 0)
root.configure(background='black')

# Center the buttons vertically
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)

butt_start = tk.Button(root, text="START!", command=lambda: start_game(), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_start.grid(row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

butt_score = tk.Button(root, text="SCORE BOARD!", command=lambda: score_board(), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_score.grid(row=2, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

butt_exit = tk.Button(root, text="EXECUTE THE GAME!", command=lambda: execute_game(root), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_exit.grid(row=3, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

# Adjust column weights to center buttons horizontally
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Create a label for the time
time_label = tk.Label(root, font=DEF_FONT_S, bg=BILA, fg=BOARD)
time_label.grid(row=4, column=1, sticky=tk.SE, padx=0, pady=0)

# Start updating the time
update_time(time_label)

root.mainloop()
