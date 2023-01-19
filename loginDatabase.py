import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x120')

        self.title('User login')
        self.passwordEntry = tk.StringVar(self)
        self.userNameEntry = tk.StringVar(self)
        self.createWidgets()

    def createWidgets(self):
        
        data = pd.read_csv(r'LoginDatabase.csv')
        self.dataCol = ('username','password')
        self.df = pd.DataFrame(data,columns=self.dataCol)
        
        self.userName = Entry(self,textvariable=self.userNameEntry)
        self.userName.insert(0,'Username')
        self.password = Entry(self,show='*',textvariable=self.passwordEntry)
        self.password.insert(0,'Password')
        self.userName.pack()
        self.password.pack()
        self.userName.bind('<FocusIn>',self.tempUsernameText)
        self.password.bind('<FocusIn>',self.tempPasswordText)
        self.loginButton = ttk.Button(self,text='Login',command=self.verifyLogin)
        self.loginButton.pack()
        self.registerButton = ttk.Button(self,text='Create account',command=self.createUser)
        self.registerButton.pack()
    def tempUsernameText(self,e):
        self.userName.delete(0,'end')
    def tempPasswordText(self,e):
        self.password.delete(0,'end')
    def verifyLogin(self):
        if self.userNameEntry.get() in self.df.values:
            if self.passwordEntry.get() in self.df.values:
                self.destroy()
                mainWindow = tk.Tk()
                mainWindow.wm_title('Character selector')
                label = ttk.Label(mainWindow,text='Welcome back!')
                label.pack()
            else:
                failedLogin = tk.Tk()
                failedLogin.wm_title('Failed login')
                label = ttk.Label(failedLogin,text='Username or password incorrect!')
                label.pack()
        else:
            
                failedLogin = tk.Tk()
                failedLogin.wm_title('Failed login')
                label = ttk.Label(failedLogin,text='Username or password incorrect!')
                label.pack()
    def createUser(self):
        if self.userNameEntry.get() in self.df.values :
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup,text='Username in use!')
            label.pack()
            b1 = ttk.Button(popup,text='Okay',command=popup.destroy)
            b1.pack()
        else:
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup,text='Account created!')
            label.pack()
            b1 = ttk.Button(popup,text='Okay',command=popup.destroy)
            b1.pack()
            self.df.loc[len(self.df.index)] = [f'{self.userNameEntry.get()}',f'{self.passwordEntry.get()}']
            self.df.to_csv('LoginDatabase.csv')
if __name__=='__main__':
    app = Menu()
    app.mainloop()
