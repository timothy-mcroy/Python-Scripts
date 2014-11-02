"""
Created by Timothy McRoy
This program is designed for use with the New World of Darkness game system.
"""



import random, sys, time
if sys.version_info.major is 2:
    from Tkinter import *
if sys.version_info.major is 3:
    from tkinter import *
class DieFrame(Frame):
    """
    This class creates a dice roller specifically for New World of Darkness.
    Everything could look prettier, the formatting could be better, but it's still much faster than rolling 120 dice and counting up the hits.
    """
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.Frame1= Frame(self)
        #label entry bar
        self.EntryLabel = Label (self.Frame1, text="Die Pool")
        self.EntryLabel.grid(row=0, column=0, sticky = W)
        #Create an entry bar for the Die Pool
        self.DiePool = IntVar()                   
        self.DiePool1 = Entry(self.Frame1, textvariable = self.DiePool)
        self.DiePool1.grid(row=0, column=1, sticky = W)

        #Rote action checkbox
        self.Rote = IntVar()
        self.RoteCheck = Checkbutton(self.Frame1, text = "Rote action", variable = self.Rote)
        self.RoteCheck.grid(row=2,column = 0, sticky = W)

        #Create a Scale widget for _ Again
        self.AgainScale = IntVar()
        self.AgainScale1 = Scale(self.Frame1, label= "___ Agains", from_ = 8, to = 11, variable = self.AgainScale, tickinterval = 1, orient= HORIZONTAL)
        self.AgainScale1.grid(row=4, column=0, sticky = W+E,columnspan = 2)

        #Checkbox for timestamp
        self.Timestamp = IntVar()
        self.TimestampCheckbox = Checkbutton(self.Frame1, text= "Timestamp", variable = self.Timestamp)
        self.TimestampCheckbox.grid(row =5,column =0, sticky = W)

        #Option for Character name
        self.NameLabel = Label(self.Frame1, text = "Character name")
        self.NameLabel.grid(row=6, column=0, sticky = W)
        
        self.CharName = StringVar()
        self.NameEntry = Entry(self.Frame1, textvariable = self.CharName)
        self.NameEntry.grid(row=6, column=1, sticky = E)

        #Roll Description
        self.RollDescLabel = Label(self.Frame1, text = "Roll Description")
        self.RollDescLabel.grid(row= 7, column = 0, sticky = W)
        self.RollDesc = StringVar()
        self.RollDescEntry = Entry(self.Frame1, textvariable = self.RollDesc)
        self.RollDescEntry.grid(row=7, column = 1, sticky = E)
        
        #Button that rolls dice
        self.RollIt = Button(self.Frame1, text = "Roll", command = self.RollDice)
        self.RollIt.grid(row = 8, column = 0, sticky = W+E)

        #Place the first frame
        self.Frame1.grid(row=0,columnspan=2, sticky = W)
        
        #Create a record of all rolls made
        self.Frame2 = Frame(self)
        self.scrollbar = Scrollbar(self.Frame2)
        self.scrollbar.pack( side = RIGHT, fill=Y )
        self.DiceLog = Text( self.Frame2, yscrollcommand = self.scrollbar.set)
        self.DiceLog.pack(side = RIGHT)
        self.Frame2.grid(row=0, column = 2, sticky =E)
    def RollDice(self):
        Rote=self.Rote.get()
        DiePool=self.DiePool.get()
        Agains = self.AgainScale.get()
        CharName = self.CharName.get()
        RollDesc = self.RollDesc.get()
        g        = ''               #String Accumulator
        if self.Timestamp.get() == 1:
            g = str(time.strftime("%I:%M:%S %p", time.localtime()))
        Accum = 0
        y=[]
        rerolled=0
        while (DiePool>0):
            a     =[ int(random.random()*10+1) for i in range(DiePool)]  #a represents the "live dice", dice that are being rolled
            y    += a  #Players like to know exactly what their die result was.  (whether they were close, whether the rote action helped, etc).
                       #We can keep track of everything, including rote actions, with y as an accumulator
            if Rote==1:  #If the box is checked
                Rote = 0
                hits = sum([1 for i in y if i >=8])  # Any roll greater than 8 is a hit, as per the rules
                self.DiceLog.insert(1.0, '\n' + str(DiePool-hits) + " extra dice from rote action")
                y+= [ int(random.random()*10+1) for i in range(DiePool-hits)]  
            hits = sum([1 for i in a if i >=8]) #New world of Darkness has a standard 8 difficulty
            DiePool = sum([1 for i in a if i>=Agains])  # When something is "Again", it gets to be added to the count and that many dice are rolled again.
            rerolled +=DiePool
            Accum+=hits
        if Accum == 0:
            self.DiceLog.insert(1.0, "\n\n" +g+" - " +CharName+" - "+ RollDesc+ "  "+g+'\n' + 'This roll was a failure' + "\n" +str(sorted(y)))
            return
        else:
            
            if (rerolled==0):  #Custom output indicating the strength of a roll.
                self.DiceLog.insert( 1.0,'\n' +"No extra dice from explosions.  Your dice hate you." )
            elif (rerolled< (self.DiePool.get())/2):  # We want the original die pool for this comparison.  
                self.DiceLog.insert( 1.0,'\n' +str(rerolled)+" extra dice from explosions." )
            else:
                self.DiceLog.insert( 1.0,'\n' +str(rerolled)+" extra dice from explosions!" )
            self.DiceLog.insert( 1.0,"\n\n" +g+" - " +CharName+" - "+ RollDesc+"  "+'\n' + str(Accum) + " hits with "+str(Agains)+" agains with a dice pool of "+str(self.DiePool.get()) +"\n" + str( sorted(y)) + '\n' )                      
            return



g=DieFrame()
g.master.title("New World of Darkness Dice Roller")
g.mainloop()



















            
        
        
        
