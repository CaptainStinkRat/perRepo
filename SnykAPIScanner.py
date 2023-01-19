import tkinter as tk
from tkinter import ttk
import pandas as pd
import snyk
from tkinter import *
import webbrowser

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
        self.dataCol = ('Package Name ','Version Scanned')
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
        sBar.pack(side='right',fill='y')
        self.tree.configure(yscrollcommand=sBar.set)

        
        for self.x in self.df.values.tolist():
        
            self.tree.insert('',1,text='1',values=self.x,tags=self.x)
        #self.tree.insert('','end',text='1',values=df.values[1])
        # self.tree.selection_set(self.tree.tag_has(self.searchData.get()))
        self.tree.pack()
        addEntry = ttk.Button(self,text='Scan a package',command=self.entryAdding)
        addEntry.pack()
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
        client = snyk.SnykClient('1420765f-9921-426b-a64a-ed46fc3edb3d',tries=4,debug=True)

        org=client.organizations.first()

        result = org.test_python(f'{self.packageAdd.get()}',f'{self.versionAdd.get()}')
        if result.ok == False:
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup,text='Vulnerabilities found! Opening Snyk Security!')
            label.pack(side='top',fill='x',pady=10)
            b1 = ttk.Button(popup,text='Okay',command=popup.destroy)
            b1.pack()
            webbrowser.open(f'https://security.snyk.io/package/pip/{self.packageAdd.get()}', new =2)
            popup.mainloop()
        elif result.ok == True:
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup,text='No vulnerabilities found! Adding to master list.')
            label.pack(side='top',fill='x',pady=10)
            b1 = ttk.Button(popup,text='Okay',command=self.refresh)
            b1.pack()
            popup.mainloop()    
    def refresh(self,*args):
        self.df.loc[len(self.df.index)]=[f'{self.packageAdd.get()}',f'{self.versionAdd.get()}']
        self.df.to_csv('pythonPackageList.csv')
        for item in self.tree.get_children():
            self.tree.delete(item)
        for self.x in self.df.values.tolist():
        
            self.tree.insert('',1,text='1',values=self.x,tags=self.x)
        
        
if __name__ == '__main__':
    app = Menu()
    app.mainloop()
