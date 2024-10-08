#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:13:53 2024

@author: marcus
"""

# 1) Get number of players and assign a name to each player
# 1.1) randomly assign a person as the werewolf
# 2) Display the available players names
# 3) Ask the user which player is werewolf
# 4) State if they are correct or not
# 4.1) if not correct remove player and go to step 2 again
# 4.2) if they are correct exit the game

import random
import sys

werewolf = 0
players = 0
playerList = []

nameList = ["Margaret Schaefer",
"Ishaan McDowell",
"Rayna West",
"Diego Combs",
"Irene Mayer",
"Yahir Marshall",
"Adalyn Gutierrez",
"Luca Fischer",
"Maci Peterson",
"Santiago Lara",
"Heidi Michael",
"Bronson Faulkner",
"Ansley Barry",
"Emery Mills",
"June Diaz",
"Nathan McMillan",
"Ezra Compton",
"Elina Wong",
"Walter Tran",
"Kylie Gaines",
"Talon Lyons"
]

def getPlayerNames():
    i = 0
    while i < players:
        # assign a player name from the list
        ranname = random.choice(nameList)
        #print(ranname)
        if ranname not in playerList:
            playerList.append(ranname)
            i += 1
        else:
            continue
        

def getPlayerNumbers():
    global players
    players = 0
    global werewolf
    while players < 3:
        players = input("How many players do you want? ")
        
        if players.isdigit():
            playtest = int(players)
            if playtest < 3 or playtest > 10:
                print("Please choose a number between 3 and 10")
                players = 0
            else:
                players = int(players)
        else:
            print("Please choose a number between 3 and 10")
            players = 0
            
    # print(f"You have {players} players")
    werewolf = random.randint(1, players)
    #print(f"Werewolf is player {werewolf}")
    getPlayerNames()
    # print(playerList)
    
def nightPhase():
    # you need to remove a random villager who is not the werewolf
    pass

def displayPlayers():
    i = 0
    for each in playerList:
        i += 1
        print(i, "=", each)

def guessWerewolf():
    # ask the user who they think is the werewolf
    global players, werewolf
    displayPlayers()
    while True:
        userChoice = input("Who do you think is the werewolf: ")

        try:
            userChoice = int(userChoice)
            if userChoice > players or userChoice < 0:
                print("That is an invalid choice.\nTry again")
                continue
            else:
                if userChoice == werewolf:
                    print("You successfully chose the werewolf!\nCongratulations")
                    break
                else:
                    print(f"You chose poorly.\nRemoving player {playerList[userChoice -1]}")
                    # remove the player
                    del playerList[userChoice - 1]
                    players += -1
                    if werewolf > userChoice:
                        werewolf += -1
                    #print(f"Werewolf is player {werewolf}")
                    print("These are the players left:")                    
                    #print(playerList)
                    displayPlayers()
                # if not then go again.
        except:
            print("That is an invalid choice.\nTry again")
            continue
        # if they guess the werewolf they win...
       


getPlayerNumbers()
guessWerewolf()
