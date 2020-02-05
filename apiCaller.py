import requests
from tkinter import *

def calcAndDisplayWinLoss(gameID, winCount, lossCount, winPercent, textDisplay):
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

        textDisplay.insert(INSERT, "Wins: " + str(winCount))
        textDisplay.insert(INSERT, '\n' + "Losses: " + str(lossCount))
        textDisplay.insert(INSERT, '\n' + "Win Percentage: ")
        if lossCount != 0:
            textDisplay.insert(INSERT, str((winCount/lossCount)*100))
        else:
            textDisplay.insert(INSERT, str(winCount))
        textDisplay.insert(INSERT, "%")
    #else:
    #    raise Exception()
    #except:
    #    textDisplay.insert(END, "Sorry, something went wrong with fetching Data")


#winPercentCalc.pack()

if __name__ == "__main__":
    top = Tk()
    top.geometry('300x300')
    gameID = -1
    winCount = 0
    lossCount = 0
    winPercent = 0
    textDisplay = Text(top)
    #winPercentCalc = Button(top, text="Calculate Win Rate")
    title = "Legends of Runeterra Win/Loss Tracker"
    titleDisplay = Label(top, text=title)
    top.title(title)

    textDisplay.pack()
    titleDisplay.pack()
    while True:
        top.update()
        calcAndDisplayWinLoss(gameID, winCount, lossCount, winPercent, textDisplay)
    top.mainloop()
