from tkinter import *
import tkinter as tk

points = []
assists = []
rebounds = []
steals = []
blocks = []
fouls = []
fgShot = []
fgAttempt = []
threePointAttempt = []
threePointScored = []
freeThrowMade = []
freeThrowMissed = []
assistMade_Array = []
fgShot_Array = []
fgMade_Array = []
rebounds_Array = []
steal_Array = []
block_Array = []
foul_Array = []
threePointMade_Array = []
freeThrowMade_Array = []
freeThrowMissed_Array = []
fgAttempt_Array = []
threePointAttempt_Array = []

visitorScore = []
visitorScore_Array =[]

playerList = [] #Empty Player List

global buttonPress
buttonPress = False
global k
k = 1

root = Tk()
newWindow = Tk()

root.title("Bearkats Stat Tracker")
root.geometry("1920x1080")
root.configure(background="gray30")

def gameWindow():
    statTracker()
    root.deiconify() #Makes Game Window Reappear
    newWindow.destroy()

def mainWindow():
    root.withdraw()
    newWindow.title("New Window")
    newWindow.geometry("480x270")
    newWindow.configure(background="gray30")
    global k
    if buttonPress == True: #Changes Player Name & Label Numbers
        k += 1
        str(k)
        players = playerInput.get()
        playerList.append(players) #adds players into the List
    playerInput.delete(0, 'end') #clears Entry Box
    Button(newWindow, text='Insert Player ' + str(k), bg="black", command=buttonPressTrue, fg="white", highlightbackground="gray90", activebackground="deep sky blue").place(x=130, y=60, height=33, width=150)
    Label(newWindow, text='Player ' + str(k) + " Name", bg="black", fg="white", highlightbackground="gray90").place(x=5, y=15, height=35, width=110)

playerInput = Entry(newWindow) #Input Box
playerInput.place(x=5, y=60, height=30, width=110)

def buttonPressTrue():
    global buttonPress
    buttonPress = True
    mainWindow()

Button(newWindow, text='Start Game', bg="black", command=gameWindow, fg="white", highlightbackground="gray90", activebackground="deep sky blue").place(x=130, y=120, height=33, width=150)

def fgMade_Fun(j):
    get_points = points[j].get()
    add_points = int(get_points) + 2

    points[j].delete(0, tk.END)
    points[j].insert(0, add_points)

def fieldGoalAttempt(j):
    get_fgAttempt = fgAttempt[j].get()
    add_fgAttempt = int(get_fgAttempt) + 1

    fgAttempt[j].delete(0, tk.END)
    fgAttempt[j].insert(0, add_fgAttempt)

def fieldGoalShot(j):
    get_fgShot = fgShot[j].get()
    add_fgShot = int(get_fgShot) + 1

    fgShot[j].delete(0, tk.END)
    fgShot[j].insert(0, add_fgShot)

def threePointerAttempted(j):
    get_threePointAttempt = threePointAttempt[j].get()
    add_threePointAttempt = int(get_threePointAttempt) + 1

    threePointAttempt[j].delete(0, tk.END)
    threePointAttempt[j].insert(0, add_threePointAttempt)

def threePointerScored(j):
    get_threePointScored = threePointScored[j].get()
    add_threePointScored = int(get_threePointScored) + 1

    threePointScored[j].delete(0, tk.END)
    threePointScored[j].insert(0, add_threePointScored)

def addAssists(j):
    get_assists = assists[j].get()
    add_assists = int(get_assists) + 1

    assists[j].delete(0, tk.END)
    assists[j].insert(0, add_assists)

def addRebounds(j):
    get_rebounds = rebounds[j].get()
    add_rebounds = int(get_rebounds) + 1

    rebounds[j].delete(0, tk.END)
    rebounds[j].insert(0, add_rebounds)

def addSteals(j):
    get_steals = steals[j].get()
    add_steals = int(get_steals) + 1

    steals[j].delete(0, tk.END)
    steals[j].insert(0, add_steals)

def addBlocks(j):
    get_blocks = blocks[j].get()
    add_blocks = int(get_blocks) + 1

    blocks[j].delete(0, tk.END)
    blocks[j].insert(0, add_blocks)

def addFouls(j):
    get_fouls = fouls[j].get()
    add_fouls = int(get_fouls) + 1

    fouls[j].delete(0, tk.END)
    fouls[j].insert(0, add_fouls)

def threePointerMade(j):
    get_points = points[j].get()
    add_points = int(get_points) + 3

    points[j].delete(0, tk.END)
    points[j].insert(0, add_points)

def freeThrowMake(j):
    get_points = points[j].get()
    add_points = int(get_points) + 1

    points[j].delete(0, tk.END)
    points[j].insert(0, add_points)

    get_ftMade = freeThrowMade[j].get()
    add_ftMade = int(get_ftMade) + 1

    freeThrowMade[j].delete(0, tk.END)
    freeThrowMade[j].insert(0, add_ftMade)

def freeThrowMiss(j):
    get_ftMissed = freeThrowMissed[j].get()
    add_ftMissed = int(get_ftMissed) + 1

    freeThrowMissed[j].delete(0, tk.END)
    freeThrowMissed[j].insert(0, add_ftMissed)

def visitorScores(j):
    get_visitorScore = visitorScore[j].get()
    add_visitorScore = int(get_visitorScore) + 1

    visitorScore[j].delete(0, tk.END)
    visitorScore[j].insert(0, add_visitorScore)
def statTracker():
    global playerCount
    playerCount = len(playerList)
    pointCounter = 0
    xCoordinate = 0

    for j in range(0, playerCount):

        yCoordinate = 150
        xCoordinate += 200  # Seperates each column

        playerLabel = Label(root, text=playerList[j], bg="white", fg="black", highlightbackground="gray90", borderwidth=1,relief="raised").place(x=5 + xCoordinate, y=5 + yCoordinate, height=30, width=150)

        #points
        pointLabel = Label(root, text="Points: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y = 40 + yCoordinate, height=30, width=55)
        boxname = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        points.append(boxname)
        points[j].insert(0, 0)
        boxname.place(x=60 + xCoordinate, y=40 + yCoordinate, height=30, width=95)

        #assists
        assistLabel = Label(root, text="Assists: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y = 70 + yCoordinate, height=30, width=55)
        assistBox = Entry(root,bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        assists.append(assistBox)
        assists[j].insert(0, 0)
        assistBox.place(x=60 + xCoordinate, y=70 + yCoordinate, height=30, width=95)

        assistAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addAssists(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        assistMade_Array.append(assistAddition)
        assistAddition.place(x = 120 + xCoordinate, y = 76 + yCoordinate, height = 15, width =15)

        #rebounds
        reboundLabel = Label(root, text="Rebounds: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y = 100 + yCoordinate, height=30, width=55)
        reboundBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        rebounds.append(reboundBox)
        rebounds[j].insert(0, 0)
        reboundBox.place(x=60 + xCoordinate, y = 100 + yCoordinate, height=30, width=95)

        reboundAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addRebounds(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        rebounds_Array.append(reboundAddition)
        reboundAddition.place(x = 120 + xCoordinate, y = 106 + yCoordinate, height=15, width=15)

        #steals
        stealLabel = Label(root, text="Steals: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=130 + yCoordinate, height=30, width=55)
        stealBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        steals.append(stealBox)
        steals[j].insert(0, 0)
        stealBox.place(x=60 + xCoordinate, y = 130 + yCoordinate, height=30, width=95)

        stealAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addSteals(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        steal_Array.append(stealAddition)
        stealAddition.place(x = 120 + xCoordinate, y = 136 + yCoordinate, height=15, width=15)

        #blocks
        blockLabel = Label(root, text="Blocks: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=160 + yCoordinate, height=30, width=55)
        blockBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        blocks.append(blockBox)
        blocks[j].insert(0, 0)
        blockBox.place(x=60 + xCoordinate, y = 160 + yCoordinate, height=30, width=95)

        blockAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addBlocks(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        block_Array.append(blockAddition)
        blockAddition.place(x = 120 + xCoordinate, y = 166 + yCoordinate, height=15, width=15)

        #fouls
        foulsLabel = Label(root, text="Fouls: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=190 + yCoordinate, height=30, width=55)
        foulsBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        fouls.append(foulsBox)
        fouls[j].insert(0, 0)
        foulsBox.place(x=60 + xCoordinate, y = 190 + yCoordinate, height=30, width=95)

        foulsAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addFouls(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        foul_Array.append(foulsAddition)
        foulsAddition.place(x = 120 + xCoordinate, y = 196 + yCoordinate, height=15, width=15)

        # field goal made
        fgMade = Button(root, text='FG Made',
                        command=lambda pointCounter=pointCounter: [fieldGoalShot(pointCounter),
                                                                   fieldGoalAttempt(pointCounter),
                                                                   fgMade_Fun(pointCounter)]
                        , bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",
                        activebackground="deep sky blue")
        fgMade_Array.append(fgMade)
        fgMade.place(x=5 + xCoordinate, y=310 + yCoordinate, height=50, width=75)

        #field goal missed
        fgMissed = Button(root, text='FG Missed',
                                  command=lambda pointCounter=pointCounter: fieldGoalAttempt(pointCounter)
                                  , bg="white", fg="black", highlightbackground="gray90", borderwidth=2,
                                  relief="raised", activebackground="deep sky blue")
        fgAttempt_Array.append(fgMissed)
        fgMissed.place(x=80 + xCoordinate, y=310 + yCoordinate, height=50, width=75)

        #three point made
        threePointFGMadeButton = Button(root, text='3PT Made',
                                  command=lambda pointCounter=pointCounter:[fieldGoalShot(pointCounter),fieldGoalAttempt(pointCounter), threePointerMade(pointCounter),
                                      threePointerScored(pointCounter), threePointerAttempted(pointCounter)]

                                  , bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",activebackground="deep sky blue")
        threePointMade_Array.append(threePointFGMadeButton)
        threePointFGMadeButton.place(x=5 + xCoordinate, y=360 + yCoordinate, height=50, width=75)

        #three point missed
        threePointMissed = Button(root, text='3PT Missed', command=lambda pointCounter=pointCounter:[threePointerAttempted(pointCounter),fieldGoalAttempt(pointCounter)], bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",activebackground="deep sky blue")
        threePointAttempt_Array.append(threePointMissed)
        threePointMissed.place(x=80 + xCoordinate, y=360 + yCoordinate, height=50, width=75)

        #free throw made
        freeThrowLabel = Label(root, text="FT %: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1,
                           relief="raised").place(x=5 + xCoordinate, y=280 + yCoordinate, height=30, width=55)

        freeThrowFGMade = Button(root, text='FT Made', command=lambda pointCounter=pointCounter: [freeThrowMake(pointCounter), freeThrowMiss(pointCounter)], bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",activebackground="deep sky blue")
        freeThrowMade_Array.append(freeThrowFGMade)
        freeThrowFGMade.place(x=5 + xCoordinate, y=410 + yCoordinate, height=50, width=75)

        ftMadeBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        freeThrowMade.append(ftMadeBox)
        freeThrowMade[j].insert(0, 0)
        ftMadeBox.place(x=60 + xCoordinate, y=280 + yCoordinate, height=30, width=47)

        #free throw missed
        ftBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        freeThrowMissed.append(ftBox)
        freeThrowMissed[j].insert(0, 0)
        ftBox.place(x=107.5 + xCoordinate, y=280 + yCoordinate, height=30, width=47)

        freeThrowFGMissed = Button(root, text='FT Missed',
                                 command=lambda pointCounter=pointCounter: freeThrowMiss(pointCounter), bg="white",
                                 fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",
                                 activebackground="deep sky blue")
        freeThrowMissed_Array.append(freeThrowFGMissed)
        freeThrowFGMissed.place(x=80 + xCoordinate, y=410 + yCoordinate, height=50, width=75)

        #field goal Percentage
        fgLabel = Label(root, text="FG %: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=220 + yCoordinate, height=30, width=55)
        fgBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        fgShot.append(fgBox)
        fgShot[j].insert(0, 0)
        fgBox.place(x=60 + xCoordinate, y=220 + yCoordinate, height=30, width=47.5)

        fgAttemptBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        fgAttempt.append(fgAttemptBox)
        fgAttempt[j].insert(0, 0)
        fgAttemptBox.place(x=107.5 + xCoordinate, y=220 + yCoordinate, height=30, width=47)

        #three point percentage
        threePointPercentage = Label(root, text="3PT %: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=250 + yCoordinate, height=30, width=55)
        threePointAttemptBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        threePointAttempt.append(threePointAttemptBox)
        threePointAttempt[j].insert(0, 0)
        threePointAttemptBox.place(x=107.5 + xCoordinate, y=250 + yCoordinate, height=30, width=47)

        threePointMadeBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        threePointScored.append(threePointMadeBox)
        threePointScored[j].insert(0, 0)
        threePointMadeBox.place(x=60 + xCoordinate, y=250 + yCoordinate, height=30, width=47)

        #bearkats box
        Label(root, text="Bearkats", bg="white", fg="black", borderwidth=1, relief="raised").place(x=730, y=15, height=30, width=150)
        Label(root, text="Visitor", bg="white", fg="black", borderwidth=1, relief="raised").place(x=730, y=45, height=30, width=150)
        bearkatScore = Entry(root,bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="solid")
        bearkatScore.place(x=880, y=15, height=30, width=150)

        #visitor box
        visitorBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        visitorScore.append(visitorBox)
        visitorScore[j].insert(0, 0)
        visitorBox.place(x=880, y = 45, height=30, width=150)

        visitorAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: visitorScores(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        visitorScore_Array.append(visitorAddition)
        visitorAddition.place(x = 1030, y = 45, height=30, width=30)
        pointCounter += 1

def saveToFile():
    fileToSaveTo = open('Game.csv', "w")
    for i in range(playerCount):
        tempPoints = points[i].get()
        tempAssist = assists[i].get()
        tempRebound = rebounds[i].get()
        tempSteal = steals[i].get()
        tempBlock = blocks[i].get()
        tempFouls = fouls[i].get()
        tempFgMade = fgShot[i].get()
        tempFgMissed = fgAttempt[i].get()
        tempThreePointMade = threePointScored[i].get()
        tempThreePointMissed = threePointAttempt[i].get()
        tempFreeThrowMade = freeThrowMade[i].get()
        tempFreeThrowMissed = freeThrowMissed[i].get()
        str_tempPoints = str(tempPoints) + " Points, "
        str_tempAssist = str(tempAssist) + " Assists, "
        str_tempRebound = str(tempRebound) + " Rebounds, "
        str_tempSteal = str(tempSteal) + " Steals, "
        str_tempBlock = str(tempBlock) + " Blocks, "
        str_tempFgMade = "FGs: " + str(tempFgMade) + "/"
        str_tempFgMissed = str(tempFgMissed) + ", "
        str_tempThreePointMade = "3PTs: " + str(tempThreePointMade) + "/"
        str_tempThreePointMissed = str(tempThreePointMissed) + ", "
        str_tempFreeThrowMade = "FTs: " + str(tempFreeThrowMade) + "/"
        str_tempFreeThrowMissed = str(tempFreeThrowMissed) + ", "
        str_tempFouls = str(tempFouls) + " Fouls \n"
        playerStats = playerList[i] + ": " + str_tempPoints + str_tempAssist + str_tempRebound + str_tempSteal \
                      + str_tempBlock + str_tempFgMade + str_tempFgMissed + str_tempThreePointMade \
                      + str_tempThreePointMissed + str_tempFreeThrowMade + str_tempFreeThrowMissed + str_tempFouls
        fileToSaveTo.writelines(playerStats)

    fileToSaveTo.close()

saveData = Button(text="Export", bg="white", fg="black", command=saveToFile, highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x=10, y=10, height=30, width=150)


mainWindow()

mainloop()