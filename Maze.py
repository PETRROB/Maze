import tkinter as tk
import pygame
import sys
import os
import time
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

    #open_manual()

    root = tk.Tk()
    root.title("Maze Game")
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

    butt_manual = tk.Button(root, text="MANUAL!", command=lambda: open_manual(),image=img_back, compound=tk.CENTER, fg="white", font=LARGE_FONT_S, borderwidth=0)
    butt_manual.place(x = 200, y = 450)

    butt_exit = tk.Button(root, text="EXECUTE THE GAME!", command=lambda: execute_game(root), image=img_back, compound=tk.CENTER, fg="white", font=LARGE_FONT_S, borderwidth=0)
    butt_exit.place(x = 200, y = 550)
    

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
    new_window.title("Maze Game")
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
    diff_choice.title("Maze Game")
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
    

    butt_Easy = tk.Button(diff_choice, text = "Easy!", command=lambda: easy_game(diff_choice),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Easy.place(x = 200, y = 250)
    butt_Medium = tk.Button(diff_choice, text = "Medium!", command=lambda: med_game(diff_choice),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Medium.place(x = 200, y = 350)
    butt_Hard = tk.Button(diff_choice, text = "Hard!", command=lambda: hard_game(diff_choice),   image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Hard.place(x = 200, y = 450)


    diff_choice.mainloop()

def name_Board(text_box):
    
    score_table = open("score_board.txt", "a")
    score_table.write(text_box + "\n")
    score_table.close()



def game(diff_choice, WIDTH, HEIGHT, end_x, end_y, maze, player_x, player_y):

    diff_choice.destroy()

    pygame.init()
    # size of the window and time
    FPS = 30

    # define the background colour
    grey=(255/3,255/3,255/3)
   
    # create a window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Game")

    # upload the images
    player_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/player.png")
    player_img = pygame.transform.scale(player_img, (20, 20))
    end_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/end.png")
    end_img = pygame.transform.scale(end_img, (20, 20))
    wall_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/wall.jpeg")
    wall_img = pygame.transform.scale(wall_img, (20, 20))
    checkpoint_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/checkpoint.png")
    checkpoint_img = pygame.transform.scale(checkpoint_img, (20, 20))
    checkpoint1_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/checkpoint.png")
    checkpoint1_img = pygame.transform.scale(checkpoint1_img, (20, 20))
    checkpoint2_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/checkpoint.png")
    checkpoint2_img = pygame.transform.scale(checkpoint2_img, (20, 20))
    grey_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/grey.png")
    grey_img = pygame.transform.scale(grey_img, (20, 20))

    # clock time
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y // 20][player_x // 20 - 1] != "#":
            if maze[player_y // 20][player_x // 20-1]=='a':
                checkpoint_img=grey_img
            elif maze[player_y // 20][player_x // 20-1]=='b':
                checkpoint1_img=grey_img
            elif maze[player_y // 20][player_x // 20-1]=='$':
                checkpoint2_img=grey_img
            player_x -= 20
        elif keys[pygame.K_RIGHT] and player_x < WIDTH - 20 and maze[player_y // 20][player_x // 20 + 1] != "#":
            if maze[player_y // 20][player_x // 20+1]=='a':
                checkpoint_img=grey_img
            elif maze[player_y // 20][player_x // 20+1]=='b':
                checkpoint1_img=grey_img
            elif maze[player_y // 20][player_x // 20+1]=='$':
                checkpoint2_img=grey_img
            player_x += 20
        elif keys[pygame.K_UP] and player_y > 0 and maze[player_y // 20 - 1][player_x // 20] != "#":
            if maze[player_y // 20-1][player_x // 20]=='a':
                checkpoint_img=grey_img
            elif maze[player_y // 20-1][player_x // 20]=='b':
                checkpoint1_img=grey_img
            elif maze[player_y // 20-1][player_x // 20]=='$':
                checkpoint2_img=grey_img
            player_y -= 20
        elif keys[pygame.K_DOWN] and player_y < HEIGHT - 20 and maze[player_y // 20 + 1][player_x // 20] != "#":
            if maze[player_y // 20+1][player_x // 20]=='a':
                checkpoint_img=grey_img
            elif maze[player_y // 20+1][player_x // 20]=='b':
                checkpoint1_img=grey_img
            elif maze[player_y // 20+1][player_x // 20]=='$':
                checkpoint2_img=grey_img
            player_y += 20

        

        # show the background
        screen.fill(grey)

        # make the map
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "#":
                    screen.blit(wall_img, (j * 20, i * 20))

        # checkpoint
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "$":
                    screen.blit(checkpoint2_img, (j * 20, i * 20))

        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "a":
                    screen.blit(checkpoint_img, (j * 20, i * 20))

        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "b":
                    screen.blit(checkpoint1_img, (j * 20, i * 20))

        # show the player and exit
        screen.blit(player_img, (player_x, player_y))
        screen.blit(end_img, (end_x, end_y))

        # reach the exit
        if player_x == end_x and player_y == end_y:
            print("Congratulations! You won!")
            running = False
 
  
        
        pygame.display.flip()
        clock.tick(FPS)
    if player_x == end_x and player_y == end_y:
        name_Board("Win")
    else:
        name_Board("Lose")

    pygame.quit()
    main_page()
    sys.exit()

def easy_game(diff_choice):
    
    name_Board("Easy")
    
    WIDTH, HEIGHT = 480,600
    
    # define the starting point
    player_x, player_y = 0, 20

    # define the exit
    end_x, end_y = WIDTH-20, HEIGHT-40

    maze = [
    '########################',
    'S   #           b      #',
    '# # ########### ## ### #',
    '# #           #  #   # #',
    '# ########### ###### # #',
    '# #       # #      # # #',
    '# # ##### # ###### # # #',
    '#   #   # #        # # #',
    '# ### # # ######## # ###',
    '# #   # # #      # #   #',
    '# # ### # # #### # ### #',
    '#   # # #   #    #   # #',
    '##### # ##### ## ### # #',
    '#   # #  #  # #  # #   #',
    '# # #    # ## #### #####',
    '# #    #    #          #',
    '# ###### #### ######## #',
    '# #      #         # # #',
    '# # ###### ####### # # #',
    '# # #    # #     # # # #',
    '#   #  # # a # #     # #',
    '# ###### ########### # #',
    '# #           #    # # #',
    '# ### ####### # #### # #',
    '#  $  #     # #      # #',
    '####### ### # ###### ###',
    '#   #     # # #    # # #',
    '# ### ### ### # #### # #',
    '#       #              E',
    '########################',
    ]
    
    game(diff_choice, WIDTH, HEIGHT, end_x, end_y, maze, player_x, player_y)


def med_game(diff_choice):

    name_Board("Medium")
    # define the starting point
    player_x, player_y = 0, 20
    
    WIDTH, HEIGHT = 940,600

    end_x, end_y = WIDTH-20, 20

    maze = [
    '###############################################',
    'S   #                  #  $ #                 E',
    '# # ########### ## ### # # ########### ## ### #',
    '# #           #  #   # # #           #  #   # #',
    '# ########### ###### # # ########### ###### # #',
    '# #       # #      # # # #       # #      # # #',
    '# # ##### # ###### # # # # ##### # ###### # # #',
    '#       # #        # # #   #   # #        # # #',
    '# ##### # ######## # ### ### # # ######## # ###',
    '# # # # # #      # #   # # # # # #      # #   #',
    '# # # # # # #### # ### # # ### # # #### # ### #',
    '#   # #   #    #   #   #   # # #   #    #   # #',
    '##### # ##### ## ### # ##### # ##### ## ### # #',
    '#   # #  #  # #  # #   #   # #  #  # #  # #   #',
    '# # # # ## ## #### ##### # #    # ## #### #####',
    '# #   #     #          # #    #    #          #',
    '# ######## ## ######## # ###### #### ######## #',
    '# #      #  #      # # # #      #         # # #',
    '# # ###### #######a# # # # ###### ####### # # #',
    '# #      # #     ### # # # #    # #     # # # #',
    '#   #  #     # #     # #   #  # #   # #     #b#',
    '# ################## # # ###### ########### # #',
    '# #           #    # # # #           #    # # #',
    '# ### ####### # #### # # ### ####### # #### # #',
    '#     #     # #      # #     #     # #      # #',
    '####### ### # ################ ### # ###### ###',
    '#   #     # # #    # #     #     # # #    # # #',
    '# ### ### ### # #### # # ### ### ### # #### # #',
    '#       #              #       #              #',
    '###############################################',
    ]
    
    game(diff_choice, WIDTH, HEIGHT, end_x, end_y, maze, player_x, player_y)

def hard_game(diff_choice):
    name_Board("Hard")
    
    WIDTH, HEIGHT = 940,1060

    # define the starting point
    player_x, player_y = 0, 20

    # define the exit
    end_x, end_y =  0, HEIGHT-40

    

    maze = [
    '###############################################',
    'S   #                  #  a #                 #',
    '# # ########### ## ### # # ########### ## ### #',
    '# #           #  #   # # #           #  #   # #',
    '# ########### ###### # # ########### ###### # #',
    '# #       # #      # # # #       # #      # # #',
    '# # ##### # ###### # # # # ##### # ###### # # #',
    '#   #   # #        # # #   #   # #        # # #',
    '# ### # # ######## # ### ### # # ######## # ###',
    '# #   # # #      # #   # #   # # #      # #   #',
    '# # ### # # #### # ### # # ### # # #### # ### #',
    '#   # # #   #    #   # #   # # #   #    #   # #',
    '##### # ##### ## ### # ##### # ##### ## ### # #',
    '#   # #  #  # #  # #   #   # #  #  # #  # #   #',
    '# # #    # ## #### ##### # #    # ## #### #####',
    '# #    #    #          # #    #    #          #',
    '# ###### #### ######## # ###### #### ######## #',
    '# #      #         # # # #      #         # # #',
    '# # ###### ####### # # # # ###### ####### # # #',
    '# # #    # #     # # # # # #    # #     # # # #',
    '#   #  # #   # #     # #   #  # #   # #     # #',
    '# ###### ########### # # ###### ########### # #',
    '#                  # # #                  # # #',
    '############################################# #',
    '#   #                  #    #                 #',
    '# # ########### ## ### # # ########### ## ### #',
    '# #           #  #   # # #           #  #   # #',
    '# ########### ###### # # ########### ###### # #',
    '# #       # #      # # # #       # #      # # #',
    '# # ##### #$###### # # # # ##### # ###### # # #',
    '#   #   # #        # # #   #   # #        # # #',
    '# ### # # ######## # ### ### # # ######## # ###',
    '# #   # # #      # #   # #   # # #      # #   #',
    '# # ### # # #### # ### # # ### # # #### # ### #',
    '#   # # #   #    #   # #   # # #   #    #   # #',
    '##### # ##### ## ### # ##### # ##### ## ### # #',
    '#   # #  #  # #  # #   #   # #  #  # #  # #   #',
    '# # #    # ## #### ##### # #    # ## #### #####',
    '# #    #    #          # #    #    #          #',
    '# ###### #### ######## # ###### #### ######## #',
    '# #      #         # # # #      # b       # # #',
    '# # ###### ####### # # # # ###### ####### # # #',
    '# # #    # #     # # # # # #    # #     # # # #',
    '#   #  # #   # #     # #   #  # #   # #     # #',
    '# ###### ########### # # ###### ########### # #',
    '# #           #    # # # #           #    # # #',
    '# ### ####### # #### # # ### ####### # #### # #',
    '#     #     # #      # #     #     # #      # #',
    '####### ### # ###### ######### ### # ###### ###',
    '#   #     # # #    # # #   #     # # #    # # #',
    '# ### ### ### # #### # # ### ### ### # #### # #',
    'E       #     #                #              #',
    '###############################################',
    ]
    
    game(diff_choice, WIDTH, HEIGHT, end_x, end_y, maze, player_x, player_y)


def score_board(root):
    
    root.destroy()  # Close the current window
    name = []
    difficulty = []
    status = []
    y = 0

    # Create a new window
    score_board = tk.Tk()
    score_board.title("Maze Game")
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
        
        if y % 3 == 1:
            difficulty.append(a)
        elif y % 3 == 2:
            status.append(a)
        else:
            name.append(a)
        
        y += 1
    
    table = ttk.Treeview(score_board, columns=("name","difficulty","status"), show = "headings")
    table.heading("name", text = "Player Name")
    table.heading("difficulty", text= "Difficulty")
    table.heading("status", text = "Win or Lose")
    table.place(x = 100, y = 0)
    
    for i in range(len(name)):
        data = (name[i], difficulty[i], status[i])
        table.insert(parent = "", index = 0, values = data)
    
    

    butt_Back = tk.Button(score_board, text = "Back!", command=lambda: go_back_from_score_board(score_board),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Back.place(x = 200, y = 697)


    score_board.mainloop()

def open_manual():
    file_path = "C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/manual.txt"
    # Check if the file exists before attempting to open
    if os.path.exists(file_path):
        # Open the file using the default associated application
        os.startfile(file_path)
    else:
        print(f"The file '{file_path}' does not exist.")


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