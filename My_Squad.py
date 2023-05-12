import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from MySquadManagement import MySquadManagement


class My_Squad(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.data = MySquadManagement.LoadMySquad()

        self.Name = []
        self.Position = []
        self.overall = []
        self.Imp = []
        for r in self.data:
            self.Name.append(r["short_name"])
            self.Position.append(r["player_positions"])
            self.overall.append(r["overall"])
            self.Imp.append(r["player_face_url"])


    def create_widgets(self):
        self.btn_quit = ttk.Button(self, text="Quit", command=root.destroy)
        self.btn_quit.grid(row=2, column=0, pady=10)

    def ST(self):
        ST_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="ST":
                ST_Name.append(self.Name[i])
        return ST_Name

    def RW(self):
        RW_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="RW":
                RW_Name.append(self.Name[i])
        return RW_Name

    def LW(self):
        LW_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="LW":
                LW_Name.append(self.Name[i])
        return LW_Name
    
    def CM(self):
        CM_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="CM":
                CM_Name.append(self.Name[i])
        return CM_Name

    def CDM(self):
        CDM_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:3]=="CDM":
                CDM_Name.append(self.Name[i])
        return CDM_Name
    
    def CDM(self):
        CDM_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:3]=="CDM":
                CDM_Name.append(self.Name[i])
        return CDM_Name
    
    def RB(self):
        RB_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="RB":
                RB_Name.append(self.Name[i])
        return RB_Name
    
    def LB(self):
        LB_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="LB":
                LB_Name.append(self.Name[i])
        return LB_Name
    
    def CB(self):
        CB_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="CB":
                CB_Name.append(self.Name[i])
        return CB_Name

    def GK(self):
        GK_Name = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="GK":
                GK_Name.append(self.Name[i])
        return GK_Name
        