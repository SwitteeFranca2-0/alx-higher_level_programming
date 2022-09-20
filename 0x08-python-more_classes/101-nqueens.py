#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N\n")
    exit(1)

try:
    N = int(sys.argv[1])
except:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

queen = "%"
chess_board = []

for i in range(N):
    chess_board.append(["_" for i in range(N)])
print(chess_board)

for i in range(N):
    chess_board[i][0] = queen 
chess_board[0][1] = queen
print(chess_board)

for i in range(N):
    for j in range(N):
        if chess_board[i][j] == "%":
            position = [i, j]
            dimen_check(position)


def dimen_check(position):
    x, y = position
    column_check(x, y)
    diag_check(x, y)


def column_check(v-al, val2):
    i = 1
    while (i + val2 < N):
        if check_board(val + i, val2) == queen:
            chess_board[x, y] = "_"
            val2 += 1
            chess_board[val, val2] = queen
            i = 1
        i++
    return

def diag_check(x, y):
    i = 1
    while(i + x < N and i + y < N):
        if check_board(x + i, y + i) == queen:
            chess_board[x, y] = "_"
            y += 1
            x += 1
            chess_board[x, y] = queen
            i = 1
        i++
    return

def run_check()