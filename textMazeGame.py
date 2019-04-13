#Joseph Harrison 2019
#maze game
from mazeArray import make_arr
from mazeArray import make_maze
import random as r

def main():
    cont = ''
    I, J = 11, 19
    while cont != 'q':
        
        #create maze as array
        arr = make_arr(I, J)
        #create start and endpoints
        i, j = 2 * r.randint(0, (I - 2) // 2) + 1, 2 * r.randint(0, (J - 2) // 2) + 1
        end = 2 * r.randint(0, (I - 2) // 2) + 1, 2 * r.randint(0, (J - 2) // 2) + 1
        arr = make_maze(arr, (i, j))
        arr[end[0]][end[1]] = '$'

        userin = ''
        while userin != 'q' and (i, j) != end:

            #mark player
            arr[i][j] = 'o' 

            #draw arr
            arrStr = ''
            for row in arr:
                arrStr += ' '.join(row) + '\n'
            print(arrStr)

            #get input from user
            userin = input('>>> ')
        
            arr[i][j] = ' '

            #validate input and move player
            if userin == 'w' and arr[i - 1][j] != '=':
                i, j = i - 1, j
            elif userin == 'a' and arr[i][j - 1] != '=':
                i, j = i, j - 1
            elif userin == 's' and arr[i + 1][j] != '=':
                i, j = i + 1, j
            elif userin == 'd' and arr[i][j + 1] != '=':
                i, j = i, j + 1
            else:
                arr[i][j] = 'o'
        
            if (i, j) == end:
                print("you've won")

        cont = input("new maze ('q' to quit): ")
    print('exiting...')

if __name__ == '__main__':
    main()
