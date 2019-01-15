# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 00:12:32 2019

@author: Jithin George
Milestone project 1 from Python-3 Bootcamp course
"""

global board

def initialize():
    return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
def validate_input(i_char):
        return (i_char.upper() == 'X' or i_char.upper() == 'O')

def player_input(p_val, num_val, board):
    if(num_val<=9 and board[num_val-1] == " " and num_val>0):
        board[num_val-1] = p_val
        print('SUCCESS: Entry added successfully\n')
        return True
    else:
        if(num_val==0 or num_val>9):
            print('ERROR: Sorry! Position value keyed-in is Invalid. Enter 1-9')
            return False
        print('ERROR: Sorry! Position is already occupied ' + board[num_val-1] +'\n')
        return False

def exec_game(key, value):
    while(True):
        val = input(key + ': Enter your preferred num position (1-9) for ' + value + "\n")
        if(player_input(value, int(val), board)):
            #print(board)
            display_board(board)
            break
        else:
            continue
    return

def display_board(board):
    print(" " + board[6] + "  |  " + board[7] + " |  " + board[8]);
    print("--------------");
    print(" " + board[3] + "  |  " + board[4] + " |  " + board[5]);
    print("--------------");
    print(" " + board[0] + "  |  " + board[1] + " |  " + board[2]);

#display_board();
board = initialize()
players = {"p1" : " ", "p2": " "}
display_board(board)
while(True):
    valA = input("P1 - Select your choice 'X' or 'O' \n")
    players['p1']=valA
    if(validate_input(players['p1'])): 
        if(valA.upper()=='X'):
            players['p2']='O'
        else:
            players['p2']='X'
        print("Player1 = " + players['p1'] + "  Player2 = " + players['p2'])
        break
    else:
        print("ERROR: Sorry! Only 'X' and 'O' are allowed in Tic-Tac Game\n")
        continue
        
result = False
counter = 0
while(True):
    counter=counter+1
    if(counter%2!=0):
        exec_game('P1', players['p1'])
    else:
        exec_game('P2', players['p2'])
    if(counter==9):
        break
