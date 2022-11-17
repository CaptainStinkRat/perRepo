import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd   
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfile


def fileSelect():
    filetypes = (
        ('text files','*.txt'),
        ('All files','*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title = 'Selected File',
        message=filename
    )
def saveFile():
    f = asksaveasfile(initialfile = 'Untitled.txt',defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
def closeMenu():
    root.destroy()


root = tk.Tk()
root.geometry("500x200")

menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff = 0)
#fileMenu.add_command(label = "New",command = )
fileMenu.add_command(label = 'Open', command = fileSelect)
#fileMenu.add_command(label='Save',command=)
fileMenu.add_command(label='Save as...',command=lambda:saveFile())
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=root.quit)
menuBar.add_cascade(label = 'File',menu = fileMenu)
#root.config(menu=menuBar)

def vehicleSelect(selectedVehicle):
    global vehicleType
    vehicleType = selectedVehicle






teamChoice = tk.IntVar()

blueTeam = tk.Radiobutton(root, text = "Blue Team",variable = teamChoice, value = 0)
redTeam = tk.Radiobutton(root, text = "Red Team",variable = teamChoice, value = 1)
blueTeam.grid(row=1, column=1)
redTeam.grid(row=1,column=2)

vehicleChoice = tk.IntVar()

options = ['Jeeps','Tanks','Motorcycles']
vehiclePick = tk.StringVar(root)
vehiclePick.set(options[0])
vehicleDropDown = OptionMenu(root, vehiclePick, *options,command = vehicleSelect)
vehicleDropDown.grid(row=2,column=1)



def inputValue():
    global vehicleNum
    vehicleNum = textBox.get("1.0","end-1c")
textBox= Text(root, height=1,width=30)
textBox.grid(row=2,column=2)
buttonCommit=Button(root, height=1,width=30, text = "Army create", command=lambda: inputValue())
buttonCommit.grid(row=3,column=2)

root.config(menu=menuBar)
root.mainloop()



