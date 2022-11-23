import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
import matplotlib.pyplot as plt
import math
import itertools
from random import randint
import time




class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("680x320")
        self.title('Rocket tester')

        self.thrusterSelector=('Small','Medium','Large')
        self.thrusterOption = tk.StringVar(self)
        self.fuelTankSelector=('Small','Medium','Large')
        self.fuelTankOption = tk.StringVar(self)
        self.passangerSelector=(1,2,3,4)
        self.passangerOption = tk.IntVar(self)
        self.coneSelector=('Pointed','Sloped','Barrel')
        self.coneOption = tk.StringVar(self)
        self.townLocation = tk.IntVar(self)
        self.coneWeight = 0
        self.fuelTankWeight = 0
        self.thrusterWeight = 0
        self.passangerWeight = 0
        self.conePower = 0
        self.fuelTankPower = 0
        self.thrusterPower = 0
        self.passangerPower = 0
        global totalWeight 
        totalWeight = 0
        global totalPower
        totalPower = 0
        self.createWidgets()

    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        label = ttk.Label(self,text = 'Choose the pieces of the rocket:')
        label.grid(column=0,row=0,sticky=tk.W,**paddings)
        thrusterLabel = ttk.Label(self,text ='Thruster size:')
        thrusterLabel.grid(column=0,row=1,sticky=tk.W,**paddings)
        thrusterGenerate = ttk.OptionMenu(self,self.thrusterOption,self.thrusterSelector[0],*self.thrusterSelector,command = self.thrustSelect)
        thrusterGenerate.grid(column=0,row=2,sticky=tk.W,**paddings)
        fuelTankLabel = ttk.Label(self,text='Fuel tank size:')
        fuelTankLabel.grid(column=1,row=1,sticky=tk.W,**paddings)
        fuelTankGenerate = ttk.OptionMenu(self,self.fuelTankOption,self.fuelTankSelector[0],*self.fuelTankSelector,command=self.fuelTankSelect)
        fuelTankGenerate.grid(column=1,row=2,sticky=tk.W,**paddings)
        passangerLabel = ttk.Label(self,text ='Number of Passengers:')
        passangerLabel.grid(column=2,row=1,sticky=tk.W,**paddings)
        passangerGenerate = ttk.OptionMenu(self,self.passangerOption,self.passangerSelector[0],*self.passangerSelector,command=self.passangerSelect)
        passangerGenerate.grid(column=2,row=2,sticky=tk.W,**paddings)
        coneLabel = ttk.Label(self,text='Cone shape:')
        coneLabel.grid(column=3,row=1,sticky=tk.W,**paddings)
        coneGenerate = ttk.OptionMenu(self,self.coneOption,self.coneSelector[0],*self.coneSelector,command=self.coneSelect)
        coneGenerate.grid(column=3,row=2,sticky=tk.W,**paddings)

        rocketSet = ttk.Button(self,text='Create rocket',command=self.rocketCreate)
        rocketSet.grid(column=4,row=2,sticky=tk.W,**paddings)
        self.rocketsetLabel = ttk.Label(self,foreground='red')
        self.rocketsetLabel.grid(column=0,row=3,sticky=tk.W,**paddings)
        

    def rocketCreate(self,*args):
        totalWeight = self.thrusterWeight+ self.fuelTankWeight + self.passangerWeight + self.coneWeight
        totalPower = self.thrusterPower+ self.fuelTankPower + self.conePower
        self.rocketsetLabel['text']=f'The total weight is: {totalWeight} and the total power is: {totalPower}'

    def thrustSelect(self,*args):
        if self.thrusterOption == 'Small':
            global thrusterPower 
            thrusterPower = 1
            global thrusterWeight
            thrusterWeight = 1
        elif self.thrusterOption == 'Medium':
            self.thrusterPower = 3
            self.thrusterWeight = 3
        elif self.thrusterOption == 'Large':
            self.thrusterPower = 5
            self.thrusterWeight = 7
        else:
            pass
    def fuelTankSelect(self,*args):
        if self.fuelTankOption == 'Small':
            self.fuelTankPower = 1
            self.fuelTankWeight = 3
        elif self.fuelTankOption == 'Medium':
            self.fuelTankPower = 2
            self.fuelTankWeight = 6
        elif self.fuelTankOption == 'Large':
            self.fuelTankPower = 4
            self.fuelTankWeight = 8
        else:
            pass
    def passangerSelect(self,*args):
        if self.passangerOption == 1:
            self.passangerWeight = 1
        elif self.passangerOption == 2:
            self.passangerWeight = 2
        elif self.passangerOption == 3:
            self.passangerWeight = 3
        elif self.passangerOption == 4:
            self.passangerWeight = 4
        else:
            pass


    def coneSelect(self,*args):
        if self.coneOption == 'Pointed':
            self.conePower = 2
            self.coneWeight =1
        elif self.coneOption == 'Sloped':
            self.conePower = 3
            self.coneWeight = 2
        elif self.coneOption == 'Barrel':
            self.conePower = 4
            self.coneWeight = 3
        else:
            pass

if __name__=="__main__":
    app = Menu()
    app.mainloop()
