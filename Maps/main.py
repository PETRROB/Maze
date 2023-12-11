import pygame
import sys

pygame.init()

# size of the window and time
WIDTH, HEIGHT = 940,600
FPS = 30

# define the background colour
grey=(255/3,255/3,255/3)
# define the map and checkpoint
# define the map and checkpoint
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
end_x, end_y = WIDTH-20, HEIGHT-580

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
            checkpoint_img=grey_img
        elif maze[player_y // 20][player_x // 20-1]=='$':
            checkpoint_img=grey_img
        player_x -= 20
    elif keys[pygame.K_RIGHT] and player_x < WIDTH - 20 and maze[player_y // 20][player_x // 20 + 1] != "#":
        if maze[player_y // 20][player_x // 20+1]=='a':
            checkpoint_img=grey_img
        elif maze[player_y // 20][player_x // 20+1]=='b':
            checkpoint_img=grey_img
        elif maze[player_y // 20][player_x // 20+1]=='$':
            checkpoint_img=grey_img
        player_x += 20
    elif keys[pygame.K_UP] and player_y > 0 and maze[player_y // 20 - 1][player_x // 20] != "#":
        if maze[player_y // 20-1][player_x // 20]=='a':
            checkpoint_img=grey_img
        elif maze[player_y // 20-1][player_x // 20]=='b':
            checkpoint_img=grey_img
        elif maze[player_y // 20-1][player_x // 20]=='$':
            checkpoint_img=grey_img
        player_y -= 20
    elif keys[pygame.K_DOWN] and player_y < HEIGHT - 20 and maze[player_y // 20 + 1][player_x // 20] != "#":
        if maze[player_y // 20+1][player_x // 20]=='a':
            checkpoint_img=grey_img
        elif maze[player_y // 20+1][player_x // 20]=='b':
            checkpoint_img=grey_img
        elif maze[player_y // 20+1][player_x // 20]=='$':
            checkpoint_img=grey_img
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
                screen.blit(checkpoint_img, (j * 20, i * 20))

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "a":
                screen.blit(checkpoint_img, (j * 20, i * 20))

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "b":
                screen.blit(checkpoint_img, (j * 20, i * 20))
# show the player and exit
    screen.blit(player_img, (player_x, player_y))
    screen.blit(end_img, (end_x, end_y))

    # reach the exit
    if player_x == end_x and player_y == end_y:
        print("Congratulations! You won!")
        running = False
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()