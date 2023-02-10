import tkinter as tk
from tkinter import *
import json
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog as fd
import vt


class gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('680x240')
        self.title('Website Virustotal uploader')
        self.URLAdd = tk.StringVar(self)
        self.client = vt.Client('78b45954d30631f35ac8eee1e03996e6edc78fb7c5685559b9f71980b7682fc9')
        self.createWidgets()

    def writeToJSONFile(self,path, fileName, data):
        json.dump(data, path,indent=4,separators=(',',': '))
    def createWidgets(self):
        self.URLEntry = Entry(self,textvariable=self.URLAdd,width=50)
        self.URLEntry.grid(column=1,row=0)
        menubar = Menu(self)
        fileMenu = Menu(menubar,tearoff=0)
        fileMenu.add_command(label='Save',command=self.createJson)
        fileMenu.add_command(label='Load',command=self.loadJson)
        menubar.add_cascade(label='File',menu=fileMenu)
        self.config(menu=menubar)
        addButton = tk.Button(self,text='Add website to scan',command=self.addWebsite)
        addButton.grid(column=2,row=0,sticky=W)
        VTScanButton = tk.Button(self,text='Scan list on Virustotal',command=self.multipleScan)
        VTScanButton.grid(column=1,row=3,sticky=W)
        self.websiteList = Listbox(self)
        self.websiteList.grid(columnspan=5,row=1,sticky=W,ipadx=150)
        self.maliciousList = Listbox(self)
        self.maliciousList.grid(column=4,row=1)
        self.notMalicious = Listbox(self)
        self.notMalicious.grid(column=3,row=1)
        maliciousLabel = tk.Label(text='Malicious URLs')
        maliciousLabel.grid(column=4,row=0)
        notmaliciousLabel = tk.Label(text='Not Malicious URLs')
        notmaliciousLabel.grid(column=3,row=0)
    def addWebsite(self,*args):
        self.websiteList.insert(END,f'{self.URLAdd.get()}')
        self.URLEntry.delete(0,'end')

    def createJson(self,*args):
        data = []
        for i in self.websiteList.get(0,END):
            print(i)
            data.append({
                "Websites": f"{i}"
            })
        files = [('JSON File','*.json')]
        fileName = 'Websites'
        filePos = asksaveasfile(filetypes = files,defaultextension= json,initialfile='Websites')
        self.writeToJSONFile(filePos, fileName, data)
    def loadJson(self,*args):
        fileTypes = [('JSON files','*.json')]
        fileName = fd.askopenfilename(title='Open website list',initialdir='/',filetypes=fileTypes)
        with open(fileName) as jsonFile:
            listObj = json.load(jsonFile)
            x = len(listObj)
            for x in range(0,x):
                self.websiteList.insert(END,listObj[x]["Websites"])
    def multipleScan(self,*args):
        self.maliciousList.delete(0,END)
        self.notMalicious.delete(0,END)
        for i in self.websiteList.get(0,END):
            urlID = vt.url_id(i)
            url = self.client.get_object("/urls/{}".format(urlID))
            self.findings = url.get('last_analysis_stats')
            if self.findings['malicious'] > 0:
                self.maliciousList.insert(END,i)
            else:
                self.notMalicious.insert(END,i)
    
if __name__=='__main__':
    app = gui()
    app.mainloop()
