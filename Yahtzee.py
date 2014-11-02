"""Primitive yahtzee game I wrote while helping someone with their Intro to CS homework"""


import random
def rollDice():
    return [random.randint(1,6) for i in range(5)]
def isYahtzee(aList):
    g=True
    for i in aList:
        g=(aList[0]==i)and g
    return g
def replaceValue(diceList, i):
    diceList[i]=random.randint(1,6)
    return diceList
def newRoll(diceList,indexList):
    for i in range(len(indexList)):
        if indexList[i]:
            diceList =replaceValue(diceList, i)
    return diceList
def askTheUser():
    Accum=[]
    for i in range(1,6):
        g=input("Do you want to reroll die #" +str(i)+"? Please answer yes or no  :")
        g=g.lower()
        if g=="yes":
            Accum+=[1]
        else:
            Accum+=[0]
    return Accum
#this function allows the user to play a simplified version of Yahtzee!
def yahtzee():
        #simulate the rolling of the 5 dice to start the round
        myRoll = rollDice()
        #the user will be able to select specific dice to re-roll, and they can
        #do this two times in a single round. We will check to see if the user
        #rolled a Yahtzee. that is the only check that we will make in this
        #simplified version of the game.
        for i in range(0, 2):
            #display the results of the roll
            print(myRoll)
            #if the user rolled a Yahtzee, end the game. otherwise, ask the user
            #if they want to re-roll each die.
            if (isYahtzee(myRoll)):
                return "Yahtzee!"
            else:
                replaceList = askTheUser()
                #re-roll the dice selected
                newRoll(myRoll, replaceList)
                #show the user the result of the final re-roll
                print(myRoll)
                #check to see if the final re-roll produced a yahtzee
        if (isYahtzee(myRoll)):
            return("Yahtzee!")
        else:
            return "Bummer. You didn’t get a Yahtzee. Better luck next time!"

