import requests
from tkinter import *

top = Tk()
top.geometry('300x300')
gameID = -1
winCount = 0
lossCount = 0
winPercent = 0
textDisplay = Text(top)
winPercentCalc = Button(top, text="Calculate Win Rate")
title = "Legends of Runeterra Win/Loss Tracker"
titleDisplay = Label(top, text=title)
top.title(title)

def main():
    global gameID
    global winCount
    global lossCount
    global winPercent

    #try:
    response = requests.get("http://localhost:21337/game-result")

    if gameID != response.json()['GameID']:
        textDisplay.delete(1.0, END)
        localPlayerWon = response.json()['LocalPlayerWon']
        gameID =  response.json()['GameID']

        if localPlayerWon == True:
            winCount = winCount + 1
        else:
            lossCount = lossCount + 1

        textDisplay.insert(INSERT, str(winCount))
        textDisplay.insert(INSERT, '\n' + str(lossCount))

        if lossCount != 0:
            textDisplay.insert(INSERT, '\n' +  str(winCount/lossCount))
        else:
            textDisplay.insert(INSERT, '\n' +  str(winCount))
    #else:
    #    raise Exception()
    #except:
    #    textDisplay.insert(END, "Sorry, something went wrong with fetching Data")


winPercentCalc.pack()
textDisplay.pack()
titleDisplay.pack()

while True:
    top.update_idletasks()
    top.update()
    main()
top.mainloop()
