import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
import matplotlib.pyplot as plt
import math
import itertools
from random import *
import time

global unitCount

##creating class object for the menu##
class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("720x540")
        self.title('Battle Sim')
        self.armySelector = ['Red','Blue','Green']
        self.unitSelector = ('Foot solider','Pilot','Engineer')
        self.vehicleSelector = ('Airplane','Jeep','Tank')
        self.armyOptionSelected = tk.StringVar(self)
        self.unitOptionSelected = tk.StringVar(self)
        self.vehcileOptionSelected = tk.StringVar(self)
        self.secoundVehcileOptionSelected = tk.StringVar(self)
        self.thirdVehcileOptionSelected = tk.StringVar(self)
        
        self.secoundUnitOptionSelected = tk.StringVar(self)
        self.thirdUnitOptionSelected = tk.StringVar(self)
        self.optionSelected = IntVar(self)
        self.createWidgets()
        

    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        self.unitCount = 0
        self.vehicleCount = 0 
        label = ttk.Label(self, text = 'Select an army to create building:')
        label.grid(column=0,row=0,sticky=tk.W,**paddings)
        armyCompSelect = Radiobutton(self,text ='Ground units',variable = self.optionSelected,value=1,command=self.unitsAdd)
        armyCompSelect.grid(column=2,row=0,sticky=tk.W,**paddings)
        armyCompSelectVehicle = Radiobutton(self,text='Vehicles',variable = self.optionSelected,value=2,command=self.unitsAdd)
        armyCompSelectVehicle.grid(column=3,row=0,sticky=tk.W,**paddings)
        armyColorSelectorMenu = ttk.OptionMenu(self,self.armyOptionSelected,self.armySelector[0],*self.armySelector,command = self.optionChanged)
        armyColorSelectorMenu.grid(column = 1, row = 0, sticky=tk.W, **paddings)
        self.outputLabel = ttk.Label(self)
        self.outputLabel.grid(column=0,row=1,sticky=tk.W)
        # unitGenerator = ttk.Button(self,text='Click to add ground units',command=self.unitNum)
        # unitGenerator.grid(column=0,row=9,sticky=tk.W,**paddings)

    def unitNum(self,*args):
        self.unitCount = self.unitCount + 1
        if self.unitCount == 1:
            self.firstGroundLabel = ttk.Label(self,text='First squad of ground units:')
            self.firstGroundLabel.grid(column=0,row=2, sticky=tk.W)
            self.firstGroundUnits = ttk.OptionMenu(self,self.unitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.firstGroundUnits.grid(column=1,row=2,sticky=tk.W)
        if self.unitCount == 2:
            self.secondGroundLabel = ttk.Label(self,text='Second squad of ground units:')
            self.secondGroundLabel.grid(column=0,row=3,sticky=tk.W)
            self.secondGroundUnits = ttk.OptionMenu(self,self.secoundUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.secondGroundUnits.grid(column=1,row=3,sticky=tk.W)
        elif self.unitCount == 3:
            self.thirdGroundLabel = ttk.Label(self,text='Third squad of ground units:')
            self.thirdGroundLabel.grid(column=0,row=4,sticky=tk.W)
            self.thirdGroundUnits = ttk.OptionMenu(self,self.thirdUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.thirdGroundUnits.grid(column=1,row=4,sticky=tk.W)


    def unitsAdd(self,*args):
        if self.optionSelected.get() == 1:
            if self.vehicleCount > 1:
                self.firstVehicleUnits.destroy()
                self.firstVehicleLabel.destroy()
                self.secondVehicleUnits.destroy()
                self.secondVehicleLabel.destroy()
                self.thirdVehicleUnits.destroy()
                self.thirdVehicleLabel.destroy()
                self.vehicleGenerator.destroy()
                self.vehicleCount = 0
            self.unitGenerator = ttk.Button(self,text='Click to add ground units',command=self.unitNum)
            self.unitGenerator.grid(column=0,row=5,sticky=tk.W)
        elif self.optionSelected.get() == 2:
            if self.unitCount > 1:
                self.firstGroundUnits.destroy()
                self.firstGroundLabel.destroy()
                self.secondGroundUnits.destroy()
                self.secondGroundLabel.destroy()
                self.thirdGroundUnits.destroy()
                self.thirdGroundLabel.destroy()
                self.unitGenerator.destroy()
                self.unitCount = 0
            self.vehicleGenerator = ttk.Button(self,text='Click to add vehicle  units',command=self.vehicleNum)
            self.vehicleGenerator.grid(column=2,row=5,sticky=tk.W)


    def optionChanged(self,*args):
        self.outputLabel['text']=f'You selected: {self.armyOptionSelected.get()}'
        self.outputLabel['foreground']=f'{self.armyOptionSelected.get()}'
    def vehicleNum(self,*args):
        self.vehicleCount = self.vehicleCount + 1
        if self.vehicleCount == 1:
            self.firstVehicleLabel = ttk.Label(self,text='First squad of vehicle units:')
            self.firstVehicleLabel.grid(column=2,row=2, sticky=tk.W)
            self.firstVehicleUnits = ttk.OptionMenu(self,self.vehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.firstVehicleUnits.grid(column=3,row=2,sticky=tk.W)
        elif self.vehicleCount == 2:
            self.secondVehicleLabel = ttk.Label(self,text='Second squad of vehicle units:')
            self.secondVehicleLabel.grid(column=2,row=3,sticky=tk.W)
            self.secondVehicleUnits = ttk.OptionMenu(self,self.secoundVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.secondVehicleUnits.grid(column=3,row=3,sticky=tk.W)
        elif self.vehicleCount == 3:
            self.thirdVehicleLabel = ttk.Label(self,text='Third squad of vehicle units:')
            self.thirdVehicleLabel.grid(column=2,row=4,sticky=tk.W)
            self.thirdVehicleUnits = ttk.OptionMenu(self,self.thirdVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.thirdVehicleUnits.grid(column=3,row=4,sticky=tk.W)
        

if __name__=="__main__":
    application = Menu()
    application.mainloop()
