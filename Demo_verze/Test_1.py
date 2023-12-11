import tkinter as tk
import pygame
import sys
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
    

    butt_Easy = tk.Button(diff_choice, text = "Easy!", command=lambda: game(diff_choice, 60),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Easy.place(x = 200, y = 250)
    butt_Medium = tk.Button(diff_choice, text = "Medium!", command=lambda: game(diff_choice, 30),  image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Medium.place(x = 200, y = 350)
    butt_Hard = tk.Button(diff_choice, text = "Hard!", command=lambda: game(diff_choice, 10),   image=img_back, compound=tk.CENTER, fg="white", font=DIG_FONT_S, borderwidth=0)
    butt_Hard.place(x = 200, y = 450)


    diff_choice.mainloop()

def name_Board(text_box):
    
    score_table = open("score_board.txt", "a")
    score_table.write(text_box + "\n")
    score_table.close()



def game(diff_choice, time_df):

    diff_choice.destroy()

    pygame.init()
    # size of the window and time
    WIDTH, HEIGHT = 700,600
    FPS = 30

    # define the background colour
    grey=(255/3,255/3,255/3)
    # define the map and checkpoint
    maze = [
        '########################',
        'S $ #                  #',
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
        '#   #  # #   # #     # #',
        '# ###### ########### # #',
        '# #           #    # # #',
        '# ### ####### # #### # #',
        '#     #     # #      # #',
        '####### ### # ###### ###',
        '#   #     # # #    # # #',
        '# ### ### ### # #### # #',
        '#       #              E',
        '########################',
    ]

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
    grey_img = pygame.image.load("C:/Users/robin/Desktop/SKOOL/Computer_prog_language/Semestral_Project/images/grey.png")
    grey_img = pygame.transform.scale(grey_img, (20, 20))

    
    
    # clock time
    clock = pygame.time.Clock()

    # define the starting point
    player_x, player_y = 0, 20

    # define the exit
    end_x, end_y = WIDTH-240, HEIGHT-40

    # customizing button
        # initializing font
    font = pygame.font.Font(None, 36)
        # Draw the execution button
    button_rect = pygame.Rect(535, 450, 115, 57)
    button_color = (169, 169, 169)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = font.render("Execute", True, (255, 255, 255))
        
        #time countdown
        
    button_rect_timer = pygame.Rect(535, 250, 115, 57)
    pygame.draw.rect(screen, button_color, button_rect_timer)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.USEREVENT:
                time_df -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.quit()
                    main_page()
                    sys.exit()
        
        a,b = pygame.mouse.get_pos()
        if button_rect.x <= a <= button_rect.x + 115 and button_rect.y <= b <= button_rect.y +57:
            pygame.draw.rect(screen,(169,169,169),button_rect )
        else:
            pygame.draw.rect(screen, (110,110,110),button_rect)
        
        screen.blit(button_text, (button_rect.x + 10, button_rect.y + 15))
        button_text_timer = font.render(f'timer: {time_df}', True, (255, 255, 255))
        screen.blit(button_text_timer, (button_rect_timer.x + 10, button_rect_timer.y + 15))

        # move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y // 20][player_x // 20 - 1] != "#":
            if maze[player_y // 20][player_x // 20-1]=='$':
                checkpoint_img=grey_img
            player_x -= 20
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 20 and maze[player_y // 20][player_x // 20 + 1] != "#":
            if maze[player_y // 20][player_x // 20+1]=='$':
                checkpoint_img=grey_img
            player_x += 20
        if keys[pygame.K_UP] and player_y > 0 and maze[player_y // 20 - 1][player_x // 20] != "#":
            if maze[player_y // 20-1][player_x // 20]=='$':
                checkpoint_img=grey_img
            player_y -= 20
        if keys[pygame.K_DOWN] and player_y < HEIGHT - 20 and maze[player_y // 20 + 1][player_x // 20] != "#":
            if maze[player_y // 20+1][player_x // 20]=='$':
                checkpoint_img=grey_img
            player_y += 20
        
        # meet the checkpoint 
        

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
                    screen.blit(checkpoint_img, (j * 20, i * 20))

        # show the player and exit
        screen.blit(player_img, (player_x, player_y))
        screen.blit(end_img, (end_x, end_y))

        # reach the exit
        if player_x == end_x and player_y == end_y:
            print("Congratulations! You won!")
            running = False

        
        

       
            
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        
        
        

        

    pygame.quit()
    main_page()
    sys.exit()

    
    

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