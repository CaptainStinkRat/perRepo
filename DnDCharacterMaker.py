import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('560x320')
        self.title('DnD Character Maker')
        # self.style = ttk.Style()
        # self.style.theme_use('clam')
        self.searchTerm = tk.StringVar(self)
        self.classSelection = tk.StringVar(self)
        self.classSelector = ['Monk','Barbarian','Archer','Rogue','Mage','Warlock','Paladin','Bard']
        self.speciesSelection = tk.StringVar(self)
        self.speciesSelector = ['Elf','Human','Gnome','Halfling','Dwarf']
        self.dwarfPath = 'dwarf.jpg'
        self.humanPath = 'human.jpg'
        self.elfPath = 'elf.jpg'
        self.gnomePath = 'gnome.jpg'
        self.halflingPath = 'halfling.jpg'
        self.createWidgets()
    def createWidgets(self):
        self.searchEntry = ttk.Entry(self,textvariable=self.searchTerm,width=30)
        self.searchEntry.grid(row=0,column=0)
        self.speciesSelect = ttk.OptionMenu(self,self.speciesSelection,self.speciesSelector[0],*self.speciesSelector,command=self.speciesPick)
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
        self.image = ImageTk.PhotoImage(Image.open(self.elfPath))
        self.panel = tk.Label(self,image = self.image)
        self.panel.grid(row=1,column=1)
        self.createButton = ttk.Button(self,text='Create character!')
        self.createButton.grid(row=2,column=0)

    def classPicks(self,*args):
        if self.classSelection.get() == 'Monk':
            self.dexterityInsert.delete(0,END)
            self.strengthInsert.delete(0,END)
            self.intellectInsert.delete(0,END)
            self.constitutionInsert.delete(0,END)
            self.wisdomInsert.delete(0,END)
            self.charismaInsert.delete(0,END)

            self.dexterityInsert.insert(0,12)
            self.strengthInsert.insert(0,10)
            self.intellectInsert.insert(0,7)
            self.constitutionInsert.insert(0,13)
            self.wisdomInsert.insert(0,10)
            self.charismaInsert.insert(0,8)
            
        elif self.classSelection.get() == 'Barbarian':
            self.dexterityInsert.delete(0,END)
            self.strengthInsert.delete(0,END)
            self.intellectInsert.delete(0,END)
            self.constitutionInsert.delete(0,END)
            self.wisdomInsert.delete(0,END)
            self.charismaInsert.delete(0,END)
            self.dexterityInsert.insert(0,4)
            self.strengthInsert.insert(0,14)
            self.intellectInsert.insert(0,5)
            self.constitutionInsert.insert(0,15)
            self.wisdomInsert.insert(0,5)
            self.charismaInsert.insert(0,6)
        elif self.classSelection.get() == 'Archer':
            self.dexterityInsert.delete(0,END)
            self.strengthInsert.delete(0,END)
            self.intellectInsert.delete(0,END)
            self.constitutionInsert.delete(0,END)
            self.wisdomInsert.delete(0,END)
            self.charismaInsert.delete(0,END)
            self.dexterityInsert.insert(0,13)
            self.strengthInsert.insert(0,5)
            self.intellectInsert.insert(0,8)
            self.constitutionInsert.insert(0,6)
            self.wisdomInsert.insert(0,7)
            self.charismaInsert.insert(0,8)
        elif self.classSelection.get() == 'Rogue':
            self.dexterityInsert.delete(0,END)
            self.strengthInsert.delete(0,END)
            self.intellectInsert.delete(0,END)
            self.constitutionInsert.delete(0,END)
            self.wisdomInsert.delete(0,END)
            self.charismaInsert.delete(0,END)
            self.dexterityInsert.insert(0,14)
            self.strengthInsert.insert(0,5)
            self.intellectInsert.insert(0,8)
            self.constitutionInsert.insert(0,6)
            self.wisdomInsert.insert(0,7)
            self.charismaInsert.insert(0,7)
        elif self.classSelection.get() == 'Warlock':
            self.dexterityInsert.delete(0,END)
            self.strengthInsert.delete(0,END)
            self.intellectInsert.delete(0,END)
            self.constitutionInsert.delete(0,END)
            self.wisdomInsert.delete(0,END)
            self.charismaInsert.delete(0,END)
            self.dexterityInsert.insert(0,6)
            self.strengthInsert.insert(0,5)
            self.intellectInsert.insert(0,11)
            self.constitutionInsert.insert(0,6)
            self.wisdomInsert.insert(0,10)
            self.charismaInsert.insert(0,4)
        elif self.classSelection.get() == 'Paladin':
            self.dexterityInsert.delete(0,END)
            self.strengthInsert.delete(0,END)
            self.intellectInsert.delete(0,END)
            self.constitutionInsert.delete(0,END)
            self.wisdomInsert.delete(0,END)
            self.charismaInsert.delete(0,END)
            self.dexterityInsert.insert(0,6)
            self.strengthInsert.insert(0,11)
            self.intellectInsert.insert(0,8)
            self.constitutionInsert.insert(0,11)
            self.wisdomInsert.insert(0,8)
            self.charismaInsert.insert(0,8)
        elif self.classSelection.get() == 'Bard':
            self.dexterityInsert.delete(0,END)
            self.strengthInsert.delete(0,END)
            self.intellectInsert.delete(0,END)
            self.constitutionInsert.delete(0,END)
            self.wisdomInsert.delete(0,END)
            self.charismaInsert.delete(0,END)
            self.dexterityInsert.insert(0,7)
            self.strengthInsert.insert(0,5)
            self.intellectInsert.insert(0,10)
            self.constitutionInsert.insert(0,7)
            self.wisdomInsert.insert(0,9)
            self.charismaInsert.insert(0,12)
    def speciesPick(self,*args):
        if self.speciesSelection.get() == 'Elf':
            self.image = ImageTk.PhotoImage(Image.open(self.elfPath))
            self.panel = tk.Label(self,image = self.image)
            self.panel.grid(row=1,column=1)
        elif self.speciesSelection.get() == 'Dwarf':
            self.image = ImageTk.PhotoImage(Image.open(self.dwarfPath))
            self.panel = tk.Label(self,image = self.image)
            self.panel.grid(row=1,column=1)
        elif self.speciesSelection.get() == 'Human':
            self.image = ImageTk.PhotoImage(Image.open(self.humanPath))
            self.panel = tk.Label(self,image = self.image)
            self.panel.grid(row=1,column=1)
        elif self.speciesSelection.get() == 'Halfling':
            self.image = ImageTk.PhotoImage(Image.open(self.halflingPath))
            self.panel = tk.Label(self,image = self.image)
            self.panel.grid(row=1,column=1)
        elif self.speciesSelection.get() == 'Gnome':
            self.image = ImageTk.PhotoImage(Image.open(self.gnomePath))
            self.panel = tk.Label(self,image = self.image)
            self.panel.grid(row=1,column=1)
if __name__=='__main__':
    app = Menu()
    app.mainloop()