import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("480x240")
        self.title('Solar System Creator')

        self.planetSelector=('Earthlike','Marslike','Mercurylike',
        'Venuslike','Jupiterlike','Saturnlike','Uranuslike','Neptunelike')
        self.planetOption = tk.StringVar(self)
        self.planetOption2 = tk.StringVar(self)
        self.planetOption3 = tk.StringVar(self)
        self.planetOption4 = tk.StringVar(self)
        self.planetOption5 = tk.StringVar(self)
        self.planetNumOption = tk.IntVar(self)
        self.planetGrav = tk.IntVar(self)
        self.planetGrav2 = tk.IntVar(self)
        self.planetGrav3 = tk.IntVar(self)
        self.planetGrav4 = tk.IntVar(self)
        self.planetGrav5 = tk.IntVar(self)
        self.createWidgets()
        self.planetNumOption.set(0)

    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        label = ttk.Label(self, text='Select how many planets in this solar system (up to 5):')
        label.grid(column=0,row=0,sticky=tk.W,**paddings)
        planetNumSel = ttk.Button(self,text='Add a planet',command=self.planetNum)
        planetNumSel.grid(column=1,row=0,sticky=tk.W,**paddings)
        self.planetCount = 0
    
    def planetNum(self,*args):
        self.planetCount = self.planetCount + 1
        planetsToAdd = ttk.OptionMenu(self,self.planetOption,self.planetSelector[0],*self.planetSelector,command = self.planets)
        planetsToAdd.grid(column=0,row=1,sticky=tk.W)
        planetSlider = tk.Scale(self, from_=0.5, to=200,orient='horizontal',variable=self.planetGrav)
        planetSlider.set(100)
        planetSlider.grid(column=1,row=1,sticky=tk.W)
        if self.planetCount == 2:
            planetsToAdd2 = ttk.OptionMenu(self,self.planetOption2,self.planetSelector[0],*self.planetSelector,command = self.planets)
            planetsToAdd2.grid(column=0,row=2,sticky=tk.W)
            planetSlider2 = tk.Scale(self, from_=0.5, to=200,orient='horizontal',variable=self.planetGrav2)
            planetSlider2.set(100)
            planetSlider2.grid(column=1,row=2,sticky=tk.W)
        elif self.planetCount == 3:
            planetsToAdd3 = ttk.OptionMenu(self,self.planetOption3,self.planetSelector[0],*self.planetSelector,command = self.planets)
            planetsToAdd3.grid(column=0,row=3,sticky=tk.W)
            planetSlider3 = tk.Scale(self, from_=0.5, to=200,orient='horizontal',variable=self.planetGrav3)
            planetSlider3.set(100)
            planetSlider3.grid(column=1,row=3,sticky=tk.W)
        elif self.planetCount == 4:
            planetsToAdd4 = ttk.OptionMenu(self,self.planetOption4,self.planetSelector[0],*self.planetSelector,command = self.planets)
            planetsToAdd4.grid(column=0,row=4,sticky=tk.W)
            planetSlider4 = tk.Scale(self, from_=0.5, to=200,orient='horizontal',variable=self.planetGrav4)
            planetSlider4.set(100)
            planetSlider4.grid(column=1,row=4,sticky=tk.W)
        elif self.planetCount == 5:
            planetsToAdd5 = ttk.OptionMenu(self,self.planetOption5,self.planetSelector[0],*self.planetSelector,command = self.planets)
            planetsToAdd5.grid(column=0,row=5,sticky=tk.W)
            planetSlider5 = tk.Scale(self, from_=0.5, to=200,orient='horizontal',variable=self.planetGrav5)
            planetSlider5.set(100)
            planetSlider5.grid(column=1,row=5,sticky=tk.W)
        else:
            pass
    def planetAdd(self,*args):
        planetsToAdd = ttk.OptionMenu(self,self.planetOption,self.planetSelector[0],*self.planetSelector,command = self.planets)
        planetsToAdd.grid(column=0,row=1,sticky=tk.W)
    def planets(self,*args):
        pass

if __name__=="__main__":
    app = Menu()
    app.mainloop()
