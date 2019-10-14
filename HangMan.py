# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 01:58:03 2019

@author: Sadman Sakib
"""

import random
words = ["Bangladesh", "India", "Pakistan", "Srilanka", "Brazil" , "Spain",
        "England", "France", "Italy", "Portugal", "Nepal", "Bhutan", "Chaina",
        "Bolivia", "Croatia"]
def game():
    index=random.randint(1,len(words)-1)
    selectedWord = words[index-1]
    toBeChecked= ""
    for alph in selectedWord:
        toBeChecked += "*"
#   print(selectedWord)
    print(toBeChecked)
    chance=5
    while chance>=1 and selectedWord != toBeChecked:
        enteredAlphabet = input("Guess a letter:")
        i=0
        flag=0
        while i< len(selectedWord):
            if enteredAlphabet == selectedWord[i]:
                toBeChecked = toBeChecked[:i] + enteredAlphabet + toBeChecked[i+1:]   
                flag=1
            i=i+1
        if flag==1:
            print("Correct Guess !")
        else:
            print("Wrong Guess.")
            chance-=1
        print("You have "+ str(chance) + " chances remaining.")
        print("Current status:"+ str(toBeChecked))
    if(chance>0 and selectedWord == toBeChecked):
        print("*** You Win ***")
        choice = input("Enter Y to play again and N to exit.")
        if choice == "Y" or choice == "y":
            game()
        else:
            return
    if (chance==0):
        print("***Game Over! You Lose.***")
        choice = input("Enter Y to play again and N to exit.")
        if choice == "Y" or choice == "y":
            game()
        else:
            return
    return;

game()