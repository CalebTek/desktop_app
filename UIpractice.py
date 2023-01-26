# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:09:24 2020

@author: LFC SOKOTO STUDIO
"""


from tkinter import *
from tkinter import ttk
from tkinter import Menu
from PIL import Image, ImageTk
import os

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("CahabaCreek CahabaWorks")
        self.minsize(width = 800, height = 600)
        
        ## create a window canvas
        
        
        ### include all other widgets
        self.createMenu()
        self.createTools()
        #self.createButtons()
        self.createPartition()
        #self.createRadios()
        self.sideNavi()
        self.upperNavi()
        self.lowerNavi()
        
    def createMenu(self):
        #self.menuCanvas = Canvas(self)
        #self.menuCanvas.pack(side = "right")
        ## creating a menu bar
        self.menu_bar = Menu(self)
        self.config(menu = self.menu_bar)
        
        

        ## create menu and add menu items
        self.menus = ["File", "View", "Reports", "Tools", "Help"]
        
        self.file_menu = ["New", "Open", "Save", "Save As", "Print","Print Preview", "Exit"]
        self.file_menu_short = ["Ctrl+N", "Ctrl+O", "Ctrl+S",
                                "Ctrl+Shift+S", "Ctrl+P", "", 'Alt+F4']
        
        self.view_menu = ["Copy", "Cut", "Paste", "Select All", "Preferences", "Tools"]
        self.view_menu_short = ["Ctrl+C", "Ctrl+X", "Ctrl+V", "Ctrl+A", "Shift+P", ""]
        
        ## add file menu items and shortcuts
        file_menu = [0]*len(self.file_menu)
        for i in range(len(self.file_menu)):
            file_menu[i] = "{:<15s} {:<15s}".format(self.file_menu[i], self.file_menu_short[i])
        
        ## add view menu items and shortcuts
        view_menu = [0]*len(self.view_menu)
        
        for i in range(len(self.view_menu)):
            view_menu[i] = "{:<15s} {:<15s}".format(self.view_menu[i], self.view_menu_short[i])
        
        menu_items = [0]*len(self.menus)
        
        ## create menu items
        for i in range(len(self.menus)):
            menu_items[i] = Menu(self.menu_bar, tearoff = 0)
        
        ## create file menu items
        for i in range(len(self.file_menu)):
            menu_items[0].add_command(label=file_menu[i])
            menu_items[0].add_separator()

        ## create view menu items
        for i in range(len(self.view_menu)):
            menu_items[1].add_command(label=view_menu[i])
            menu_items[1].add_separator()            
   
        
        for i in range(len(self.menus)):
            self.menu_bar.add_cascade(label = self.menus[i], menu = menu_items[i])
        
        '''
        long proress for the above code
        ## create menu and add menu items
        self.menus = ["File", "View", "Reports", "Tools", "Help"]
        self.file_menu = Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "New")
        self.menu_bar.add_cascade(label = self.menus[0], menu = self.file_menu)
        '''
    '''
    def createButtons(self, butText = None, butImage = None, frame = None,
                      height = None, width = None, bg = None, font = None):
        ## create buttons
        if butText != None and butImage == None:
            butLen = len(butText)
            buttons = [0]*butLen
            for i in range(butLen):
                buttons[i] = Button(frame,text = butText[i], height = height, width = width,
                                    bg = bg, font = font)
        elif butImage != None and butText == None:
            butLen = len(butImage)
            buttons = [0]*butLen
            for i in range(butLen):
                buttons[i] = Button(frame, image = butImage[i], height = height, width = width,
                                    bg = bg, font = font)
        else:
            errorMSG = "Button text or image cannot be empty"
        

       
        #for i in range(butLen):
        #    buttons[i] = Button(self, text = butText[i])
            
       
        return(buttons)
     ''' 
    
    '''
    def createRadios(self, radText = None,frame = None, font = None,
                     radVar = None, radValue = None,
                     height = None, width = None, bg = None):
        ## create buttons
        if radText != None and radValue != None:
            radLen = len(radText)
            radios = [0]*radLen
            for i in range(radLen):
                radios[i] = Radiobutton(frame, text = radText[i], font = font,
                                        var = radVar, value = radValue[i],
                                        height = height, width = width, bg = bg)
        else:
            errorMSG = "Radio text or value cannot be empty"
            
        return(radios)
      '''  

    
    def createTools(self):
        
        ## creating frame to hold tools
        self.toolFrame = Frame(self)
        self.toolFrame.place(relx = 0, rely = 0)
        
        '''
        ## create list of icons in the image directory
        img_list = os.listdir("./images/UIpractice/img/")
        img = [("./images/UIpractice/img/"+img_list[i]) for i in range(len(img_list))]
        
        butImg = [PhotoImage((img[i])) for i in range(len(img))]
        '''
        
        #image = butImg[i]
        #buttons = [0] * len(butImg)
        ## use text instead  of icon for now
        butText = ["Icon_" + str(i) for i in range(1,16)]
        buttons = [0] * len(butText)
        for i in range(len(buttons)):
            buttons[i] = ttk.Button(self.toolFrame, text = butText[i],
                                    width = 8)
            buttons[i].pack(side = "left", padx = 4, pady =4)
        
        
        '''
        ## create button
        buttons = self.createButtons(frame = self.toolFrame, butImage = butImg, width = 40, height = 30)
        for i in range(len(buttons)):
            buttons[i].pack(side = "left")
        '''

        ''' 
        #buttons = self.createButtons(butText = ["Submit", "Cancel"], frame = self.toolFrame)
        #[buttons[i].pack(side = "left") for i in range(len(buttons))]
        
        #buttons = self.createButtons(butText = ["Submit", "Cancel"], frame = self.toolFrame)
        #[buttons[i].pack(side = "top") for i in range(len(buttons))] 
        '''
    '''
    def createTools(self):
        self.toolFrame = Frame(self)
        self.toolFrame.pack(side = "top")
        img = PhotoImage("./images/UIpractice/img/copy.png")
        self.button = Button(self.toolFrame, image = img, height = 50, width = 50)
        self.button.pack(side = "left")
    '''
    
    def createPartition(self):
        ## create the partition window
        self.canvas = Canvas(self, bg = "green")
        self.canvas.place(relx = 0, rely = 0.05, relwidth = 1, relheight = 0.95)
        
        ## create side navigation
        self.sideFrame = Frame(self.canvas, bg = "red")
        self.sideFrame.place(relx = 0.002, rely = 0.003, relheight = 0.994, relwidth = 0.15)
        self.upperFrame = Frame(self.canvas, bg = "blue")
        self.upperFrame.place(relx = 0.152, rely = 0.003, relheight = 0.784, relwidth = 0.848)
        self.lowerFrame = Frame(self.canvas, bg = "yellow")
        self.lowerFrame.place(relx = 0.152, rely = 0.786, relheight = 0.994, relwidth = 0.848)
    
    '''
    def createTabs(self, frame = None, tabName = None):
        ## create Tabs (notebooks)
        tabCtrl = ttk.Notebook(frame)
        #childFrame = tabCtrl , childFrame = None and childFrame != None 
        tabFrame = Frame(tabCtrl)
        if frame != None and tabName != None:
            if isinstance(tabName, list):
                tabLen = len(tabName)
            else:
                tabLen = 1
        
        for i in range(tabLen):
            ## create tabs in tab control
            tabCtrl.add(tabFrame, text = tabName[i])
            #tab[i].pack(expand = 1, fill = "both")
        
        return(tabCtrl)
      '''  
    
    def sideNavi(self):
        sideTab = ttk.Notebook(self.sideFrame)
        memberTab = Frame(sideTab, bg = "blue")
        ## trying other tabs
        #memberTab2 = ttk.Frame(sideTab)
        sideTab.add(memberTab, text = "Modules")
        #sideTab.add(memberTab2, text = "Modules Try")
        sideTab.pack(expand = 1, fill = "both")
        
        upperNavi = Frame(memberTab)
        upperNavi.place(relx = 0.01, rely = 0.01,relheight = 0.498, 
                        relwidth = 0.98)
        
        ## Members label
        membersLabell = Label(upperNavi, text = "Members")
        membersLabell.pack(side = "top", anchor = "w")
        
        radVar = IntVar()
        radVar.set(0)
        radText = ["Phone Book", "Member Cards", "Member List", "Houseolds"]
        
        radios = [0]*len(radText)
        for i in range(len(radText)):
            radios[i] = Radiobutton(upperNavi, var = radVar, text = radText[i],
                                    value = radText[i])
            radios[i].pack(side = "top", anchor = "w")
        '''
        radios = self.createRadios(frame = upperNavi,radVar = var,
                                   radText = text, radValue = text)
        for i in range(len(radios)):
            radios[i].pack(side = "top", anchor = "w")
        '''
        
        lowerNavi = Frame(memberTab)
        lowerNavi.place(rely = 0.51, relx = 0.01, relheight = 0.496, relwidth = 0.98)
        
        ## create members attributes button
        membersAttrItems = ["Members", "Groups", "Contributors", "Financials"]
        
        buttons = [0]*len(membersAttrItems)
        
        for i in range(len(buttons)):
            buttons[i] = ttk.Button(lowerNavi, text = membersAttrItems[i],
                                width = 20)
            buttons[i].pack(side = "top", pady = 3)
        '''
        buttons = self.createButtons(frame = lowerNavi, butText = membersAttrItems, width = 15)
        for i in range(len(buttons)):
            buttons[i].pack(side = "top", pady = 3)
        '''
            
    def upperNavi(self):
        tab_names = ["Phone Book", "Member Cards", "Member List", "Houseolds"]
         
        tabCtrl = ttk.Notebook(self.upperFrame)
        
        ## create Tabs holder
        tabFrame = [0]*len(tab_names)
        for i in range(len(tab_names)):
            tabFrame[i] = Frame(tabCtrl)
        
        # Creating member
        
        ## create Member Cards widgets
       
        '''
        label = Label(tabFrame[0], text = "This is {} Tab".format(tab_names[0]))
        label.pack(side = "left")
        label = Label(tabFrame[1], text = "This is {} Tab".format(tab_names[1]))
        label.pack(side = "left") 
        label = Label(tabFrame[2], text = "This is {} Tab".format(tab_names[2]))
        label.pack(side = "left")
        label = Label(tabFrame[3], text = "This is {} Tab".format(tab_names[3]))
        label.pack(side = "left")
        '''

        label = [0]*len(tab_names)
        for i in range(len(tab_names)):
            label[i] = Label(tabFrame[i], text = "This is {} Tab".format(tab_names[i]))
            label[i].pack(side="left")

        
        ## add Tabs
        for i in range(len(tab_names)):
            tabCtrl.add(tabFrame[i], text = tab_names[i])
            tabCtrl.pack(expand = 1, fill = "both")
        
    def lowerNavi(self):
        tab_names = ["Household", "Notes", "Custom Fields", "Contributions",
                     "Pledges", "Small Groups", "Visits"]
        '''
        tabs = self.createTabs(frame = self.lowerFrame,
                          tabName = tab_names)
        for i in range(len(tabs)):
            tabs[i].pack(expand = 1, fill = "both")
        '''
        tabCtrl = ttk.Notebook(self.lowerFrame)
        
        ## create Tabs
        tabFrame = [0]*len(tab_names)
        for i in range(len(tab_names)):
            tabFrame[i] = Frame(tabCtrl)


        label = [0]*len(tab_names)
        for i in range(len(tab_names)):
            label[i] = Label(tabFrame[i], text = "This is {} Tab".format(tab_names[i]))
            label[i].pack(side="top")

   
        '''
        label = Label(tabFrame[0], text = "This is {} Tab".format(tab_names[0]))
        label.pack(side = "top")
        '''
        
        ## add Tabs
        for i in range(len(tab_names)):
            tabCtrl.add(tabFrame[i], text = tab_names[i])
            tabCtrl.pack(expand = 1, fill = "both")
        


if __name__ == "__main__":
    app = Root()
    app.mainloop()        
    
    
    
'''
butFrame = Frame()
butFrame.pack(side = "top")        

def createButtons(frame = None, butText = None, butImage = None):
    ## create buttons
    if butText != None:
        butLen = len(butText)
        buttons = [0]*butLen
        for i in range(butLen):
            buttons[i] = Button(text = butText[i])
    elif butImage != None:
        butLen = len(butImage)
        buttons = [0]*butLen
        for i in range(butLen):
            buttons[i] = Button(image = butImage[i])
    else:
        errorMSG = "Button text or image cannot be empty"
    return(buttons)
        
buttons = createButtons(butText = ["Submit", "Cancel"], frame = butFrame)
for i in range(len(buttons)):
    buttons[i].pack(side = "left")
'''