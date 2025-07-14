"""
Created on Mon June 21 18:08:13 2025

@author: Ayushman Dwivedi
ALSO ADDED GUI FOR NXT LVL GAMING EXPERIENCE
"""

#TICTACTOE_GAME.py
#USED GUI,MINIMAX,ALPHA-BETA,AND PROPER WIN DETECTION
# Author: AYUSHMAN DWIVEDI(100% human effort)

import tkinter as tk
from tkinter import messagebox
import random
board = [""] * 9
current_player = "O"  
difficulty = "Hard" #DEFAULT DIFFICULTY  

# Check winner or tie
def check_winner(bd):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a, b, c in wins:
        if bd[a] == bd[b] == bd[c] != "":
            return bd[a]
    if "" not in bd:
        return "Tie"
    return None

# Minimax with alpha-beta pruning
def minimax_ab(bd, player, alpha, beta):
    winner = check_winner(bd)
    if winner == "X":
        return {'score': 1}
    elif winner == "O":
        return {'score': -1}
    elif winner == "Tie":
        return {'score': 0}

    if player == "X":
        best = {'score': -float('inf')}
    else:
        best = {'score': float('inf')}

    for i in range(9):
        if bd[i] == "":
            bd[i] = player
            result = minimax_ab(bd, "O" if player == "X" else "X", alpha, beta)
            bd[i] = ""
            result['index'] = i

            if player == "X":
                if result['score'] > best['score']:
                    best = result
                alpha = max(alpha, best['score'])
            else:
                if result['score'] < best['score']:
                    best = result
                beta = min(beta, best['score'])

            if beta <= alpha:
                break
    return best

# AI Move logic
def ai_move():
    empty = [i for i in range(9) if board[i] == ""]

    if difficulty == "Easy":
        idx = random.choice(empty)
    elif difficulty == "Medium":
        priority = [4,0,2,6,8]
        idx = next((i for i in priority if i in empty), random.choice(empty))
    else:
        move = minimax_ab(board, "X", -float('inf'), float('inf'))
        idx = move['index']

    board[idx] = "X"
    buttons[idx]["text"] = "X"
    post_move()

# Human click
def on_click(i):
    if buttons[i]["text"] == "" and not check_winner(board):
        buttons[i]["text"] = current_player
        board[i] = current_player

        winner = check_winner(board)
        if winner:
            show_result(winner)
            return

        # AI thinking delayi(GIVE FULL VIBE)
        root.after(600, ai_move)

# After any move (AI or player)
def post_move():
    winner = check_winner(board)
    if winner:
        show_result(winner)

def show_result(winner):
    if winner == "Tie":
        msg = "It's a tie!"
    else:
        msg = f"{winner} wins!"
    messagebox.showinfo("Game Over", msg)
    reset_game()

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "O"
    for b in buttons:
        b.config(text="")

def set_difficulty(level):
    global difficulty
    difficulty = level
    reset_game()

# GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe vs AI")

# Difficulty selection
tk.Label(root, text="Difficulty:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
tk.Button(root, text="Easy", width=6, command=lambda: set_difficulty("Easy")).grid(row=0, column=1)
tk.Button(root, text="Medium", width=6, command=lambda: set_difficulty("Medium")).grid(row=0, column=2)
tk.Button(root, text="Hard", width=6, command=lambda: set_difficulty("Hard")).grid(row=0, column=3)

# Game board
buttons = []
for idx in range(9):
    b = tk.Button(root, text="", font=("Helvetica", 28),
                  width=4, height=2, command=lambda i=idx: on_click(i))
    b.grid(row=(idx // 3) + 1, column=idx % 3, padx=2, pady=2)
    buttons.append(b)

root.mainloop()

