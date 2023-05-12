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
        
    def Select_ST(self, event):
        selected_value = event.widget.get()
        self.selected_ST.append(selected_value)
        if len(self.selected_ST) <= 1:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_ST_power=int(dictionary[selected_value])
                    print(self.FW_Overall)
        else:
            for dictionary in self.overall:
                if selected_value in dictionary:
                    self.FW_Overall -= self.Pre_ST_power
                    self.FW_Overall += int(dictionary[selected_value])
                    self.Pre_ST_power = int(dictionary[selected_value])
                    print(self.FW_Overall)
        print(self.selected_ST)
        
    def Select_RW(self, event):
        selected_value = event.widget.get()
        self.selected_RW.append(selected_value)
        print(self.selected_RW)
    def Select_LW(self):
        pass
    def Select_CM(self):
        pass
    def Select_CM2(self):
        pass
    def Select_CDM(self):
        pass
    def Select_RB(self):
        pass
    def Select_LB(self):
        pass
    def Select_CB(self):
        pass
    def Select_CB2(self):
        pass
    def Select_GK(self):
        pass
    
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=1600, height=650, bg = 'seagreen', highlightbackground= "seagreen")
        self.canvas.pack()

        choices = ['GB', 'MB', 'KB', 'a', 'b', 'c', 'd', 'e']
        variable = tk.StringVar(self.master)
        variable.set('GB')

        self.canvas.create_text(225, 50, text="My Squad", font=('Helvetica 24 bold'))
        self.canvas.pack()

        #ST
        self.ST_Box = ttk.Combobox(self.master, values=self.ST,width=10)
        self.ST_Box.bind("<<ComboboxSelected>>", self.Select_ST)
        self.canvas.create_window(225, 150, window=self.ST_Box)

        #LW
        self.LW_Box = ttk.Combobox(self.master, values=self.LW, width=10)
        self.canvas.create_window(65, 195, window=self.LW_Box)

        #RW
        self.RW_Box = ttk.Combobox(self.master, values=self.RW, width=10)
        self.canvas.create_window(385, 195, window=self.RW_Box)

        #CM
        self.CM_Box = ttk.Combobox(self.master, values=self.CM, width=10)
        self.canvas.create_window(125, 300, window=self.CM_Box)

        #CM
        self.CM2_Box = ttk.Combobox(self.master, values=self.CM, width=10)
        self.canvas.create_window(325, 300, window=self.CM2_Box)

        #CDM
        self.CDM_Box = ttk.Combobox(self.master, values=self.CDM, width=10)
        self.canvas.create_window(225, 400, window=self.CDM_Box)

        #LB
        self.LB_Box = ttk.Combobox(self.master, values=self.LB, width=10)
        self.canvas.create_window(75, 425, window=self.LB_Box)

        #RB
        self.RB_Box = ttk.Combobox(self.master, values=self.RB, width=10)
        self.canvas.create_window(375, 425, window=self.RB_Box)

        #CB
        self.CB_Box = ttk.Combobox(self.master, values=self.CB, width=10)
        self.canvas.create_window(150, 500, window=self.CB_Box)

        #CB
        self.CB2_Box = ttk.Combobox(self.master, values=self.CB, width=10)
        self.canvas.create_window(300, 500, window=self.CB2_Box)

        #GK
        self.GK_Box = ttk.Combobox(self.master, values=self.GK, width=10)
        self.canvas.create_window(225, 600, window=self.GK_Box)

        #Competitor
        self.canvas.create_text(1275, 50, text="Competitor Squad", font=('Helvetica 24 bold'))
        self.canvas.pack()
        #FW
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1275, 150, window=self.w)

        #LW
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1435, 195, window=self.w)

        #RW
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1115, 195, window=self.w)

        #CM
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1375, 300, window=self.w)

        #CM
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1175, 300, window=self.w)

        #CDM
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1275, 400, window=self.w)

        ##LB
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1425, 425, window=self.w)

        #RB
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1125, 425, window=self.w)

        #CB
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1350, 500, window=self.w)

        #CB
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1200, 500, window=self.w)

        #GK
        self.w = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(1275, 600, window=self.w)
        
        self.canvas.create_rectangle(450, 0, 1050, 900, fill='white')

        #self.canvas.create_oval(50, 50, 150, 150, fill='white')
        