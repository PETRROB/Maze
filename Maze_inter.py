import tkinter as tk
from tkinter import *
from time import strftime
from tkinter import ttk
from random import choice


LARGE_FONT_S = ("Arial", 26, "bold")
DIG_FONT_S = ("Arial", 24, "bold")
DEF_FONT_S = ("Arial", 20)

BILA_1 = "#F8FAFF"
BILA = "#FFFFFF"
SV_MODRA = "#CCEDFF"
SV_SEDA = "#F5F5F5"
BOARD = "#25265E"


def main_page():

    root = tk.Tk()
    root.title("Labyrinth")
    root.geometry("800x800")
    root.resizable(0, 0)
    root.configure(background='black')

    text_label = tk.Label(root, text = "MAZE!!!",  bg="black", fg="yellow", font=DIG_FONT_S, borderwidth=0)
    text_label.grid(row=1, column=2, sticky=tk.N )

    # Center the buttons vertically
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(4, weight=1)

    butt_start = tk.Button(root, text="START!", command=lambda: start_game(root), bg="black", fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_start.grid(row=2, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

    butt_score = tk.Button(root, text="SCORE BOARD!", command=lambda: score_board(root), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
    butt_score.grid(row=3, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

    butt_exit = tk.Button(root, text="EXECUTE THE GAME!", command=lambda: execute_game(root), bg="black", fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_exit.grid(row=4, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

    # Adjust column weights to center buttons horizontally
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)

    # Create a label for the time
    time_label = tk.Label(root, font=DEF_FONT_S, bg="black", fg="white")
    time_label.grid(row=999, column=3, sticky=tk.SE, padx=0, pady=0)

    # Start updating the time
    update_time(time_label)

    root.mainloop()


def start_game(root):
    # Function to close the current window and open a new window with a text box
    root.destroy()  # Close the current window

    # Create a new window
    new_window = tk.Tk()
    new_window.title("Labyrinth")
    new_window.geometry("800x800")
    new_window.resizable(0, 0)
    new_window.configure(background='black')

    # Add a text box to the new window
    text_box = tk.Text(new_window, height=1, width=30, font=DIG_FONT_S)
    text_box.pack()

    butt_sendText = tk.Button(new_window, text="Next", command=lambda: diff_choice(new_window, text_box), bg="black", fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_sendText.pack()

    butt_Back = tk.Button(new_window, text="Back!", command=lambda: go_back_from_play(new_window), bg="black", fg="yellow", font=DIG_FONT_S, borderwidth=0)
    butt_Back.pack()

    new_window.mainloop()

def diff_choice(new_window, text_box):
    
    name_Board(text_box.get("1.0", "end-1c"))  # Get the content of the text box

    new_window.destroy()

    diff_choice = tk.Tk()
    diff_choice.title("Labyrinth")
    diff_choice.geometry("800x800")
    diff_choice.resizable(0, 0)
    diff_choice.configure(background='black')

    butt_Easy = tk.Button(diff_choice, text = "Easy!", command=lambda: game(), bg="black", fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Easy.grid(row=1, column=1, sticky=tk.N + tk.W +tk.E +tk.S)
    butt_Medium = tk.Button(diff_choice, text = "Medium!", command=lambda: game(), bg="black", fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Medium.grid(row=2, column=1, sticky=tk.N + tk.W +tk.E +tk.S)
    butt_Hard = tk.Button(diff_choice, text = "Hard!", command=lambda: game(), bg="black", fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Hard.grid(row=3, column=1, sticky=tk.N + tk.W +tk.E +tk.S)


    diff_choice.mainloop()

def name_Board(text_box):
    
    score_table = open("score_board.txt", "a")
    score_table.write(text_box + "\n")
    score_table.close()



def game():
    pass
    

def score_board(root):
    
    root.destroy()  # Close the current window
    name = []
    status = []
    y = 0

    # Create a new window
    score_board = tk.Tk()
    score_board.title("Labyrinth")
    score_board.geometry("800x800")
    score_board.resizable(0, 0)
    score_board.configure(background='black')

    score_table = open("score_board.txt", "r")
    score_read = score_table.readlines()
    score_table.close()
    
    for i in score_read:
        a = i.strip("\n")
        
        if y % 2 == 0:
            name.append(a)
        else:
            status.append(a)
        
        y += 1
    
    table = ttk.Treeview(score_board, columns=("name","status"), show = "headings")
    table.heading("name", text = "Player Name")
    table.heading("status", text = "Win or Lose")
    table.pack()
    print(name)
    print(status)

    for i in range(len(name)):
        data = (name[i], status[i])
        table.insert(parent = "", index = 0, values = data)

    butt_Back = tk.Button(score_board, text = "Back!", command=lambda: go_back_from_score_board(score_board), bg="black", fg="yellow", font=DIG_FONT_S, borderwidth=0)
    butt_Back.pack()

    score_board.mainloop()

    

def execute_game(root):
    print("You exit a game!!!")
    root.destroy()  # Close the Tkinter window

def go_back_from_score_board(score_board):
    score_board.destroy()
    main_page()

def go_back_from_play(start_game):
    start_game.destroy()
    main_page()

def update_time(label):
    time_string = strftime("%H:%M:%S %p")
    label.config(text=time_string)
    label.after(1000, update_time, label)  # Update every 1000 milliseconds (1 second)

main_page()