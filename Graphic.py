import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from My_Squad import My_Squad
from MySquadManagement import MySquadManagement
import matplotlib.patches as mpatches

class GUIElement:
    def __init__(self, master):
        self.master = master

    def pack(self):
        pass

class MyGUI:
    def __init__(self,master):
        self.master = master
        master.geometry("1500x700")
        master.title("Football11 Squad Pickup")
        master["bg"] = "white"

        self.quit_button = Button(master, "Quit", self.master.quit)
        self.quit_button.pack()

class Button(GUIElement):
    def __init__(self, master, text, command):
        super().__init__(master)
        self.text = text
        self.command = command

    def pack(self):
        self.button = tk.Button(self.master, text=self.text, command=self.command)
        self.button.pack()
    
class App:
    def __init__(self, master):
        self.master = master

        self.data = MySquadManagement.LoadMySquad()

        instance = My_Squad()
        self.ST = instance.ST()
        self.RW = instance.RW()
        self.LW = instance.LW()
        self.CM = instance.CM()
        self.CDM = instance.CDM()
        self.RB = instance.RB()
        self.LB = instance.LB()
        self.CB = instance.CB()
        self.GK = instance.GK()
        self.overall = instance.Overall()
        
        self.Pre_ST_power = 0
        self.Pre_LW_power = 0
        self.Pre_RW_power = 0
        self.Pre_CM_power = 0
        self.Pre_CM2_power = 0
        self.Pre_CDM_power = 0
        self.Pre_RB_power = 0
        self.Pre_LB_power = 0
        self.Pre_CB_power = 0
        self.Pre_CB2_power = 0
        self.Pre_GK_power = 0
        
        self.selected_ST = []
        self.selected_RW = []
        self.selected_LW = []
        self.selected_CM = []
        self.selected_CM2 = []
        self.selected_CDM = []
        self.selected_RB = []
        self.selected_LB = []
        self.selected_CB = []
        self.selected_CB2 = []
        self.selected_GK = []

        self.FW_Overall = 0
        self.MF_Overall = 0
        self.DF_Overall = 0
        self.GK_Overall = 0
        
        self.PreCom_ST_power = 0
        self.PreCom_LW_power = 0
        self.PreCom_RW_power = 0
        self.PreCom_CM_power = 0
        self.PreCom_CM2_power = 0
        self.PreCom_CDM_power = 0
        self.PreCom_RB_power = 0
        self.PreCom_LB_power = 0
        self.PreCom_CB_power = 0
        self.PreCom_CB2_power = 0
        self.PreCom_GK_power = 0

        
        self.selected_Com_ST = []
        self.selected_Com_RW = []
        self.selected_Com_LW = []
        self.selected_Com_CM = []
        self.selected_Com_CM2 = []
        self.selected_Com_CDM = []
        self.selected_Com_RB = []
        self.selected_Com_LB = []
        self.selected_Com_CB = []
        self.selected_Com_CB2 = []
        self.selected_Com_GK = []

        self.FW_Com_Overall = 0
        self.MF_Com_Overall = 0
        self.DF_Com_Overall = 0
        self.GK_Com_Overall = 0
        
        self.Cal_Overall = [self.FW_Overall, self.MF_Overall, self.DF_Overall, self.GK_Overall]
        self.Cal_Com_Overall = [self.FW_Com_Overall, self.MF_Com_Overall, self.DF_Com_Overall, self.GK_Com_Overall]
    
    #Select My Squad
    def Select_ST(self, event):
        selected_value = event.widget.get()
        self.selected_ST.append(selected_value)
        if len(self.selected_ST) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_ST_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall -= self.Pre_ST_power
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_ST_power = int(dictionary[selected_value])
                    print(self.Cal_Overall[0])
        print(self.selected_ST)
        
    def Select_RW(self, event):
        selected_value = event.widget.get()
        self.selected_RW.append(selected_value)
        if len(self.selected_RW) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_RW_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall -= self.Pre_RW_power
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_RW_power = int(dictionary[selected_value])
                    print(self.FW_Overall)
        print(self.selected_RW)
        
    def Select_LW(self, event):
        selected_value = event.widget.get()
        self.selected_LW.append(selected_value)
        if len(self.selected_LW) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_LW_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall -= self.Pre_LW_power
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_LW_power = int(dictionary[selected_value])
                    print(self.FW_Overall)
        print(self.selected_LW)
        
    def Select_CM(self, event):
        selected_value = event.widget.get()
        self.selected_CM.append(selected_value)
        if len(self.selected_CM) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Overall += int(dictionary[selected_value])
                    self.Pre_CM_power=int(dictionary[selected_value])
                    '''
                    self.CM.remove(selected_value)
                    self.select_CM = selected_value
                    '''
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Overall -= self.Pre_CM_power
                    self.MF_Overall += int(dictionary[selected_value])
                    self.Pre_CM_power = int(dictionary[selected_value])
                    '''
                    self.CM.append(self.select_CM)
                    self.CM.remove(selected_value)
                    self.select_CM = selected_value
                    '''
                    print(self.MF_Overall)
        print(self.selected_CM)
        
    def Select_CM2(self, event):
        selected_value = event.widget.get()
        self.selected_CM2.append(selected_value)
        if len(self.selected_CM) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Overall += int(dictionary[selected_value])
                    self.Pre_CM2_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Overall -= self.Pre_CM2_power
                    self.MF_Overall += int(dictionary[selected_value])
                    self.Pre_CM2_power = int(dictionary[selected_value])
                    print(self.MF_Overall)
        print(self.selected_CM2)
        
    def Select_CDM(self, event):
        selected_value = event.widget.get()
        self.selected_CDM.append(selected_value)
        if len(self.selected_CDM) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Overall += int(dictionary[selected_value])
                    self.Pre_CDM_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Overall -= self.Pre_CDM_power
                    self.MF_Overall += int(dictionary[selected_value])
                    self.Pre_CDM_power = int(dictionary[selected_value])
                    print(self.MF_Overall)
        print(self.selected_CDM)
        
    def Select_RB(self, event):
        selected_value = event.widget.get()
        self.selected_RB.append(selected_value)
        if len(self.selected_RB) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_RB_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall -= self.Pre_RB_power
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_RB_power = int(dictionary[selected_value])
                    print(self.DF_Overall)
        print(self.selected_RB)
        
    def Select_LB(self, event):
        selected_value = event.widget.get()
        self.selected_LB.append(selected_value)
        if len(self.selected_LB) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_LB_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall -= self.Pre_LB_power
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_LB_power = int(dictionary[selected_value])
                    print(self.DF_Overall)
        print(self.selected_LB)
        
    def Select_CB(self, event):
        selected_value = event.widget.get()
        self.selected_CB.append(selected_value)
        if len(self.selected_CB) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_CB_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall -= self.Pre_CB_power
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_CB_power = int(dictionary[selected_value])
                    print(self.DF_Overall)
        print(self.selected_CB)
        
    def Select_CB2(self, event):
        selected_value = event.widget.get()
        self.selected_CB2.append(selected_value)
        if len(self.selected_CB2) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_CB2_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Overall -= self.Pre_CB2_power
                    self.DF_Overall += int(dictionary[selected_value])
                    self.Pre_CB2_power = int(dictionary[selected_value])
                    print(self.DF_Overall)
        print(self.selected_CB2)
        
    def Select_GK(self, event):
        selected_value = event.widget.get()
        self.selected_GK.append(selected_value)
        if len(self.selected_GK) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.GK_Overall += int(dictionary[selected_value])
                    self.Pre_GK_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.GK_Overall -= self.Pre_GK_power
                    self.GK_Overall += int(dictionary[selected_value])
                    self.Pre_GK_power = int(dictionary[selected_value])
                    print(self.GK_Overall)
        print(self.selected_GK)
        
    #Select Com
    def Select_Com_ST(self, event):
        selected_value = event.widget.get()
        self.selected_Com_ST.append(selected_value)
        if len(self.selected_Com_ST) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_ST_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Com_Overall -= self.PreCom_ST_power
                    self.FW_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_ST_power = int(dictionary[selected_value])
                    print(self.FW_Com_Overall)
        print(self.selected_Com_ST)
        
    def Select_Com_RW(self, event):
        selected_value = event.widget.get()
        self.selected_Com_RW.append(selected_value)
        if len(self.selected_Com_RW) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_RW_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Com_Overall -= self.PreCom_RW_power
                    self.FW_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_RW_power = int(dictionary[selected_value])
                    print(self.FW_Com_Overall)
        print(self.selected_Com_RW)
        
    def Select_Com_LW(self, event):
        selected_value = event.widget.get()
        self.selected_LW.append(selected_value)
        if len(self.selected_Com_LW) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_LW_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Com_Overall -= self.PreCom_LW_power
                    self.FW_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_LW_power = int(dictionary[selected_value])
                    print(self.FW_Com_Overall)
        print(self.selected_Com_LW)
        
    def Select_Com_CM(self, event):
        selected_value = event.widget.get()
        self.selected_Com_CM.append(selected_value)
        if len(self.selected_Com_CM) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CM_power=int(dictionary[selected_value])
                    '''
                    self.CM.remove(selected_value)
                    self.select_CM = selected_value
                    '''
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Com_Overall -= self.PreCom_CM_power
                    self.MF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CM_power = int(dictionary[selected_value])
                    '''
                    self.CM.append(self.select_CM)
                    self.CM.remove(selected_value)
                    self.select_CM = selected_value
                    '''
                    print(self.MF_Com_Overall)
        print(self.selected_Com_CM)
        
    def Select_Com_CM2(self, event):
        selected_value = event.widget.get()
        self.selected_Com_CM2.append(selected_value)
        if len(self.selected_Com_CM) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CM2_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Com_Overall -= self.PreCom_CM2_power
                    self.MF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CM2_power = int(dictionary[selected_value])
                    print(self.MF_Com_Overall)
        print(self.selected_Com_CM2)
        
    def Select_Com_CDM(self, event):
        selected_value = event.widget.get()
        self.selected_Com_CDM.append(selected_value)
        if len(self.selected_Com_CDM) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CDM_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.MF_Com_Overall -= self.PreCom_CDM_power
                    self.MF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CDM_power = int(dictionary[selected_value])
                    print(self.MF_Com_Overall)
        print(self.selected_Com_CDM)
        
    def Select_Com_RB(self, event):
        selected_value = event.widget.get()
        self.selected_Com_RB.append(selected_value)
        if len(self.selected_Com_RB) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_RB_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall -= self.PreCom_RB_power
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_RB_power = int(dictionary[selected_value])
                    print(self.DF_Com_Overall)
        print(self.selected_Com_RB)
        
    def Select_Com_LB(self, event):
        selected_value = event.widget.get()
        self.selected_Com_LB.append(selected_value)
        if len(self.selected_Com_LB) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_LB_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall -= self.PreCom_LB_power
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_LB_power = int(dictionary[selected_value])
                    print(self.DF_Com_Overall)
        print(self.selected_Com_LB)
        
    def Select_Com_CB(self, event):
        selected_value = event.widget.get()
        self.selected_Com_CB.append(selected_value)
        if len(self.selected_Com_CB) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CB_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall -= self.PreCom_CB_power
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CB_power = int(dictionary[selected_value])
                    print(self.DF_Com_Overall)
        print(self.selected_Com_CB)
        
    def Select_Com_CB2(self, event):
        selected_value = event.widget.get()
        self.selected_Com_CB2.append(selected_value)
        if len(self.selected_Com_CB2) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CB2_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.DF_Com_Overall -= self.PreCom_CB2_power
                    self.DF_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_CB2_power = int(dictionary[selected_value])
                    print(self.DF_Com_Overall)
        print(self.selected_Com_CB2)
        
    def Select_Com_GK(self, event):
        selected_value = event.widget.get()
        self.selected_Com_GK.append(selected_value)
        if len(self.selected_Com_GK) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.GK_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_GK_power=int(dictionary[selected_value])
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.GK_Com_Overall -= self.PreCom_GK_power
                    self.GK_Com_Overall += int(dictionary[selected_value])
                    self.PreCom_GK_power = int(dictionary[selected_value])
                    print(self.GK_Com_Overall)
        print(self.selected_Com_GK)
        
    #Create widgets    
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=1600, height=650, bg = 'seagreen', highlightbackground= "seagreen")
        self.canvas.pack()
        
        self.canvas.create_text(225, 50, text="My Squad", font=('Helvetica 24 bold'))
        self.canvas.pack()

        #ST
        self.ST_Box = ttk.Combobox(self.master, values=self.ST,width=10)
        self.ST_Box.bind("<<ComboboxSelected>>", self.Select_ST)
        self.canvas.create_window(225, 150, window=self.ST_Box)

        #LW
        self.LW_Box = ttk.Combobox(self.master, values=self.LW, width=10)
        self.LW_Box.bind("<<ComboboxSelected>>", self.Select_LW)
        self.canvas.create_window(65, 195, window=self.LW_Box)

        #RW
        self.RW_Box = ttk.Combobox(self.master, values=self.RW, width=10)
        self.RW_Box.bind("<<ComboboxSelected>>", self.Select_RW)
        self.canvas.create_window(385, 195, window=self.RW_Box)

        #CM
        self.CM_Box = ttk.Combobox(self.master, values=self.CM, width=10)
        self.CM_Box.bind("<<ComboboxSelected>>", self.Select_CM)
        self.canvas.create_window(125, 300, window=self.CM_Box)

        #CM
        self.CM2_Box = ttk.Combobox(self.master, values=self.CM, width=10)
        self.CM2_Box.bind("<<ComboboxSelected>>", self.Select_CM2)
        self.canvas.create_window(325, 300, window=self.CM2_Box)

        #CDM
        self.CDM_Box = ttk.Combobox(self.master, values=self.CDM, width=10)
        self.CDM_Box.bind("<<ComboboxSelected>>", self.Select_CDM)
        self.canvas.create_window(225, 400, window=self.CDM_Box)

        #LB
        self.LB_Box = ttk.Combobox(self.master, values=self.LB, width=10)
        self.LB_Box.bind("<<ComboboxSelected>>", self.Select_LB)
        self.canvas.create_window(75, 425, window=self.LB_Box)

        #RB
        self.RB_Box = ttk.Combobox(self.master, values=self.RB, width=10)
        self.RB_Box.bind("<<ComboboxSelected>>", self.Select_RB)
        self.canvas.create_window(375, 425, window=self.RB_Box)

        #CB
        self.CB_Box = ttk.Combobox(self.master, values=self.CB, width=10)
        self.CB_Box.bind("<<ComboboxSelected>>", self.Select_CB)
        self.canvas.create_window(150, 500, window=self.CB_Box)

        #CB
        self.CB2_Box = ttk.Combobox(self.master, values=self.CB, width=10)
        self.CB2_Box.bind("<<ComboboxSelected>>", self.Select_CB2)
        self.canvas.create_window(300, 500, window=self.CB2_Box)

        #GK
        self.GK_Box = ttk.Combobox(self.master, values=self.GK, width=10)
        self.GK_Box.bind("<<ComboboxSelected>>", self.Select_GK)
        self.canvas.create_window(225, 600, window=self.GK_Box)

        #Competitor
        self.canvas.create_text(1275, 50, text="Competitor Squad", font=('Helvetica 24 bold'))
        self.canvas.pack()
        
        #FW
        self.ST_Com_Box = ttk.Combobox(self.master, values=self.ST, width=10)
        self.ST_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_ST)
        self.canvas.create_window(1275, 150, window=self.ST_Com_Box)

        #LW
        self.LW_Com_Box = ttk.Combobox(self.master, values=self.LW, width=10)
        self.LW_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_LW)
        self.canvas.create_window(1115, 195, window=self.LW_Com_Box)

        #RW
        self.RW_Com_Box = ttk.Combobox(self.master, values=self.RW, width=10)
        self.RW_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_RW)
        self.canvas.create_window(1435, 195, window=self.RW_Com_Box)

        #CM
        self.CM_Com_Box = ttk.Combobox(self.master, values=self.CM, width=10)
        self.CM_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_CM)
        self.canvas.create_window(1375, 300, window=self.CM_Com_Box)

        #CM
        self.CM2_Com_Box = ttk.Combobox(self.master, values=self.CM, width=10)
        self.CM2_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_CM2)
        self.canvas.create_window(1175, 300, window=self.CM2_Com_Box)

        #CDM
        self.CDM_Com_Box = ttk.Combobox(self.master, values=self.CDM, width=10)
        self.CDM_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_CDM)
        self.canvas.create_window(1275, 400, window=self.CDM_Com_Box)

        #LB
        self.LB_Com_Box = ttk.Combobox(self.master, values=self.LB, width=10)
        self.LB_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_LB)
        self.canvas.create_window(1125, 425, window=self.LB_Com_Box)

        #RB
        self.RB_Com_Box = ttk.Combobox(self.master, values=self.RB, width=10)
        self.RB_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_RB)
        self.canvas.create_window(1425, 425, window=self.RB_Com_Box)

        #CB
        self.CB_Com_Box = ttk.Combobox(self.master, values=self.CB, width=10)
        self.CB_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_CB)
        self.canvas.create_window(1350, 500, window=self.CB_Com_Box)

        #CB
        self.CB2_Com_Box = ttk.Combobox(self.master, values=self.CB, width=10)
        self.CB2_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_CB2)
        self.canvas.create_window(1200, 500, window=self.CB2_Com_Box)

        #GK
        self.GK_Com_Box = ttk.Combobox(self.master, values=self.GK, width=10)
        self.GK_Com_Box.bind("<<ComboboxSelected>>", self.Select_Com_GK)
        self.canvas.create_window(1275, 600, window=self.GK_Com_Box)
        
        self.canvas.create_rectangle(450, 0, 1050, 900, fill='white')
        
        #self.variable_values1 = self.Cal_Overall()
        #self.variable_values2 = self.Cal_Com_Overall()
        self.variable_values1 = [self.Cal_Overall[0],self.Cal_Overall[1],self.Cal_Overall[2],self.Cal_Overall[3]]
        self.variable_values2 = [self.Cal_Com_Overall[0],self.Cal_Com_Overall[1],self.Cal_Com_Overall[2],self.Cal_Com_Overall[3]]

        # Create a radar graph
        self.fig = Figure(figsize=(4, 4))
        self.ax = self.fig.add_subplot(222, polar=True)
        self.figure_canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.figure_canvas.get_tk_widget().place(x=465, y=370)

        self.plot_radar_graph()
            
        update_button = tk.Button(self.master, text="Compare", command=self.update_value)
        update_button.place(x=720, y=600)

        #self.canvas.create_oval(50, 50, 150, 150, fill='white')

    def plot_radar_graph(self):
        self.ax.clear()

        # Define the variables and their values
        categories = ['Attack', 'Passing', 'Defend', 'Protect']
        values1 = self.variable_values1.copy()
        values2 = self.variable_values2.copy()

        # Duplicate the first value to complete the loop
        values1.append(values1[0])
        values2.append(values2[0])

        # Calculate angles for each variable
        angles = [n / float(len(categories)) * 2 * 3.14159 for n in range(len(categories))]
        angles += angles[:1]

        red_line = self.ax.plot(angles, values1, marker='o', linestyle='-', color='red', label='My Squad')
        self.ax.fill(angles, values1, facecolor='red', alpha=0.25)

        yellow_line = self.ax.plot(angles, values2, marker='o', linestyle='-', color='yellow', label='Com Squad')
        self.ax.fill(angles, values2, facecolor='yellow', alpha=0.25)
        self.ax.legend(handles=[red_line[0], yellow_line[0]], loc='upper left', bbox_to_anchor=(-0.7, 1), fontsize='xx-small')

        self.ax.set_xticks(angles[:-1])
        self.ax.set_xticklabels(categories)

        self.ax.set_yticks([25, 50, 75, 100])

        self.ax.set_title('Overall Compare', size=10)
        self.ax.set_facecolor('lightgray')

        self.figure_canvas.draw()

    def update_value(self):
        self.variable_values1[0]=self.FW_Overall//3
        self.variable_values1[1]=self.MF_Overall//3
        self.variable_values1[2]=self.DF_Overall//4
        self.variable_values1[3]=self.GK_Overall
        self.variable_values2[0]=self.FW_Com_Overall//3
        self.variable_values2[1]=self.MF_Com_Overall//3
        self.variable_values2[2]=self.DF_Com_Overall//4
        self.variable_values2[3]=self.GK_Com_Overall
        self.plot_radar_graph()