#Joseph Harrison 2019
import random as r
import time

#make a template arr for maze
def make_arr(I, J):
    #top of arr
    arr = [['=' for j in range(2 * J + 1)]]
    for i in range(I):
        #create row with gaps
        row = ['=' if j % 2 == 0 else ' '
                for j in range(2 * J + 1)]
        arr.append(row)
        #solid wall
        arr.append(['=' for j in range(2 * J + 1)])
    return arr

#create a maze using backtracking
def make_maze(arr, p):
    #vertices we have visited
    visited = []
    #the stack is used for backtracking
    stack = [p]
    #vectors used to get next point
    vectors = [(2, 0), (-2, 0),
               (0, 2), (0, -2)]
    
    #backtracking will eventually exhaust
    #all positions in stack
    while len(stack) != 0:
        i, j = stack[-1]
        
        visited.append((i, j))

        arr[i][j] = 'o'

        possible = []
        #check for possible vectors
        for v in vectors:
            #transformed point
            t = i + v[0], j + v[1]
            #check if that point is valid
            if t[0] < 1 or t[0] > len(arr) - 1:
                continue
            elif t[1] < 1 or t[1] > len(arr[0]) - 1:
                continue
            #check to make sure we haven't 
            #already been there
            elif t in visited:
                continue
            else:
                possible.append((v, t))

        arr[i][j] = ' '

        #if there are no available spaces
        if len(possible) == 0:
            #backtrack
            #remove p from stack
            stack.pop()
        else:
            #randomly select new point
            v, t = r.choice(possible)

            #we need the vector to remove wall, 
            #w, between the current vertex and t
            wi, wj = i + v[0] // 2, j + v[1] // 2
            arr[wi][wj] = ' '

            #push the new point onto stack
            stack.append(t)

    return arr

def main():
    flag = False
    while not flag:
        try:
            x = int(input('x size: '))
            y = int(input('y size: '))
            if x % 2 == 1 and y % 2 == 1:
                flag = True
            else:
                print('must be odd')
        except ValueError:
            print('must be int')
    arr = make_arr(y, x)
    arr = make_maze(arr, (1, 1))
    arrStr = ''
    for row in arr:
        arrStr += ' '.join(row) + '\n'
    print(arrStr)

if __name__ == '__main__':
    main()
