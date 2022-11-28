import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
import matplotlib.pyplot as plt
import math
import itertools
from random import randint
import time
import numpy as np




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
        self.angleOption = tk.IntVar(self)
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
        angleSlider = tk.Scale(self,from_=90,to=10,orient='vertical',variable=self.angleOption)
        angleSlider.grid(column=0,row=3,sticky=tk.W,**paddings)
        angleSliderLabel = ttk.Label(self,text='Set angle in degrees')
        angleSliderLabel.grid(column=0,row=4,sticky=tk.W,**paddings)
        rocketSet = ttk.Button(self,text='Create rocket',command=self.rocketCreate)
        rocketSet.grid(column=4,row=2,sticky=tk.W,**paddings)
        self.rocketsetLabel = ttk.Label(self,foreground='red')
        self.rocketsetLabel.grid(column=0,row=3,sticky=tk.W,**paddings)
        

    def thrustSelect(self,*args):
        self.thrusterWeight = 0
        self.thrusterPower = 0
        if self.thrusterOption.get() == 'Small':
            self.thrusterPower += 1
            self.thrusterWeight += 1
        elif self.thrusterOption.get() == 'Medium':
            self.thrusterPower += 3
            self.thrusterWeight += 3
        elif self.thrusterOption.get() == 'Large':
            self.thrusterPower += 5
            self.thrusterWeight += 7
        else:
            pass
    def fuelTankSelect(self,*args):
        self.fuelTankPower = 0
        self.fuelTankWeight = 0
        self.fuelLevels = 0
        if self.fuelTankOption.get() == 'Small':
            self.fuelLevels += 1
            self.fuelTankPower += 1
            self.fuelTankWeight += 3
        elif self.fuelTankOption.get() == 'Medium':
            self.fuelLevels += 3
            self.fuelTankPower += 2
            self.fuelTankWeight += 6
        elif self.fuelTankOption.get() == 'Large':
            self.fuelLevels += 6
            self.fuelTankPower += 4
            self.fuelTankWeight += 8
        else:
            pass
    def passangerSelect(self,*args):
        self.passangerWeight = 0
        if self.passangerOption.get() == 1:
            self.passangerWeight += 1
        elif self.passangerOption.get() == 2:
            self.passangerWeight += 2
        elif self.passangerOption.get() == 3:
            self.passangerWeight += 3
        elif self.passangerOption.get() == 4:
            self.passangerWeight += 4
        else:
            pass


    def coneSelect(self,*args):
        self.conePower = 0
        self.coneWeight = 0
        if self.coneOption.get() == 'Pointed':
            self.conePower = self.conePower + 2
            self.coneWeight =self.coneWeight + 1
        elif self.coneOption.get() == 'Sloped':
            self.conePower = self.conePower + 3
            self.coneWeight = self.coneWeight + 2
        elif self.coneOption.get() == 'Barrel':
            self.conePower = self.conePower + 4
            self.coneWeight = self.coneWeight + 3
        else:
            pass
    
    def rocketCreate(self,*args):
        self.totalWeight = self.thrusterWeight+ self.fuelTankWeight + self.passangerWeight + self.coneWeight
        self.totalPower = self.thrusterPower+ self.fuelTankPower + self.conePower
        self.wetMass = self.fuelLevels 
        self.dryMass = self.totalWeight - self.wetMass
        self.rocketPower = self.totalPower * self.fuelLevels
        self.totalBurn = self.rocketPower - self.totalWeight
        self.rocketsetLabel['text']=f'The total weight is: {self.totalWeight} and the total power is: {self.totalPower}'

if __name__=="__main__":
    app = Menu()
    app.mainloop()
    totalMass = app.totalWeight
    propellantMass = app.wetMass
    totalDryMass = app.dryMass
    burnTime = 3.4
    totalImpulse = app.rocketPower
    averageThrust = totalImpulse/burnTime
    massFlowRate = propellantMass/burnTime
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111,projection = '3d')

    time = np.linspace(0, 10, 100, False)
    print(time)
    # index = int(np.where(time==burnTime)[0] + 1)
    # thrust = np.append(np.repeat(averageThrust, index), np.repeat(0,len(time)-index))
    # mass = np.append(np.repeat(totalMass, index) - time[0:index] * massFlowRate, np.repeat(totalDryMass,len(time)-index))
    # acceleration = thrust/mass - 9.81
    # plt.style.use('dark_background')
    # plt.plot(time,acceleration)
    # plt.ylabel("Acceleration")
    # plt.xlabel("Time")
    # plt.show()
