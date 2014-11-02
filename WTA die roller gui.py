import random, sys, time
if sys.version_info.major is 2:
    from Tkinter import *
if sys.version_info.major is 3:
    from tkinter import *
class DieFrame(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.Frame1= Frame(self)
        #label entry bar
        self.EntryLabel = Label (self.Frame1, text="Die Pool")
        self.EntryLabel.grid(row=0, column=0, sticky = W)
        #Create an entry bar
        self.v = IntVar()
        self.DiePool = Entry(self.Frame1, textvariable = self.v)
        
        self.DiePool.grid(row=0, column=1, sticky = W)
        #Specialty checkbox
        self.Spec = IntVar()
        self.SpecCheck = Checkbutton(self.Frame1, text = "Specialty", variable = self.Spec)
        self.SpecCheck.grid(row=1, column=0, sticky = W)
        #Willpower checkbox
        self.WP = IntVar()
        self.WPCheck = Checkbutton(self.Frame1, text = "Willpower", variable = self.WP)
        self.WPCheck.grid(row=2,column = 0, sticky = W)
        #Damage Roll checkbox
        self.Dmg = IntVar()
        self.DmgCheck = Checkbutton(self.Frame1, text = "Damage Roll", variable = self.Dmg)
        self.DmgCheck.grid(row=3, column=0, sticky = W)
        #Create a Scale widget for difficulty
        self.sb = IntVar()
        self.DCscale = Scale(self.Frame1, label= "Difficulty", from_ = 2, to = 10, variable = self.sb, tickinterval = 1, orient= HORIZONTAL)
        self.DCscale.grid(row=4, column=0, sticky = W+E,columnspan = 2)
        #Die Result Label
        #self.DieResultLabel =Label(self.Frame1, text = "Die result:")
        #self.DieResultLabel.grid(row=6, column=1, sticky = E)

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
        #create a button that rolls the dice
        self.RollIt = Button(self.Frame1, text = "Roll", command = self.RollDice)
        self.RollIt.grid(row = 8, column = 0, sticky = W+E)

        #Place the first frame.
        self.Frame1.grid(row=0,columnspan=2, sticky = W)
        
        #Create a record of all rolls made
        self.Frame2 = Frame(self)
        self.scrollbar = Scrollbar(self.Frame2)
        self.scrollbar.pack( side = RIGHT, fill=Y )
        self.DiceLog = Text( self.Frame2, yscrollcommand = self.scrollbar.set)
        self.DiceLog.pack(side = RIGHT)
        self.Frame2.grid(row=0, column = 2, sticky =E)
        

    def RollDice(self):
        Willpower = self.WP.get()
        DiePool=self.v.get()
        Difficulty=self.sb.get()
        Specialization = self.Spec.get()
        DamageRoll= self.Dmg.get()
        CharName= self.CharName.get()
        RollDesc = self.RollDesc.get()
        g=''
        if self.Timestamp.get() == 1:
            g = str(time.strftime("%I:%M:%S %p", time.localtime()))
        
        y= [ int(random.random()*10+1) for i in range(DiePool)]
        z = sum([1 for i in y if i >=Difficulty]) + Willpower
        if Specialization == 1:
            z+= sum([1 for i in y if i == 10])
        if DamageRoll == 0:
            Minuses = sum([1 for i in y if i == 1])
        if DamageRoll == 1:
            self.DiceLog.insert(1.0, '\n' +CharName+' '+ RollDesc+ "  "+g+'\n' +str(z) + ' hits at difficulty ' + str(Difficulty)+'\n' + '   ' + str(sorted(y)) )
            return
        if z == 0 and Minuses >0:
            self.DiceLog.insert(1.0, '\n' +CharName+' '+ RollDesc+ "  "+g+'\n' + 'This roll was a botch' + "\n" +str(sorted(y)))
            return
        self.DiceLog.insert( 1.0,'\n' +CharName+' '+ RollDesc+"  "+g+'\n' + str(z-Minuses) + " hits at difficulty " +str(Difficulty) +"\n" + str( sorted(y))   )
        return
g=DieFrame()
g.master.title("Werewolf Dice Roller")
g.mainloop()
        
        


