import pygame
import sys

pygame.init()

# size of the window and time
WIDTH, HEIGHT = 470,590
FPS = 30

# define the background colour
grey=(255/3,255/3,255/3)
# define the map and checkpoint
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
    '# #           #    # # # #           #    # # #',
    '# ### ####### # #### # # ### ####### # #### # #',
    '#     #     # #      # #     #     # #      # #',
    '####### ### # ###### ######### ### # ###### ###',
    '#   #     # # #    # # #   #     # # #    # # #',
    '# ### ### ### # #### # # ### ### ### # #### # #',
    '#       #                      #     #        #',
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

# create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# upload the images
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (10, 10))
end_img = pygame.image.load("end.png")
end_img = pygame.transform.scale(end_img, (10, 10))
wall_img = pygame.image.load("wall.jpeg")
wall_img = pygame.transform.scale(wall_img, (10, 10))
checkpoint1_img = pygame.image.load("checkpoint.png")
checkpoint1_img = pygame.transform.scale(checkpoint1_img, (10, 10))
checkpoint2_img = pygame.image.load("checkpoint.png")
checkpoint2_img = pygame.transform.scale(checkpoint2_img, (10, 10))
checkpoint3_img = pygame.image.load("checkpoint.png")
checkpoint3_img = pygame.transform.scale(checkpoint3_img, (10, 10))
grey_img = pygame.image.load("grey.png")
grey_img = pygame.transform.scale(grey_img, (10, 10))

# clock time
clock = pygame.time.Clock()

# define the starting point
player_x, player_y = 0, 10

# define the exit
end_x, end_y =  0, HEIGHT-20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y // 10][player_x // 10 - 1] != "#":
        if maze[player_y // 10][player_x // 10-1]=='a':
            checkpoint2_img=grey_img
        elif maze[player_y // 10][player_x // 10-1]=='b':
            checkpoint3_img=grey_img
        elif maze[player_y // 10][player_x // 10-1]=='$':
            checkpoint1_img=grey_img
        player_x -= 10
    elif keys[pygame.K_RIGHT] and player_x < WIDTH - 10 and maze[player_y // 10][player_x // 10 + 1] != "#":
        if maze[player_y // 10][player_x // 10+1]=='a':
            checkpoint2_img=grey_img
        elif maze[player_y // 10][player_x // 10+1]=='b':
            checkpoint3_img=grey_img
        elif maze[player_y // 10][player_x // 10+1]=='$':
            checkpoint1_img=grey_img
        player_x += 10
    elif keys[pygame.K_UP] and player_y > 0 and maze[player_y // 10 - 1][player_x // 10] != "#":
        if maze[player_y // 10-1][player_x // 10]=='a':
            checkpoint2_img=grey_img
        elif maze[player_y // 10-1][player_x // 10]=='b':
            checkpoint3_img=grey_img
        elif maze[player_y // 10-1][player_x // 10]=='$':
            checkpoint1_img=grey_img
        player_y -= 10
    elif keys[pygame.K_DOWN] and player_y < HEIGHT - 10 and maze[player_y // 10 + 1][player_x // 10] != "#":
        if maze[player_y // 10+1][player_x // 10]=='a':
            checkpoint2_img=grey_img
        elif maze[player_y // 10+1][player_x // 10]=='b':
            checkpoint3_img=grey_img
        elif maze[player_y // 10+1][player_x // 10]=='$':
            checkpoint1_img=grey_img
        player_y += 10

    

    # show the background
    screen.fill(grey)

    # make the map
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "#":
                screen.blit(wall_img, (j * 10, i * 10))

    # checkpoint
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "$":
                screen.blit(checkpoint1_img, (j * 10, i * 10))

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "a":
                screen.blit(checkpoint2_img, (j * 10, i * 10))

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "b":
                screen.blit(checkpoint3_img, (j * 10, i * 10))

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