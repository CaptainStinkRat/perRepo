import tkinter as tk
from tkinter import ttk

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("480x240")
        self.title ('Army Creator')

        self.armySelector = ('Red','Blue')
        self.teamOption = tk.StringVar(self)
        self.unitOption = tk.StringVar(self)
        self.vehicleOption = tk.StringVar(self)
        self.vehicleAmount = tk.IntVar(self)
        self.unitAmount = tk.IntVar(self)
        self.unitSelector = ('Foot solider','Pilot','Engineer')
        self.vehicleSelector = ('Tank','Jeep','Airplane')
        self.createWidgets()

    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        label = ttk.Label(self, text='Select an army to build: ')
        label.grid(column=0,row=0,sticky=tk.W, **paddings)

        optionMenu = ttk.OptionMenu(
            self,
            self.teamOption,
            self.armySelector[0],
            *self.armySelector,
            command=self.option_changed)

        optionMenu.grid(column=1, row=0,sticky=tk.W,**paddings)

        unitButton = ttk.Button(self,text='Add units',command=self.unitsAdd)
        unitButton.grid(column=2,row=0,sticky=tk.W,**paddings)
        vehicleButton = ttk.Button(self,text='Add vehicle(s)',command=self.vehicleAdd)
        vehicleButton.grid(column=3,row=0,sticky=tk.W,**paddings)
        self.outputLabel = ttk.Label(self,foreground='red')
        self.outputLabel.grid(column=0,row=1,sticky=tk.W,**paddings)
        self.vehicleOutputLabel = ttk.Label(self,foreground='black')
        self.vehicleOutputLabel.grid(column=3,row=4,sticky=tk.W,**paddings)
        self.unitOutputLabel = ttk.Label(self,foreground='black')
        self.unitOutputLabel.grid(column=3,row=2,sticky=tk.W,**paddings)
    def option_changed(self,*args):
        self.outputLabel['text']=f'You selected: {self.teamOption.get()}'

    def unitsAdd(self,*args):
        unitsToAdd = ttk.OptionMenu(self,self.unitOption,self.unitSelector[0],*self.unitSelector,command =self.units )
        unitsToAdd.grid(column=0, row=2,sticky=tk.W)
        unitSlider = tk.Scale(self, from_=0, to=500, orient='horizontal',variable=self.unitAmount)
        unitSlider.grid(column=1,row=2,stick=tk.W)
        unitSet = ttk.Button(self,text='Set',command=self.unitSet)
        unitSet.grid(column=1,row=3,sticky=tk.W)
    def units(self,*args):
        pass
    def vehicleAdd(self,*args):
        vehicleToAdd = ttk.OptionMenu(self,self.vehicleOption,self.vehicleSelector[0],*self.vehicleSelector,command = self.vehicles)
        vehicleToAdd.grid(column=0,row=4,sticky=tk.W)
        vehicleSlider = tk.Scale(self, from_=0, to=500,orient='horizontal',variable=self.vehicleAmount)
        vehicleSlider.grid(column=1,row=4,sticky=tk.W)
        vehicleSet = ttk.Button(self,text='Set',command=self.vehicleSet)
        vehicleSet.grid(column=1,row=5,sticky=tk.W)
    def vehicles(self,*args):
        pass
    def vehicleSet(self,*args):
        self.vehicleOutputLabel['text']=f'{self.vehicleAmount.get()} {self.vehicleOption.get()}'
    def unitSet(self,*args):
        self.unitOutputLabel['text']=f'{self.unitAmount.get()} {self.unitOption.get()}'
if __name__ == "__main__":
    app = Menu()
    app.mainloop()
