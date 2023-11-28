import tkinter as tk
from tkinter import *
from time import strftime
from tkinter import ttk
from random import choice
from tkinter import messagebox
from PIL import ImageTk, Image



LARGE_FONT_S = ("Arial", 26, "bold")
LARGE_FONT_S_TITLE = ("Arial", 36, "bold")
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
    imgTemp = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Pict.png")
    imgTemp_bck = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Lab_bckgrd_01.jpg")
    img2 = imgTemp.resize((800,800))
    img3 = imgTemp_bck.resize((400,100))
    img = ImageTk.PhotoImage(img2)
    img_back = ImageTk.PhotoImage(img3)

    label = Label(root,image=img)
    label.pack(side='top',fill=Y)

    text_label = tk.Label(root, text="MAZE!!!", image=img_back, compound=tk.CENTER, fg="white", font = LARGE_FONT_S_TITLE, borderwidth=0)
    text_label.place(x = 200, y = 50)

    butt_start = tk.Button(root, text="START!", command=lambda: start_game(root),image=img_back, compound=tk.CENTER, fg="white", font=LARGE_FONT_S, borderwidth=0)
    butt_start.place(x = 200, y = 250)

    butt_score = tk.Button(root, text="SCORE BOARD!", command=lambda: score_board(root), image=img_back, compound=tk.CENTER, fg="white", font=LARGE_FONT_S, borderwidth=0)
    butt_score.place(x = 200, y = 350)

    butt_exit = tk.Button(root, text="EXECUTE THE GAME!", command=lambda: execute_game(root), image=img_back, compound=tk.CENTER, fg="white", font=LARGE_FONT_S, borderwidth=0)
    butt_exit.place(x = 200, y = 450)

    # Create a label for the time
    time_label = tk.Label(root, font=LARGE_FONT_S, bg="black", fg="white")
    time_label.place(x = 595, y = 755)
        # Start updating the time
    update_time(time_label)

    root.mainloop()


def start_game(root):
    # Function to close the current window and open a new window with a text box
    root.destroy()  # Close the current window

    show_popup()
    # Create a new window
    new_window = tk.Tk()
    new_window.title("Labyrinth")
    new_window.geometry("800x800")
    new_window.resizable(0, 0)
    

    imgTemp = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Pict.png")
    imgTemp_bck = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Lab_bckgrd_01.jpg")
    img2 = imgTemp.resize((800,800))
    img3 = imgTemp_bck.resize((400,100))
    img = ImageTk.PhotoImage(img2)
    img_back = ImageTk.PhotoImage(img3)

    label = Label(new_window,image=img)
    label.place(x = 0, y = 0)
    #label.pack(side='top',fill=Y)

    text_box = tk.Text(new_window, height=1, width=32, font=DIG_FONT_S)
    text_box.place(x = 100, y = 100)

    

    butt_sendText = tk.Button(new_window, text="Next", command=lambda: diff_choice(new_window, text_box),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_sendText.place(x = 200, y = 200)

    butt_Back = tk.Button(new_window, text="Back!", command=lambda: go_back_from_play(new_window), image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Back.place(x = 200, y = 300)

    new_window.mainloop()

def diff_choice(new_window, text_box):
    
    name_Board(text_box.get("1.0", "end-1c"))  # Get the content of the text box

    new_window.destroy()

    diff_choice = tk.Tk()
    diff_choice.title("Labyrinth")
    diff_choice.geometry("800x800")
    diff_choice.resizable(0, 0)
    imgTemp = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Pict.png")
    imgTemp_bck = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Lab_bckgrd_01.jpg")
    img2 = imgTemp.resize((800,800))
    img3 = imgTemp_bck.resize((400,100))
    img = ImageTk.PhotoImage(img2)
    img_back = ImageTk.PhotoImage(img3)

    label = Label(diff_choice,image=img)
    label.pack(side='top',fill=Y)
    

    butt_Easy = tk.Button(diff_choice, text = "Easy!", command=lambda: game(),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Easy.place(x = 200, y = 250)
    butt_Medium = tk.Button(diff_choice, text = "Medium!", command=lambda: game(),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Medium.place(x = 200, y = 350)
    butt_Hard = tk.Button(diff_choice, text = "Hard!", command=lambda: game(),   image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Hard.place(x = 200, y = 450)


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
    imgTemp = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Pict.png")
    imgTemp_bck = Image.open("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/Lab_bckgrd_01.jpg")
    img2 = imgTemp.resize((800,800))
    img3 = imgTemp_bck.resize((400,100))
    img = ImageTk.PhotoImage(img2)
    img_back = ImageTk.PhotoImage(img3)

    label = Label(score_board, image=img)
    label.pack(side='top',fill=Y)
    
    
    butt_Back = tk.Button(score_board, text = "Back!", command=lambda: go_back_from_score_board(score_board),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Back.place(x = 200, y = 697)
    
    
    
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
    table.place(x = 200, y = 0)
    
    for i in range(len(name)):
        data = (name[i], status[i])
        table.insert(parent = "", index = 0, values = data)
    
    

    butt_Back = tk.Button(score_board, text = "Back!", command=lambda: go_back_from_score_board(score_board),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Back.place(x = 200, y = 697)


    score_board.mainloop()


def show_popup():
    root = tk.Tk()
    root.withdraw()
    
    message = "Please, input into the text field your player name!"
    # Show a pop-up message box
    messagebox.showinfo("Message", message)

    # Destroy the temporary root window
    root.destroy()

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