#This script has GUI to help add webpage contents, it also updates the content to be used later
from tkinter import *
from tkinter import ttk
import db_web
import web_create

class webCreate:
    def __init__(self,master):
        self.frame1 = ttk.Frame(master)
        self.frame1.pack()
        self.frame2 = ttk.Frame(master)
        self.frame2.pack()
        self.label1 = ttk.Label(self.frame1,text = "This program will help you create a webpage!")
        self.label1.grid(row=0,column=0)
        
        
            
        def newWindow1():
            self.window1 = Toplevel(master)
            self.window1.title("Create Page")
            self.frame3 = ttk.Frame(self.window1)
            self.frame3.pack()
            self.frame4 = ttk.Frame(self.window1)
            self.frame4.pack()
            self.label2 = ttk.Label(self.frame3,text = "Please type in the body text here:")
            self.label2.grid(row=0,column=0)
            self.text = Text(self.frame3,width = 50, height= 25)
            self.text.grid(row=1,column=0)
            self.text.config(wrap ='word')

            def getContent():
                content = self.text.get('1.0',END)
                db_web.insert_tab(content)
                self.text.delete(1.0,'end')
                messagebox.showinfo(title ="Info",message = "Matter Saved")
                self.window1.destroy()

            def sendContent():
                matter = self.text.get('1.0',END)
                web_create.main(matter)
                
            self.button2 = ttk.Button(self.frame4, text = "Save Page",command = getContent)
            self.button2.grid(row=0,column=0)
            self.button3 = ttk.Button(self.frame4, text = "Make webpage",command = sendContent)
            self.button3.grid(row=0,column=1)

        def newWindow2():
            self.window2 = Toplevel(master)
            self.window2.title("Saved Contents")
            self.frame5 = ttk.Frame(self.window2)
            self.frame5.pack()
            self.frame6 = ttk.Frame(self.window2)
            self.frame6.pack()
            row = db_web.row_count()
            col = db_web.col_count()
            #print(row,col)
            self.yscroll = ttk.Scrollbar(self.frame5, orient = VERTICAL)
            self.list = Listbox(self.frame5, yscrollcommand = self.yscroll.set,width = 40,height = 6)
            self.yscroll.config(command= self.list.yview)
            self.list.pack(side =LEFT, fill = BOTH)
            self.yscroll.pack(side= RIGHT, fill =Y)
            #self.list.grid(row=0,column=0)
            print(db_web.disp_tab())
            for item in db_web.disp_tab():
                    self.list.insert('end',item)

            def uploadContent():
                self.window3 = Toplevel(master)
                self.window3.title("Requested Page")
                self.frame7 =ttk.Frame(self.window3)
                self.frame7.pack()
                self.frame8 =ttk.Frame(self.window3)
                self.frame8.pack()
                self.text = Text(self.frame7,width = 50, height= 25)
                self.text.grid(row=0,column=0)
                self.text.config(wrap ='word')
                row_val = self.list.curselection()[0]
                
                #print(row_val)
                #print(type(row_val))
                self.text.insert('1.0', db_web.disp_date(row_val))
                def sendContent():
                    matter = self.text.get('1.0',END)
                    web_create.main(matter)
                
                self.button8 = ttk.Button(self.frame8, text = "Make webpage",command = sendContent)
                self.button8.grid(row=0,column=1)
                    
            self.button6 = ttk.Button(self.frame6, text = "Select",command = uploadContent)
            self.button6.grid(row=0,column=1)
            
            

        def close():
            master.destroy()
            
        self.button1 = ttk.Button(self.frame2, text = "Create New Page", command = newWindow1)
        self.button1.grid(row=2,column=0)
        self.button4 = ttk.Button(self.frame2, text = "List Saved Contents", command = newWindow2)
        self.button4.grid(row=2,column=1)
        self.button7 = ttk.Button(self.frame2,text = "Close Application", command = close)
        self.button7.grid(row=3,column=0)
        
            
        





def main():
    root = Tk()
    app = webCreate(root)
    root.mainloop()

if __name__ == "__main__":main()
