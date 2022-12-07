import xlsxwriter
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog as fd


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("480x240")
        self.title ('Donnifier')
        self.monthSelectOption = ['Jan','Feb','Mar','Apr','May','Jun','Jul',
        'Aug','Sep','Oct','Nov','Dec']
        self.yearSelectOption = [2022,2023,2024,2025]
        self.monthSelector = tk.StringVar(self)
        self.yearSelector = tk.IntVar(self)
        self.reportSelector = tk.StringVar(self)
        self.reportSelectOption = ['Clicker Report','Incident Report','5 Courses','Repeat Offenders']
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
        donnifyButton = ttk.Button(self,text='Donnify report',command=self.formatFile)
        donnifyButton.grid(column=2,row=4,sticky=tk.W,**paddings) 
        selectLabel = ttk.Label(self,text='Select month and year of the report: ')
        selectLabel.grid(column=0,row=2,sticky=tk.W,**paddings)
        monthSelect = ttk. OptionMenu(self,self.monthSelector,self.monthSelectOption[0],*self.monthSelectOption)
        monthSelect.grid(column = 1,row=2,sticky=tk.W,**paddings)
        yearSelect = ttk.OptionMenu(self,self.yearSelector,self.yearSelectOption[0],*self.yearSelectOption)
        yearSelect.grid(column=2,row=2,sticky=tk.W,**paddings)
        typeOfReport = ttk.OptionMenu(self,self.reportSelector,self.reportSelectOption[0],*self.reportSelectOption)
        typeOfReport.grid(column=1,row=3,sticky=tk.W,**paddings)
        reportLabel = ttk.Label(self,text='What type of report is it?')
        reportLabel.grid(column=0,row=3,sticky=tk.W,**paddings) 

    def unformattedFile(self,*args):
        self.openFile = fd.askopenfilename(title='Open a File',file=(("xlsx files",".*xlsx"),("All Files","*.")))
        self.outputLabel = ttk.Label(self,foreground='red')
        self.outputLabel.grid(column=0,row=1,sticky=tk.W)
        fileName = r"{}".format(self.openFile)
        df = pd.read_excel(fileName)
        writer = pd.ExcelWriter(fileName,engine='xlsxwriter',datetime_format='dd/mm/yy hh:mm')
        df.to_excel(writer,sheet_name=f'{self.monthSelector.get()} {self.yearSelector.get()} {self.reportSelector.get()}',index=False,startrow=0,startcol=0,header=False,columns=["Email",'First Name','Last Name','Job Title','Manager Name','Manager Email','Content','Enrolled','Started','Completed','Time Spent','Status','Score'])
        my_list = ["Email",'First Name','Last Name','Job Title','Manager Name','Manager Email','Content','Enrolled','Started','Completed','Time Spent','Status','Score']
        workbook = writer.book
        worksheet = writer.sheets[f'{self.monthSelector.get()} {self.yearSelector.get()} {self.reportSelector.get()}']
        header_format = workbook.add_format({'bold':True,
         'fg_color':'#FFC000','align':'center','border':1})
        for col_num,data in enumerate(my_list):
            worksheet.write(0,col_num,data,header_format)
        percent_format = workbook.add_format({'num_format':'0%'})
        worksheet.set_column('M:M',None,percent_format)
        rightFormat = workbook.add_format({'align':'right'})
        worksheet.set_column('K:K',None,rightFormat)
        # for col_num,value in enumerate(df.columns):
        #     worksheet.write(0,col_num,value,header_format)
        writer.save()

    def formatFile(self,*args):
        # workbook = xlsxwriter.Workbook(r"{}".format(self.openFile))
        # worksheet = workbook.add_worksheet()
        # header_format = workbook.add_format({'bold':True,
        # 'fg_color':'#FFC000','align':'center','border':1})
        # worksheet.set_row(0,None,header_format)
        self.destroy()
        pass
        #self.formatFile = asksaveasfile(initialfile='Untitled report',defaultextension='.xlsx',filetypes=[('xlsx Files','*.xlsx'),('All Files','*.*')])
#         workbook = xlsxwriter.Workbook(self.formatFile)

#         worksheet = workbook.add_worksheet()

#         cell_format = workbook.add_format({'bold':True, 'has_fill': 'orange'})
#         date_cell_format = workbook.add_format({'num_format':'dd/mm/yy hh:mm'})
#         time_cell_format = workbook.add_format({'num_format':'h:mm:ss'})
#         date_cell_format.set_font_size(11)
#         date_cell_format.set_font_charset('Calibri (Body)')
#         date_cell_format.set_align('center')
#         time_cell_format.set_font_size(11)
#         time_cell_format.set_font_charset('Calibri (Body)')
#         time_cell_format.set_align('center')
# # body_cell_format.set_font_size(11)
# # body_cell_format.set_font_charset('Calibri (Body)')
# # body_cell_format.set_align('center')
#         cell_format.set_font_size(12)
#         cell_format.set_font_charset('Calibri (Body)')
#         cell_format.set_align('center')
#         worksheet.write('A1:M1',self.headers,cell_format)
#         # worksheet.write('A1', 'Email', cell_format)
#         # worksheet.write('B1','First Name', cell_format)
#         # worksheet.write('C1','Last Name', cell_format)
#         # worksheet.write('D1', 'Job Title', cell_format)
#         # worksheet.write('E1', 'Manager Name',cell_format)
#         # worksheet.write('F1', 'Manager Email', cell_format)
#         # worksheet.write('G1', 'Content',cell_format)
#         # worksheet.write('H1', 'Enrolled',cell_format)
#         # worksheet.write('I1', 'Started',cell_format)
#         # worksheet.write('J1','Completed',cell_format)
#         # worksheet.write('K1','Time Spent',cell_format)
#         # worksheet.write('L1','Status',cell_format)
#         # worksheet.write('M1','Score',cell_format)
# # worksheet.write('H2',date_cell_format)
# # worksheet.write('I2',date_cell_format)
# # worksheet.write('J2',date_cell_format)
# # worksheet.write('K2',time_cell_format)
#         row = 1
#         col = 0

# # data = (
# #     ['']
# # )

#         # for name, score in (data):
#         #     worksheet.write(row,col,name)
#         #     worksheet.write(row,col+1,score)
#         # row += 1

#         workbook.close()

if __name__ == "__main__":
    app = Menu()
    app.mainloop()
