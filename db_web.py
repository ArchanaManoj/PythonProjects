import sqlite3
import os.path
import time

db = sqlite3.connect('web_page.db')

def create_tab():
    db.execute('create table if not exists web_info(ID INTEGER PRIMARY KEY AUTOINCREMENT , web_content TEXT, mod_date TEXT)')

def delete_tab():
    db.execute('drop table web_info')
    db.commit()
    
def insert_tab(web):
    t = time.strftime("%x %I:%M:%S %p")
    db.execute('insert into web_info (web_content, mod_date) values(?,?)',(web,t))
    #db.execute('insert into web_info (ID, web_content, mod_date) values(?, ?,?)',(1,"More Sample Text",t))
    db.commit()
    
def update_tab(web):
    t = time.strftime("%x")
    #web = "New Content"
    #print(t)
    db.execute("update web_info set web_content = ? , mod_date = ? where ID =1",(web,t))
    db.commit()
    
def disp_tab():
    cursor = db.execute('select  ID, mod_date from web_info')
    #s = str(cursor.fetchall())
    s = cursor.fetchall()
    #web_pg = s.replace("(","").replace(",","").replace(")","").replace("'","").replace("\n","")
    #print(s)
    return s
def row_count():
    cursor = db.execute('select count(*) from web_info')
    row = cursor.fetchone()[0]
    '''r = cursor.fetchall()
    r_s = str(r)
    row = r_s.replace("(","").replace(")","").replace(",","")'''
    #print(row)
    return row

def col_count():
    cursor = db.execute('pragma table_info(web_info)')
    col = len(cursor.fetchall())
    #print(col)
    return col
def disp_date(val):
    
    cursor = db.execute('select web_content from web_info where ID =?',(val))
    s=str(cursor.fetchone())
    web_pg = s.replace("(","").replace(",","").replace(")","").replace("'","").replace("\\n","")
    return web_pg

#def main():
    #global web
    #web = "testing"
    #delete_tab()
    #create_tab()
    #insert_tab()
    #update_tab()
    #update_tab(web)
    #disp_tab()
    #col_count()
    #row_count()
#main()
               
