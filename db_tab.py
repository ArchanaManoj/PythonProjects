import sqlite3
import time
import os.path

db = sqlite3.connect('file_info.db')


def create_tab():
    db.execute('create table if not exists file_check_date(ID int, foldername text, file_check text)')

def delete_tab():
    db.execute('drop table file_check_date')
    db.commit()
    
def insert_tab():
    db.execute('insert into file_check_date (ID, foldername, file_check) values(1,"\Personal\Tech Academy\Python\Python Final Drills\files_worked_on","30/01/2016")')
    db.commit()
    
def update_tab():
    t = time.strftime("%x")
    print(t)
    db.execute("update file_check_date set file_check = DATETIME('now','localtime')where ID=1")
    db.commit()
    
def disp_tab():
    cursor = db.execute('select file_check from file_check_date')
    s = str(cursor.fetchone())
    chk_date = s.replace("(","").replace("u","").replace("'","").replace(")","").replace(",","")
    return chk_date

#def main():
    
    #delete_tab()
    #create_tab()
    #insert_tab()
    #update_tab()
    #disp_tab()
    
    
#main()
