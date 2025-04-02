from random import randint
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.minsize(300, 200)
root.maxsize(300, 200)
root.title('King Spel')

player_one_textLabel = tk.Label(root, text="Player One: ")
player_two_textLabel = tk.Label(root, text="Player Two: ")
score_textLabel = tk.Label(root, text="Score: ")
result_textLabel = tk.Label(root, text="")

player_one_textLabel.pack()
player_two_textLabel.pack()
score_textLabel.pack()
result_textLabel.pack()

def waithere():
    var = IntVar()
    root.after(1000, var.set, 1)
    root.wait_variable(var)

def playGame():
    play_game = "Y"
    player_one_score = 0
    player_two_score = 0
    roundsPlayed = 0
    maxRound = 3

    while play_game == "Y":
        player_one_roll = randint(1, 6)
        player_two_roll = randint(1, 6)
        
        if player_one_roll > player_two_roll:
            result_textLabel.config(text=f"Player One wins with the number:  {player_one_roll}")
            player_one_textLabel.config(text=f"Player One:  {player_one_roll}")
            player_two_textLabel.config(text=f"Player Two:  {player_two_roll}")
            player_one_score += 1
            roundsPlayed += 1
        elif player_two_roll > player_one_roll:
            result_textLabel.config(text=f"Player Two wins with the number:  {player_two_roll}")
            player_one_textLabel.config(text=f"Player One:  {player_one_roll}")
            player_two_textLabel.config(text=f"Player Two:  {player_two_roll}")
            player_two_score += 1
            roundsPlayed += 1
        else:
            result_textLabel.config(text=f"Tie")
            player_one_textLabel.config(text=f"Player One:  {player_one_roll}")
            player_two_textLabel.config(text=f"Player Two:  {player_two_roll}")
            roundsPlayed += 1
        score_textLabel.config(text=f"Score: [{player_one_score}:{player_two_score}]")
        waithere()
        if player_one_score >= maxRound:
            play_game = "N"
            result_textLabel.config(text=f"Game Over! Player One won!")
            score_textLabel.config(text=f"Score: [{player_one_score}:{player_two_score}]")
        elif player_two_score >= maxRound:
            play_game = "N"
            result_textLabel.config(text=f"Game Over! Player Two won!")
            score_textLabel.config(text=f"Score: [{player_one_score}:{player_two_score}]")
        elif roundsPlayed == maxRound:
            play_game = "N"
            if player_one_score > player_two_score:
                result_textLabel.config(text=f"Game Over! Player One won!")
                score_textLabel.config(text=f"Score: [{player_one_score}:{player_two_score}]")
            elif player_two_score > player_one_score:
                result_textLabel.config(text=f"Game Over! Player Two won!")
                score_textLabel.config(text=f"Score: [{player_one_score}:{player_two_score}]")
            else:
                result_textLabel.config(text=f"Nobody Wins! You both SUCK!")
                score_textLabel.config(text=f"Score: [{player_one_score}:{player_two_score}]")

play_button = tk.Button(root, text='Play', command=playGame)
quit_button = tk.Button(root, text='Quit', command=root.quit)
play_button.pack()
quit_button.pack()

root.mainloop()