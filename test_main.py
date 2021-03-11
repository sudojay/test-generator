import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import os
from openpyxl import workbook

class Main:
    def __init__(self,master):
        self.master=master
        master.title("Test Generator")
        width=600
        height = 400
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        master.geometry("%dx%d+%d+%d" % (width, height, x, y))
        master.resizable(0, 0)
        self.Top = Frame(master, bd=2,  relief=RIDGE)
        self.Top.pack(side=TOP, fill=X)
        self.Base = Frame(master, height=200)
        self.Base.pack(side=TOP, pady=20)
        self.HomeWindow()

    def HomeWindow(self):
        for widget in self.Top.winfo_children():
            widget.destroy()
        for widget in self.Base.winfo_children():
            widget.destroy()
        self.lbl = Label(self.Top, text="Welcome to Test Generator",font=('arial', 15))
        self.lbl.pack(anchor='n')
        self.lbl_brs = Label(self.Base, text='Click on browse and select a Excel file: ',font=('arial', 14))
        self.lbl_brs.grid(row=1,column=1)
        self.gen=Button(self.Base, text="Browse", width=25, command=self.UploadAction)
        self.gen.grid(row=1, column=2)
    
    def UploadAction(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        print('Selected:', self.filename)
        if len(self.filename) == 0:
            self.HomeWindow()
        else:
            self.MainWindow()

    def MainWindow(self):
        for widget in self.Top.winfo_children():
            widget.destroy()
        for widget in self.Base.winfo_children():
            widget.destroy()
        self.l3 = Label(self.Top, text="Generate",font=('arial', 15))
        self.l3.pack(anchor='n')
        self.lbl_mks = Label(self.Base, text='No of Questions: ',font=('arial', 14))
        self.lbl_mks.grid(row=1,column=1)
        self.ent_mks = Entry(self.Base, width=45)
        self.ent_mks.grid(row=1, column=2)
        self.b1=Button(self.Base, text="Generate", width=40, command=self.reader)
        self.b1.grid(row=10, column=2)
        self.lbl_blnk=Label(self.Base)
        self.lbl_blnk.grid(row=11,column=2)

    def reader(self):
        df_temp = pd.read_excel(self.filename, engine="openpyxl")
        print(df_temp)
        self.num = int(self.ent_mks.get()) 
        if self.ent_mks.get() == "0":
            messagebox.showerror("Error", "Please provide a valid input")
            self.ent_mks.delete(0,'end')
        df=pd.DataFrame(df_temp)
        counter=0
        self.datafile=open("sample_test_xlsx.txt","w")
        self.ansfile=open("sample_answer_xlsx.txt","w")
        self.ans=df.sample(self.num)
        self.temp=pd.DataFrame(self.ans)
        for index,row in self.temp.iterrows():
            counter+=1
            self.datafile.write(str(counter)+")")
            self.datafile.write(row[0]+"\n")
            self.datafile.write(row[1]+"\n")
            self.datafile.write(row[2]+"\n")
            self.datafile.write(row[3]+"\n")
            self.datafile.write(row[4]+"\n")
            self.datafile.write("\n")            
            self.ansfile.write(str(counter)+")")                    
            self.ansfile.write(row[5]+"\n")
        self.datafile.close()
        self.ansfile.close() 
        self.ent_mks.delete(0,'end')
        os.startfile("sample_answer_xlsx.txt")
        os.startfile("sample_test_xlsx.txt")

root = Tk()
my_gui = Main(root)
root.mainloop()
    
