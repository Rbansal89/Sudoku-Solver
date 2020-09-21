
bo = [
    [0,0,0,0,0,0,0,0,0],
    [2,0,6,0,0,0,1,0,3],
    [3,0,0,1,7,6,0,0,8],
    [0,6,0,0,0,0,0,4,0],
    [0,0,0,0,9,0,0,0,0],
    [0,9,8,0,0,0,7,3,0],
    [9,1,0,0,3,0,0,6,5],
    [0,0,0,4,2,5,0,0,0],
    [0,0,3,0,6,0,4,0,0]
]

bod = [
    [8,2,7,1,5,4,3,9,6],
    [9,0,5,3,2,7,1,4,8],
    [0,4,0,6,8,0,7,5,2],
    [5,9,3,0,0,0,2,7,0],
    [4,7,0,5,1,3,6,8,9],
    [0,1,8,9,0,2,4,3,0],
    [7,0,6,2,3,0,9,1,4],
    [1,5,0,7,0,6,8,2,3],
    [2,3,9,8,4,1,5,0,7]
]
board = [
    [4,6,0,0,0,0,0,3,2],
    [9,0,5,0,6,0,1,0,8],
    [0,8,0,1,0,2,0,5,0],
    [6,0,0,0,0,0,0,0,3],
    [0,0,0,5,2,9,0,0,0],
    [0,1,0,0,0,0,0,9,0],
    [2,0,7,0,1,0,8,0,5],
    [0,3,0,0,0,0,0,2,0],
    [0,0,0,0,9,0,0,0,0],
    ]

board1 = [[0 for i in range(9)] for i in range(9)]
print(board1)
track_dict = {}

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(9):
            if bo[i][j] == 0:
                return i,j

def valid(bo,num,pos):
    x,y = pos
    for j in range(9):
        if bo[x][j] == num:
            return False
    for i in range(9):
        if bo[i][y] == num:
            return False
    #a, b = x // 3, y // 3
    for i in range(3):
        for j in range(3):
            u = i + 3 * (x // 3)
            v = j+3*(y//3)
            print(u,v)
            if board[u][v]==n: # and u!=x and v!=y:
                return False
    return True

# def valid(board, n, pos):
#     x,y = pos
#     global track_dict
#     if pos in track_dict and track_dict[pos] <= n:
#         del track_dict
#         return False
#     for i in range(len(board[x])):
#         if board[x][i]==n: #and i!=x
#             return False
#     for i in range(len(board)):
#         if board[i][y]==n: #and i!=y
#             return False
#     for i in range(3):
#         for j in range(3):
#             u = i+3*(x//3)
#             v = j+3*(y//3)
#             #print(u,v)
#             if board[u][v]==n: # and u!=x and v!=y:
#                 return False
#     return True



def print_board(bo):

    for i in range(len(bo)):
        if i%3==0 and i!= 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j%3 == 0 and j!= 0:
                print(" | ",end="")
            print(bo[i][j],end=" ")
        print()

def fill(bo,pos):
    global track_dict
    try:
        num = track_dict[pos]
        print("num: ",num)
    except:
        num = 0
    for i in range(num+1,10):
        #print("entered in valid")
        if valid(bo,i,pos):
            bo[pos[0]][pos[1]] = i
            return True
    return False

def solve(bo):
    global track_dict
    print_board(bo)
    pos = find_empty(bo)
    filled_lst = []

    i,j = pos
    while i<9:
        j = 0
        while j<9:
                print(i,j)
                if bo[i][j] !=0:
                    j+=1
                else:

                    if fill(bo,(i, j)):
                        print("fill:", i,j, bo[i][j])
                        filled_lst.append((i, j))
                        track_dict[(i,j)] = bo[i][j]
                        j += 1
                    else:
                        #print(filled_lst)
                            print("else filled: ",filled_lst)
                            bad_i, bad_j = filled_lst[-1][0], filled_lst[-1][1]
                        #if len(filled_lst) < 2:
                         #   track_dict[(bad_i,bad_j)] = bo[bad_i][bad_j]
                          #  bo[bad_i][bad_j] = 0
                          #  filled_lst.pop()
                          #  j += 1
                        #else:
                            i,j = bad_i,bad_j
                            bo[bad_i][bad_j] = 0
                            filled_lst.pop()
        # board  = [
        #     [4, 6, 0, 0, 0, 0, 0, 3, 2],
        #     [9, 0, 5, 0, 6, 0, 1, 0, 8],
        #     [0, 8, 0, 1, 0, 2, 0, 5, 0],
        #     [6, 0, 0, 0, 0, 0, 0, 0, 3],
        #     [0, 0, 0, 5, 2, 9, 0, 0, 0],
        #     [0, 1, 0, 0, 0, 0, 0, 9, 0],
        #     [2, 0, 7, 0, 1, 0, 8, 0, 5],
        #     [0, 3, 0, 0, 0, 0, 0, 2, 0],
        #     [0, 0, 0, 0, 9, 0, 0, 0, 0],
        # ]
        #print("\n")
        #print_board(bo)
        #print("\n")
        i +=1
    print_board(bo)

solve(board1)
#print(valid(bo,4,(0,0)))
