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

        self.ST = My_Squad.ST(self)
        self.RW = My_Squad.RW(self)
        self.LW = My_Squad.LW(self)
        self.CM = My_Squad.CM(self)
        self.CDM = My_Squad.CDM(self)
        self.RB = My_Squad.RB(self)
        self.LB = My_Squad.LB(self)
        self.CB = My_Squad.CB(self)
        self.GK = My_Squad.GK(self)

        self.FW_Overall = 0
        self.MF_Overall = 0
        self.DF_Overall = 0
        self.GK_Overall = 0

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=1600, height=650, bg = 'seagreen', highlightbackground= "seagreen")
        self.canvas.pack()

        choices = ['GB', 'MB', 'KB', 'a', 'b', 'c', 'd', 'e']
        variable = tk.StringVar(self.master)
        variable.set('GB')

        self.canvas.create_text(225, 50, text="My Squad", font=('Helvetica 24 bold'))
        self.canvas.pack()

        #ST
        self.ST_Box = ttk.Combobox(self.master, values=self.ST, textvariable=variable, width=10)
        self.canvas.create_window(225, 150, window=self.ST_Box)

        #LW
        self.LW_Box = ttk.Combobox(self.master, values=self.LW, textvariable=variable, width=10)
        self.canvas.create_window(65, 195, window=self.LW_Box)

        #RW
        self.RW_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(385, 195, window=self.RW_Box)

        #CM
        self.CM_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(125, 300, window=self.CM_Box)

        #CM
        self.CM2_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(325, 300, window=self.CM2_Box)

        #CDM
        self.CDM_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(225, 400, window=self.CDM_Box)

        #LB
        self.LB_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(75, 425, window=self.LB_Box)

        #RB
        self.RB_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(375, 425, window=self.RB_Box)

        #CB
        self.CB_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(150, 500, window=self.CB_Box)

        #CB
        self.CB2_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
        self.canvas.create_window(300, 500, window=self.CB2_Box)

        #GK
        self.GK_Box = ttk.Combobox(self.master, values=choices, textvariable=variable, width=10)
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