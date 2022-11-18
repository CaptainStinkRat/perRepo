import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
import csv
from tkinter import filedialog as fd


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("480x240")
        self.title ('Donnifier')

        # self.armySelector = ('Red','Blue')
        # self.teamOption = tk.StringVar(self)
        # self.unitOption = tk.StringVar(self)
        # self.vehicleOption = tk.StringVar(self)
        # self.vehicleAmount = tk.IntVar(self)
        # self.unitAmount = tk.IntVar(self)
        # self.unitSelector = ('Foot solider','Pilot','Engineer')
        # self.vehicleSelector = ('Tank','Jeep','Airplane')
        self.createWidgets()
        # self.Email
        
    def createWidgets(self):
        paddings = {'padx':5,'pady':5}
        label = ttk.Label(self, text='Unformated report: ')
        label.grid(column=0,row=0,sticky=tk.W, **paddings)
        fileUploadButton = ttk.Button(self,text='File upload',command=self.unformattedFile)
        fileUploadButton.grid(column=1,row=0,sticky=tk.W,**paddings)
        formatFileButton = ttk.Button(self,text='Format file',command=self.formatFileLocation)
        formatFileButton.grid(column=2,row=0,sticky=tk.W,**paddings)
        donnifyButton = ttk.Button(self,text='Donnify report',command=self.formatFile)
        donnifyButton.grid(column=3,row=2,sticky=tk.W,**paddings)


    def unformattedFile(self,*args):
        self.openFile = fd.askopenfilename()
    def formatFileLocation(self,*args):
        self.formatFile = fd.askopenfilename()
    def formatFile(self,*args):
        #self.formatFile = fd.askopenfilename()
        with open(self.openFile) as unformattedCsvFile:
            unformattedCsvReader = csv.reader(unformattedCsvFile, delimiter= ',')
            self.unformattedList = []
            for row in unformattedCsvReader:
                self.unformattedList.append([row[0],row[1],row[2],row[3],row[5],row[6],row[10],row[11],row[12],row[13],row[14],row[15],row[17],row[18]])
        print(self.unformattedList)
        headers = ['Email', 'First Name', 'Last Name','Job Title','Manager Name','Manager Email','Content','Enrolled','Started',
                    'Completed','Time Spent','Status','Score' ]
        self.data = self.unformattedList
        with open(self.formatFile,"w",newline='') as formattedCsvFile:
            formattedWriter = csv.writer(formattedCsvFile)
                
            for row in self.data:
                formattedWriter.writerow(row)

    def save(self,*args):
        file = asksaveasfile(initialfile = 'UntitledArmy.txt',defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        fileWrite = open(file,"w+")
        fileWrite.write(self.vehicleOption,self.vehicleAmount,self.unitOption,self.unitAmount,self.teamOption)
        fileWrite.close()
if __name__ == "__main__":
    app = Menu()
    app.mainloop()
