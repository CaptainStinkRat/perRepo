import tkinter as tk
from tkinter import ttk
import pandas as pd
import xlsxwriter
from tkinter import *

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("480x240")
        self.title('Package tester')
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.searchTerm = tk.StringVar(self)
        self.packageAdd = tk.StringVar(self)
        self.versionAdd = tk.StringVar(self)
        self.createWidgets()

    def createWidgets(self):

        data = pd.read_csv(r'pythonPackageList.csv')
        self.dataCol = ['Package Name ','Version Scanned']
        self.df = pd.DataFrame(data,columns=self.dataCol)
        self.searchTerm.trace('w',self.searchData)
        self.searchEntry = Entry(self,textvariable=self.searchTerm,width=40)
        self.searchEntry.pack()
        self.tree = ttk.Treeview(self, columns=self.dataCol,show='headings',height=5)
        self.tree.column('# 1', anchor='center')
        self.tree.heading('# 1',text='Package Name')
        self.tree.column('# 2',anchor='center')
        self.tree.heading('# 2',text='Version Scanned')
        sBar = ttk.Scrollbar(self,orient='vertical',command=self.tree.yview)
        sBar.pack(side='right',fill='x')
        self.tree.configure(xscrollcommand=sBar.set)

        
        for self.x in self.df.values.tolist():
        
            self.tree.insert('',1,text='1',values=self.x,tags=self.x)
        #self.tree.insert('','end',text='1',values=df.values[1])
        # self.tree.selection_set(self.tree.tag_has(self.searchData.get()))
        self.tree.pack()
        addEntry = ttk.Button(self,text='Add Python Package to approved list',command=self.entryAdding)
        addEntry.pack()
        self.refreshButton = Button(self,text='Refresh list',command=self.refreshList)
        self.refreshButton.configure(state='disabled')
        self.refreshButton.pack()
    def searchData(self,*args):
        self.tree.selection_set(self.tree.tag_has(self.searchTerm.get()))
        pass
    def entryAdding(self,*args):
        self.top = Toplevel(self)
        self.top.geometry("200x200")
        packageNameLabel = Label(self.top,text='Enter name of package:')
        packageNameLabel.pack()

        addingEntry = Entry(self.top,textvariable=self.packageAdd,width=25)
        addingEntry.pack()
        versionLabel = Label(self.top,text='Enter version of package:')
        versionLabel.pack()
        versionEntry = Entry(self.top,textvariable=self.versionAdd,width=25)
        versionEntry.pack()
        addButton = Button(self.top,text='Ok',command=self.submit)
        addButton.pack()

        pass
    def submit(self,*args):
        self.df.loc[len(self.df.index)]=[f'{self.packageAdd.get()}',f'{self.versionAdd.get()}']
        self.df.to_csv('pythonPackageList.csv')
        self.refreshButton.configure(state='active')
        self.top.destroy()
    def refreshList(self,*args):
        # data = pd.read_csv(r'pythonPackageList.csv')
        # self.dataCol = ['Package Name ','Version Scanned']
        # self.df = pd.DataFrame(data,columns=self.dataCol)
        for item in self.tree.get_children():
            self.tree.delete(item)
        for self.x in self.df.values.tolist():
        
            self.tree.insert('',1,text='1',values=self.x,tags=self.x)
        
if __name__ == '__main__':
    app = Menu()
    app.mainloop()
