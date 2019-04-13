from mazeArray import make_arr
from mazeArray import make_maze
import pygame
import random as r

#size of each block
SIZE = 10
WALL_COL = (255, 0, 0)
PLAYER_COL = (255, 255, 0)
END_COL = (255, 0, 255)

def game_loop(arr, pi, pj, ei, ej):
    
    global blocks
    blocks = []

    #screen size
    X, Y = SIZE * len(arr[0]), len(arr) * SIZE
    pygame.init()
    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('maze game')
    clock = pygame.time.Clock()

    #game loop
    running = True
    while running:
        clock.tick(10)
        
        #handle os quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        screen.fill((0,0,0))
        
        #handle io
        key = pygame.key.get_pressed()
        #w for up
        if key[pygame.K_w] and arr[pi - 1][pj] != '=':
            pi -= 1
        #a for left
        elif key[pygame.K_a] and arr[pi][pj - 1] != '=':
            pj -= 1
        #s for down
        elif key[pygame.K_s] and arr[pi + 1][pj] != '=':
            pi += 1
        #d for right
        elif key[pygame.K_d] and arr[pi][pj + 1] != '=':
            pj += 1
            
        #draw walls
        x, y = 0, 0
        for row in arr:
            for item in row:
                if item == '=':
                    pygame.draw.rect(screen, WALL_COL,
                    pygame.Rect(x, y, SIZE, SIZE))
                x += SIZE
            y += SIZE
            x = 0

        #draw player
        pygame.draw.rect(screen, PLAYER_COL,
        pygame.Rect(pj * SIZE, pi * SIZE, SIZE, SIZE))

        #draw end
        pygame.draw.rect(screen, END_COL,
        pygame.Rect(ej * SIZE, ei * SIZE, SIZE, SIZE))
        
        #check if the player has won
        if pi == ei and pj == ej:
            print("you've won!")
            running = False

        pygame.display.flip()
    #if we leave the game loop
    #close the window
    pygame.quit()
    
def main():
    cont = ''
    while cont != 'q':
        
        #get difficulty from user
        flag = False
        while not flag:
            diff = input('easy (e), medium (m) or hard (h): ')
            if diff == 'e':
                I, J = 21, 21
                flag = True
            elif diff == 'm':
                I, J = 31, 31
                flag = True
            elif diff == 'h':
                I, J = 41, 41
                flag = True
        
        #create the maze array
        arr = make_arr(I, J)
        arr = make_maze(arr, (1, 1))
    
        #place the player
        wi, wj = (I - 1) // 2 - 1, (J - 1) // 2 - 1
        pi, pj = r.randint(0, wi), r.randint(0, wj)
        pi, pj = 2 * pi + 1, 2 * pj + 1

        #place end
        ei, ej = r.randint(0, wi), r.randint(0, wj)
        #make sure we are not placing the end on the player
        while ei == pi and ej == pj:
            ei, ej = r.randint(0, wi), r.randint(0, wj)
        ei, ej = 2 * ei + 1, 2 * ej + 1

        #run game with maze array
        game_loop(arr, pi, pj, ei, ej)

        cont = input("'q' to quit: ")
    print('exiting...')

if __name__ == '__main__':
    main()
