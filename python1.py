#program to transfer files after checking for modification within last 24 hours
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import time, shutil
import db_tab

class fileMov:
    def __init__(self,master):
        self.frame1 = ttk.Frame(master)
        self.frame1.pack()
        self.frame2 = ttk.Frame(master)
        self.frame2.pack()
        self.label1 = ttk.Label(self.frame1, text = "This program allows you to check files modified and move them to a new folder")
        self.label1.grid(row=0,column=0)
        self.label2 = ttk.Label(self.frame1, text = "The last file check was done on: "+str(db_tab.disp_tab()))
        self.label2.grid(row=1,column=0)
        
        def folderMod():
            global sourceFold
            sourceFold = filedialog.askdirectory(initialdir = os.getcwd(), title = 'Choose the folder',
                                          mustexist =1)
            
        
        #DirDialog to check modified folder
        def folderMove():
            global destFold
            destFold = filedialog.askdirectory(initialdir = os.getcwd(), title = 'Choose the folder',
                                          mustexist =1)
            

        def fileTrans():
            global file_es, sourceFold
            print("Source: "+sourceFold)
            print("Destination: "+destFold)
        
            for fil_es in os.listdir(sourceFold):
            
                print("last modified: {}" .format(time.ctime(os.path.getmtime(sourceFold+"/"+fil_es))))
                if (time.time() - os.stat(sourceFold+"/"+fil_es).st_mtime)/(60*60) < 24:
                    shutil.move(sourceFold+"/"+fil_es,destFold)
        
            #Invoking message box
            messagebox.showinfo(title ="File Transfer Info",message = "File Transfer Successful")
            
            #calling database
            db_tab.update_tab()
        
        #buttons
        self.button1 = ttk.Button(self.frame2,text = "Choose the folder for file check",
                                  command = folderMod)
        self.button1.grid(row=0,column=0)
        self.button2 = ttk.Button(self.frame2,text = "Choose the folder for moving modified files",
                                  command = folderMove)
        self.button2.grid(row=0,column=1)
        self.button3 = ttk.Button(self.frame2,text = "Initiate move", command = fileTrans)
        self.button3.grid(row=1,column=0,columnspan = 2)

def main():
    root = Tk()
    app = fileMov(root)
    root.mainloop()

if __name__ == "__main__":main()
