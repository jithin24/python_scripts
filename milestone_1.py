# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 00:12:32 2019

@author: Jithin George
Milestone project 1 from Python-3 Bootcamp course
"""

board = []

#Initialize the Board with spaces
def initialize():
    '''
    This Function helps to initialize the Board with spaces
    '''
    return [' ']*9
    
def validate_input(i_char):
        return (i_char.upper() == 'X' or i_char.upper() == 'O')

def player_input(p_val, inp_val, board):
    '''
    This function is used to validate the user input
    Post validation it inserts X or O onto the Game board
    '''
    if str(inp_val).isdigit():
        num_val = int(inp_val)
        pass
    else:
        print('ERROR: Sorry! Position value keyed-in is Invalid. Enter 1-9')
        return False
    
    #Verify and assign the num position on Board
    if(num_val<=9 and board[num_val-1] == " " and num_val>0):
        board[num_val-1] = p_val
        #print('SUCCESS: Entry added successfully\n')
        return True
    else:
        if(num_val==0 or num_val>9):
            print('ERROR: Sorry! Position value keyed-in is Invalid. Enter 1-9')
            return False
        print('ERROR: Sorry! Position is already occupied ' + board[num_val-1] +'\n')
        return False

def exec_game(key, value):
    '''
    This Function runs one instance of the Game and displays the Board 
    post successful completion
    '''
    while(True):
        val = input(key + ': Enter your preferred num position (1-9) for ' + value + "\n")
        if(player_input(value, val, board)):
            #print(board)
            display_board(board)
            break
        else:
            continue
    return True

def check_win(play_value):
    '''
    Function verifies if the Tic Tac board slots are filled as 
    per rules and proclaims the winner. If no winning rule is
    matched the Game continues with the next player's turn
    '''
    #FirstRow
    if(board[6] == board[7] == board[8] == play_value):
        return True
    #SecondRow
    elif(board[3] == board[4] == board[5] == play_value):
        return True
    #ThirdRow
    elif(board[0] == board[1] == board[2] == play_value):
        return True
    #Top-left Diagonal
    elif(board[6] == board[4] == board[2] == play_value):
        return True
    #Top-right Diagonal
    elif(board[8] == board[4] == board[0] == play_value):
        return True
    #First column
    elif(board[6] == board[3] == board[0] == play_value):
        return True
    #Second Column
    elif(board[7] == board[4] == board[1] == play_value):
        return True
    #Third Column
    elif(board[8] == board[5] == board[2] == play_value):
        return True
    else:
        return False
    
#Function to display the Tic Tac board with its values
def display_board(board):
    print(" " + board[6] + "  | " + board[7] + " |  " + board[8]);
    print("-------------");
    print(" " + board[3] + "  | " + board[4] + " |  " + board[5]);
    print("-------------");
    print(" " + board[0] + "  | " + board[1] + " |  " + board[2]);

#Main Program section
while(True):
    print("Hello!! This is the Tic-Tac-Toe Game simulation for Two players")
    board = initialize()
    players = {"p1" : " ", "p2": " "}
    display_board(board)
    while(True):
        valA = input("Player1 - Select your choice 'X' or 'O' \n")
        if(validate_input(valA)): 
            if(valA.upper()=='X'):
                players['p1']='X'
                players['p2']='O'
            else:
                players['p1']='O'
                players['p2']='X'
            print("Player1 =" + players['p1'] + " Player2 =" + players['p2'])
            break
        else:
            print("ERROR: Sorry! Only 'X' and 'O' are allowed in Tic-Tac-Toe Game\n")
            continue
            
    result = False
    counter = 0
    #Start the Game
    while(True):
        counter=counter+1
        if(counter%2!=0):
            exec_game('P1', players['p1'])
            if(check_win(players['p1'])):
                print("Congratulations!!! Player1 Wins")
                break
            else:
                pass
        else:
            exec_game('P2', players['p2'])
            if(check_win(players['p2'])):
                print("Congratulations!!! Player2 Wins")
                break
            else:
                pass
        #Run this Loop for each square on the Game
        if(counter==9):
            print('=== Game ends as a Draw ===')
            break
    inp = input("would you like to play again?\nPress 'Y' for New Game OR any Key to Quit\n")
    if(inp.upper() == 'Y'):
        pass
    else:
        break