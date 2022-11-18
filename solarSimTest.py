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
        self.planetNumSelector=[1,2,3,4,5,6,7,8,9,10]
        self.planetOption = tk.StringVar(self)
        self.planetNumOption = tk.IntVar(self)
        self.createWidgets()


    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        label = ttk.Label(self, text='Select how many planets in this solar system:')
        label.grid(column=0,row=0,sticky=tk.W,**paddings)
        planetNumSel = ttk.OptionMenu(self,self.planetNumOption,self.planetNumSelector[0],*self.planetNumSelector,command=self.planetNum)
        planetNumSel.grid(column=1,row=0,sticky=tk.W,**paddings)
    def planetNum(self,*args):
        planetsToAdd = ttk.OptionMenu(self,self.planetOption,self.planetSelector[0],*self.planetSelector,command = self.planets)
        planetsToAdd.grid(column=0,row=1,sticky=tk.W)
            
        
    def planetAdd(self,*args):
        planetsToAdd = ttk.OptionMenu(self,self.planetOption,self.planetSelector[0],*self.planetSelector,command = self.planets)
        planetsToAdd.grid(column=0,row=1,sticky=tk.W)
    def planets(self,*args):
        pass

if __name__=="__main__":
    app = Menu()
    app.mainloop()
