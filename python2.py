import db_tab
import time

import wx
import os.path
import shutil





class Frame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File Transfer", size=(500,300))
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()
        
        wx.StaticText(panel, label='This will help you choose modified files that need to be transferred', pos=(100,50))
        wx.StaticText(panel, label='The last check was done on: {}'.format(db_tab.disp_tab()), pos =(100,80))
        
        
        dirDlgBtn1 = wx.Button(panel, label="Choose the Folder to be checked",pos=(150,120))
        dirDlgBtn2 = wx.Button(panel, label="Choose the Folder to move files into", pos =(150,150))
        
        dirDlgBtn1.Bind(wx.EVT_BUTTON, self.folderMod)
        dirDlgBtn2.Bind(wx.EVT_BUTTON, self.folderMove)
        proCeed = wx.Button(panel,label="Proceed", pos=(150,200))
        proCeed.Bind(wx.EVT_BUTTON, self.fileTrans)

    
    
        
    #DirDialog to check modified folder
    def folderMod(self, event):
        global sourceFold
        dlg = wx.DirDialog(self, "Choose a folder:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            
            sourceFold = dlg.GetPath()
            #print "You chose %s" % dlg.GetPath()
        dlg.Destroy()
        
    #DirDialog to check modified folder
    def folderMove(self, event):
        global destFold
        dlg = wx.DirDialog(self, "Choose a folder:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            
            destFold = dlg.GetPath()
            #print "You chose %s" % dlg.GetPath()
        dlg.Destroy()

    
    #Moving files from source to destination
    def fileTrans(self, event):
        global file_es, sourceFold
        print("Source: "+sourceFold)
        print("Destination: "+destFold)
        
        for fil_es in os.listdir(sourceFold):
            
            print "last modified: %s" % time.ctime(os.path.getmtime(sourceFold+"/"+fil_es))
            if (time.time() - os.stat(sourceFold+"/"+fil_es).st_mtime)/(60*60) < 24:
                    shutil.move(sourceFold+"/"+fil_es,destFold)
        #update_tab()
        #Invoking message box
        dlg1 = wx.MessageDialog(self, "File Transfer Successful",'Title',wx.OK)
        dlg1.ShowModal()
        dlg1.Destroy()
        #calling database
        db_tab.update_tab()





def main():
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
    
    
main()
