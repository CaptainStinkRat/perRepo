import tkinter as tk
from tkinter import *
from tkinter import ttk

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x320')
        self.title('DnD Character Maker')
        # self.style = ttk.Style()
        # self.style.theme_use('clam')
        self.searchTerm = tk.StringVar(self)
        self.classSelection = tk.StringVar(self)
        self.classSelector = ['Monk','Barbarian','Archer','Rogue','Mage','Warlock','Paladin','Bard']
        self.speciesSelection = tk.StringVar(self)
        self.speciesSelector = ['Elf','Human','Goblin','Gnome','Halfing','Dwarf','Dragonborn',]

        self.createWidgets()
    def createWidgets(self):
        self.searchEntry = ttk.Entry(self,textvariable=self.searchTerm,width=30)
        self.searchEntry.grid(row=0,column=0)
        self.speciesSelect = ttk.OptionMenu(self,self.speciesSelection,self.speciesSelector[0],*self.speciesSelector)
        self.speciesSelect.grid(row=0,column=1)
        self.classSelect = ttk.OptionMenu(self,self.classSelection,self.classSelector[0],*self.classSelector,command=self.classPicks)
        self.classSelect.grid(row=0,column=2)
        self.statsLabelFrame = ttk.LabelFrame(self,text='Stats')
        self.statsLabelFrame.grid(column=0,row=1,padx=20,pady=20)
        self.strengthLabel = ttk.Label(self.statsLabelFrame,text='Strength: ')
        self.strengthLabel.grid(row=0,column=0)
        self.strengthInsert = ttk.Entry(self.statsLabelFrame,width=2)
        self.strengthInsert.grid(row=0,column=1)
        self.intellectLabel = ttk.Label(self.statsLabelFrame,text='Intellect: ')
        self.intellectLabel.grid(row=1,column=0)
        self.intellectInsert = ttk.Entry(self.statsLabelFrame,width=2)
        self.intellectInsert.grid(row=1,column=1)
        self.dexterityLabel = ttk.Label(self.statsLabelFrame,text='Dexterity: ')
        self.dexterityLabel.grid(row=2,column=0)
        self.dexterityInsert = ttk.Entry(self.statsLabelFrame,width=2)
        self.dexterityInsert.grid(row=2,column=1)
        self.constitutionLabel = ttk.Label(self.statsLabelFrame,text='Constitution: ')
        self.constitutionLabel.grid(row=0,column=2)
        self.constitutionInsert = ttk.Entry(self.statsLabelFrame,width=2)
        self.constitutionInsert.grid(row=0,column=3)
        self.wisdomLabel = ttk.Label(self.statsLabelFrame,text='Wisdom: ')
        self.wisdomLabel.grid(row=1,column=2)
        self.wisdomInsert = ttk.Entry(self.statsLabelFrame,width=2)
        self.wisdomInsert.grid(row=1,column=3)
        self.charismaLabel = ttk.Label(self.statsLabelFrame,text='Charisma: ')
        self.charismaLabel.grid(row=2,column=2)
        self.charismaInsert = ttk.Entry(self.statsLabelFrame,width=2)
        self.charismaInsert.grid(row=2,column=3)

    def classPicks(self,*args):
        if self.classSelection.get() == 'Monk':
            self.dexterityInsert.insert(0,12)
            self.strengthInsert.insert(0,10)
            self.intellectInsert.insert(0,7)
            self.constitutionInsert.insert(0,13)
            self.wisdomInsert.insert(0,10)
            self.charismaInsert.insert(0,8)


if __name__=='__main__':
    app = Menu()
    app.mainloop()
