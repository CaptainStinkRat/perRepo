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

        self.vehicleSquadNum = [10,20,30,40]
    
        self.vehicleSquadOneNumSelect = IntVar(self)
        self.vehicleSquadTwoNumSelect = IntVar(self)
        self.vehicleSquadThreeNumSelect = IntVar(self)
        self.vehicleSquadFourNumSelect = IntVar(self)
        self.vehicleSquadFifthNumSelect = IntVar(self)
        
        self.groundUnitSquadNum = [10,20,30,40]

        self.groundUnitSquadOneNumSelect = IntVar(self)
        self.groundUnitSquadTwoNumSelect = IntVar(self)
        self.groundUnitSquadThreeNumSelect = IntVar(self)
        self.groundUnitSquadFourNumSelect = IntVar(self)
        self.groundUnitSquadFifthNumSelect = IntVar(self)

        self.armyOptionSelected = tk.StringVar(self)
        self.unitOptionSelected = tk.StringVar(self)
        self.vehcileOptionSelected = tk.StringVar(self)
        self.secoundVehcileOptionSelected = tk.StringVar(self)
        self.thirdVehcileOptionSelected = tk.StringVar(self)
        self.groundSquad = tk.IntVar(self)
        self.secoundUnitOptionSelected = tk.StringVar(self)
        self.thirdUnitOptionSelected = tk.StringVar(self)
        self.optionSelected = IntVar(self)
        self.unitCount = 0
        self.vehicleCount = 0
        self.vehicleSquad = tk.IntVar(self)
        self.fourthVehcileOptionSelected = StringVar(self)
        self.fifthVehcileOptionSelected = StringVar(self)
        self.fourthUnitOptionSelected = StringVar(self)
        self.fifthUnitOptionSelected = StringVar(self)
        self.createWidgets()
        

    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        # self.unitCount = 0
        # self.vehicleCount = 0
        self.armyBuilderLabelFrame = ttk.LabelFrame(self,text='Army')
        self.armyBuilderLabelFrame.grid(column=0,row=0,padx=20,pady=20)
        label = ttk.Label(self.armyBuilderLabelFrame, text = 'Select an army to start building:')
        label.grid(column=0,row=0,**paddings)
        self.unitSelectorLF = ttk.LabelFrame(self, text = 'Unit selection')
        self.unitSelectorLF.grid(column=2,row=0,padx = 30,pady=30)
        self.armyCompSelect = Radiobutton(self.unitSelectorLF,text ='Ground units',variable = self.optionSelected,value=1,command=self.unitsAdd)
        self.armyCompSelect.grid(column=2,row=0,ipadx=10,ipady=10)
        self.armyCompSelectVehicle = Radiobutton(self.unitSelectorLF,text='Vehicles',variable = self.optionSelected,value=2,command=self.unitsAdd)
        self.armyCompSelectVehicle.grid(column=3,row=0,ipadx=10,ipady=10)
        self.bothCompSelect = Radiobutton(self.unitSelectorLF,text = 'Both',variable = self.optionSelected, value = 3, command=self.unitsAdd)
        self.bothCompSelect.grid(column=4, row=0,ipadx=10,ipady=10)
        armyColorSelectorMenu = ttk.OptionMenu(self.armyBuilderLabelFrame,self.armyOptionSelected,self.armySelector[0],*self.armySelector,command = self.optionChanged)
        armyColorSelectorMenu.grid(column = 1, row = 0, ipadx=10,ipady=10)
        self.outputLabel = ttk.Label(self)
        self.outputLabel.grid(column=0,row=1,sticky=tk.W)
        # unitGenerator = ttk.Button(self,text='Click to add ground units',command=self.unitNum)
        # unitGenerator.grid(column=0,row=9,sticky=tk.W,**paddings)



    def unitsAdd(self,*args):
        if self.optionSelected.get() == 1:
            self.groundUnitLabelFrame = ttk.LabelFrame(self,text='Number of squads of ground units:')
            self.groundUnitLabelFrame.grid(column=0,row=1,padx=30,pady=30)
            self.groundSquadSelect = tk.Scale(self.groundUnitLabelFrame, from_=1, to=5,orient='horizontal',variable=self.groundSquad)
            self.groundSquadSelect.grid(column=0,row=1,ipadx=10,ipady=10)
            self.groundSquadSet = ttk.Button(self.groundUnitLabelFrame,text = 'Set ground squad size',command=self.groundUnitCreate)
            self.groundSquadSet.grid(column=1,row=1,ipadx=10,ipady=10)
            self.armyCompSelect.configure(state='disabled')
            self.armyCompSelectVehicle.configure(state='disabled')
            self.bothCompSelect.configure(state='disabled')
            
        elif self.optionSelected.get() == 2:
            self.vehicleUnitLabelFrame = ttk.LabelFrame(self,text='Number of squads of vehicle units:')
            self.vehicleUnitLabelFrame.grid(column=0,row=1,padx=30,pady=30)
            self.vehicleSquadSelect = tk.Scale(self.vehicleUnitLabelFrame, from_=1, to=5,orient='horizontal',variable=self.vehicleSquad)
            self.vehicleSquadSelect.grid(column=0,row=1,ipadx=10,ipady=10)
            self.vehicleSquadSet = ttk.Button(self.vehicleUnitLabelFrame,text = 'Set vehicle squad size',command=self.vehicleCreate)
            self.vehicleSquadSet.grid(column=1,row=1,ipadx=10,ipady=10)
            self.armyCompSelect.configure(state='disabled')
            self.armyCompSelectVehicle.configure(state='disabled')
            self.bothCompSelect.configure(state='disabled')
            
        elif self.optionSelected.get() == 3:
        
            self.groundUnitLabelFrame = ttk.LabelFrame(self,text='Number of squads of ground units:')
            self.groundUnitLabelFrame.grid(column=0,row=1,padx=30,pady=30)
            self.groundSquadSelect = tk.Scale(self.groundUnitLabelFrame, from_=1, to=5,orient='horizontal',variable=self.groundSquad)
            self.groundSquadSelect.grid(column=0,row=1,ipadx=10,ipady=10)
            self.groundSquadSet = ttk.Button(self.groundUnitLabelFrame,text = 'Set ground squad size',command=self.groundUnitCreate)
            self.groundSquadSet.grid(column=1,row=1,ipadx=10,ipady=10)
            self.vehicleUnitLabelFrame = ttk.LabelFrame(self,text='Number of squads of vehicle units:')
            self.vehicleUnitLabelFrame.grid(column=0,row=2,padx=30,pady=30)
            self.vehicleSquadSelect = tk.Scale(self.vehicleUnitLabelFrame, from_=1, to=5,orient='horizontal',variable=self.vehicleSquad)
            self.vehicleSquadSelect.grid(column=0,row=2,ipadx=10,ipady=10)
            self.vehicleSquadSet = ttk.Button(self.vehicleUnitLabelFrame,text = 'Set vehicle squad size',command=self.vehicleCreate)
            self.vehicleSquadSet.grid(column=1,row=2,ipadx=10,ipady=10)
            self.armyCompSelect.configure(state='disabled')
            self.armyCompSelectVehicle.configure(state='disabled')
            self.bothCompSelect.configure(state='disabled')
    def optionChanged(self,*args):
        pass
        # self.outputLabel['text']=f'You selected: {self.armyOptionSelected.get()}'
        # self.outputLabel['foreground']=f'{self.armyOptionSelected.get()}'
        

    def vehicleCreate(self,*args):
        self.vehicleChoiceLabel = ttk.LabelFrame(self,text='Vehicle choices')
        self.vehicleChoiceLabel.grid(column=2,row=2,padx=30,pady=30)
        if self.vehicleSquad.get() == 1:

            self.firstVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='First squad of vehicle units:')
            self.firstVehicleLabel.grid(column=2,row=2, sticky=tk.W)
            self.firstVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.firstVehicleUnits.grid(column=3,row=2,sticky=tk.W)
            self.vehicleSquadSelect.configure(state="disabled")

            self.vehicleSquadOneNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadOneNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadOneNum.grid(column=4,row=2)
        elif self.vehicleSquad.get() == 2:
            self.firstVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='First squad of vehicle units:')
            self.firstVehicleLabel.grid(column=2,row=2, sticky=tk.W)
            self.firstVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.firstVehicleUnits.grid(column=3,row=2,sticky=tk.W)
            self.secondVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Second squad of vehicle units:')
            self.secondVehicleLabel.grid(column=2,row=3,sticky=tk.W)
            self.secondVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.secoundVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.secondVehicleUnits.grid(column=3,row=3,sticky=tk.W)
            self.vehicleSquadOneNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadOneNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadOneNum.grid(column=4,row=2)

            self.vehicleSquadTwoNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadTwoNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadTwoNum.grid(column=4,row=3)
            self.vehicleSquadSelect.configure(state="disabled")
        elif self.vehicleSquad.get() == 3:
            self.firstVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='First squad of vehicle units:')
            self.firstVehicleLabel.grid(column=2,row=2, sticky=tk.W)
            self.firstVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.firstVehicleUnits.grid(column=3,row=2,sticky=tk.W)
            self.secondVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Second squad of vehicle units:')
            self.secondVehicleLabel.grid(column=2,row=3,sticky=tk.W)
            self.secondVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.secoundVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.secondVehicleUnits.grid(column=3,row=3,sticky=tk.W)
            self.thirdVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Third squad of vehicle units:')
            self.thirdVehicleLabel.grid(column=2,row=4,sticky=tk.W)
            self.thirdVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.thirdVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.thirdVehicleUnits.grid(column=3,row=4,sticky=tk.W)

            self.vehicleSquadOneNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadOneNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadOneNum.grid(column=4,row=2)

            self.vehicleSquadTwoNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadTwoNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadTwoNum.grid(column=4,row=3)

            self.vehicleSquadThreeNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadThreeNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadThreeNum.grid(column=4,row=4)            

            self.vehicleSquadSelect.configure(state="disabled")
        elif self.vehicleSquad.get() == 4:
            self.firstVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='First squad of vehicle units:')
            self.firstVehicleLabel.grid(column=2,row=2, sticky=tk.W)
            self.firstVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.firstVehicleUnits.grid(column=3,row=2,sticky=tk.W)
            self.secondVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Second squad of vehicle units:')
            self.secondVehicleLabel.grid(column=2,row=3,sticky=tk.W)
            self.secondVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.secoundVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.secondVehicleUnits.grid(column=3,row=3,sticky=tk.W)
            self.thirdVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Third squad of vehicle units:')
            self.thirdVehicleLabel.grid(column=2,row=4,sticky=tk.W)
            self.thirdVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.thirdVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.thirdVehicleUnits.grid(column=3,row=4,sticky=tk.W)
            self.fourthVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Fourth squad of vehicle units:')
            self.fourthVehicleLabel.grid(column=2,row=5,sticky=tk.W)
            self.fourthVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.fourthVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.fourthVehicleUnits.grid(column=3,row=5,sticky=tk.W)

            self.vehicleSquadOneNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadOneNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadOneNum.grid(column=4,row=2)

            self.vehicleSquadTwoNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadTwoNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadTwoNum.grid(column=4,row=3)

            self.vehicleSquadThreeNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadThreeNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadThreeNum.grid(column=4,row=4) 

            self.vehicleSquadFourNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadFourNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadFourNum.grid(column=4,row=5)

            self.vehicleSquadSelect.configure(state="disabled")
        elif self.vehicleSquad.get() == 5:
            self.firstVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='First squad of vehicle units:')
            self.firstVehicleLabel.grid(column=2,row=2, sticky=tk.W)
            self.firstVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.firstVehicleUnits.grid(column=3,row=2,sticky=tk.W)
            self.secondVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Second squad of vehicle units:')
            self.secondVehicleLabel.grid(column=2,row=3,sticky=tk.W)
            self.secondVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.secoundVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.secondVehicleUnits.grid(column=3,row=3,sticky=tk.W)
            self.thirdVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Third squad of vehicle units:')
            self.thirdVehicleLabel.grid(column=2,row=4,sticky=tk.W)
            self.thirdVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.thirdVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.thirdVehicleUnits.grid(column=3,row=4,sticky=tk.W)
            self.fourthVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Fourth squad of vehicle units:')
            self.fourthVehicleLabel.grid(column=2,row=5,sticky=tk.W)
            self.fourthVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.fourthVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.fourthVehicleUnits.grid(column=3,row=5,sticky=tk.W)

            self.fifthVehicleLabel = ttk.Label(self.vehicleChoiceLabel,text='Fifth squad of vehicle units:')
            self.fifthVehicleLabel.grid(column=2,row=6,sticky=tk.W)
            self.fifthVehicleUnits = ttk.OptionMenu(self.vehicleChoiceLabel,self.fifthVehcileOptionSelected,self.vehicleSelector[0],*self.vehicleSelector)
            self.fifthVehicleUnits.grid(column=3,row=6,sticky=tk.W)

            self.vehicleSquadOneNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadOneNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadOneNum.grid(column=4,row=2)

            self.vehicleSquadTwoNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadTwoNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadTwoNum.grid(column=4,row=3)

            self.vehicleSquadThreeNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadThreeNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadThreeNum.grid(column=4,row=4) 

            self.vehicleSquadFourNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadFourNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadFourNum.grid(column=4,row=5)

            self.vehicleSquadFiveNum = ttk.OptionMenu(self.vehicleChoiceLabel,self.vehicleSquadFifthNumSelect,self.vehicleSquadNum[0],*self.vehicleSquadNum)
            self.vehicleSquadFiveNum.grid(column=4,row=6)

            self.vehicleSquadSelect.configure(state="disabled")


    def groundUnitCreate(self,*args):
        self.groundChoiceLabel = ttk.LabelFrame(self,text='Ground unit choices')
        self.groundChoiceLabel.grid(column=2,row=1,padx=30,pady=30)
        if self.groundSquad.get() == 1:
            self.firstGroundLabel = ttk.Label(self.groundChoiceLabel,text='First squad of ground units:')
            self.firstGroundLabel.grid(column=0,row=2, sticky=tk.W)
            self.firstGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.unitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.firstGroundUnits.grid(column=1,row=2,sticky=tk.W)
            self.firstGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadOneNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.firstGroundUnitNumSelect.grid(column=2,row=2,sticky=tk.W)
            self.groundSquadSelect.configure(state="disabled")
        if self.groundSquad.get() == 2:
            self.firstGroundLabel = ttk.Label(self.groundChoiceLabel,text='First squad of ground units:')
            self.firstGroundLabel.grid(column=0,row=2, sticky=tk.W)
            self.firstGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.unitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.firstGroundUnits.grid(column=1,row=2,sticky=tk.W)
            self.secondGroundLabel = ttk.Label(self.groundChoiceLabel,text='Second squad of ground units:')
            self.secondGroundLabel.grid(column=0,row=3,sticky=tk.W)
            self.secondGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.secoundUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.secondGroundUnits.grid(column=1,row=3,sticky=tk.W)
            self.firstGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadOneNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.firstGroundUnitNumSelect.grid(column=2,row=2,sticky=tk.W)
            self.secondGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadTwoNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.secondGroundUnitNumSelect.grid(column=2,row=3,sticky=tk.W)
            self.groundSquadSelect.configure(state="disabled")
        if self.groundSquad.get() == 3:
            self.firstGroundLabel = ttk.Label(self.groundChoiceLabel,text='First squad of ground units:')
            self.firstGroundLabel.grid(column=0,row=2, sticky=tk.W)
            self.firstGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.unitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.firstGroundUnits.grid(column=1,row=2,sticky=tk.W)
            self.secondGroundLabel = ttk.Label(self.groundChoiceLabel,text='Second squad of ground units:')
            self.secondGroundLabel.grid(column=0,row=3,sticky=tk.W)
            self.secondGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.secoundUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.secondGroundUnits.grid(column=1,row=3,sticky=tk.W)

            self.thirdGroundLabel = ttk.Label(self.groundChoiceLabel,text='Third squad of ground units:')
            self.thirdGroundLabel.grid(column=0,row=4,sticky=tk.W)
            self.thirdGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.thirdUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.thirdGroundUnits.grid(column=1,row=4,sticky=tk.W)
            self.firstGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadOneNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.firstGroundUnitNumSelect.grid(column=2,row=2,sticky=tk.W)
            self.secondGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadTwoNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.secondGroundUnitNumSelect.grid(column=2,row=3,sticky=tk.W)

            self.thirdGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadThreeNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.thirdGroundUnitNumSelect.grid(column=2,row=4,sticky=tk.W)
            self.groundSquadSelect.configure(state="disabled")
        if self.groundSquad.get() == 4:
            self.firstGroundLabel = ttk.Label(self.groundChoiceLabel,text='First squad of ground units:')
            self.firstGroundLabel.grid(column=0,row=2, sticky=tk.W)
            self.firstGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.unitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.firstGroundUnits.grid(column=1,row=2,sticky=tk.W)
            self.secondGroundLabel = ttk.Label(self.groundChoiceLabel,text='Second squad of ground units:')
            self.secondGroundLabel.grid(column=0,row=3,sticky=tk.W)
            self.secondGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.secoundUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.secondGroundUnits.grid(column=1,row=3,sticky=tk.W)

            self.thirdGroundLabel = ttk.Label(self.groundChoiceLabel,text='Third squad of ground units:')
            self.thirdGroundLabel.grid(column=0,row=4,sticky=tk.W)
            self.thirdGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.thirdUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.thirdGroundUnits.grid(column=1,row=4,sticky=tk.W)

            self.fourthGroundLabel = ttk.Label(self.groundChoiceLabel,text='Fourth squad of ground units:')
            self.fourthGroundLabel.grid(column=0,row=5,sticky=tk.W)
            self.fourthGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.fourthUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.fourthGroundUnits.grid(column=1,row=5,sticky=tk.W)

            self.firstGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadOneNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.firstGroundUnitNumSelect.grid(column=2,row=2,sticky=tk.W)
            self.secondGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadTwoNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.secondGroundUnitNumSelect.grid(column=2,row=3,sticky=tk.W)

            self.thirdGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadThreeNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.thirdGroundUnitNumSelect.grid(column=2,row=4,sticky=tk.W)

            self.fourthGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadFourNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.fourthGroundUnitNumSelect.grid(column=2,row=5,sticky=tk.W)

            self.groundSquadSelect.configure(state="disabled")
        if self.groundSquad.get() == 5:
            self.firstGroundLabel = ttk.Label(self.groundChoiceLabel,text='First squad of ground units:')
            self.firstGroundLabel.grid(column=0,row=2, sticky=tk.W)
            self.firstGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.unitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.firstGroundUnits.grid(column=1,row=2,sticky=tk.W)
            self.secondGroundLabel = ttk.Label(self.groundChoiceLabel,text='Second squad of ground units:')
            self.secondGroundLabel.grid(column=0,row=3,sticky=tk.W)
            self.secondGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.secoundUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.secondGroundUnits.grid(column=1,row=3,sticky=tk.W)

            self.thirdGroundLabel = ttk.Label(self.groundChoiceLabel,text='Third squad of ground units:')
            self.thirdGroundLabel.grid(column=0,row=4,sticky=tk.W)
            self.thirdGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.thirdUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.thirdGroundUnits.grid(column=1,row=4,sticky=tk.W)

            self.fourthGroundLabel = ttk.Label(self.groundChoiceLabel,text='Fourth squad of ground units:')
            self.fourthGroundLabel.grid(column=0,row=5,sticky=tk.W)
            self.fourthGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.fourthUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.fourthGroundUnits.grid(column=1,row=5,sticky=tk.W)

            self.fifthGroundLabel = ttk.Label(self.groundChoiceLabel,text='Fifth squad of ground units:')
            self.fifthGroundLabel.grid(column=0,row=6,sticky=tk.W)
            self.fifthGroundUnits = ttk.OptionMenu(self.groundChoiceLabel,self.fifthUnitOptionSelected,self.unitSelector[0],*self.unitSelector)
            self.fifthGroundUnits.grid(column=1,row=6,sticky=tk.W)
            self.fifthGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadFifthNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.fifthGroundUnitNumSelect.grid(column=2,row=6,sticky=tk.W)
            self.firstGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadOneNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.firstGroundUnitNumSelect.grid(column=2,row=2,sticky=tk.W)
            self.secondGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadTwoNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.secondGroundUnitNumSelect.grid(column=2,row=3,sticky=tk.W)

            self.thirdGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadThreeNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.thirdGroundUnitNumSelect.grid(column=2,row=4,sticky=tk.W)

            self.fourthGroundUnitNumSelect = ttk.OptionMenu(self.groundChoiceLabel,self.groundUnitSquadFourNumSelect,self.groundUnitSquadNum[0],*self.groundUnitSquadNum)
            self.fourthGroundUnitNumSelect.grid(column=2,row=5,sticky=tk.W)
            self.groundSquadSelect.configure(state="disabled")
if __name__=="__main__":
    application = Menu()
    application.mainloop()



