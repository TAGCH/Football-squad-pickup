import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from MySquadManagement import MySquadManagement


class My_Squad:
    def __init__(self):
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
    
    def Overall(self):
        Overall = []
        Len = len(self.data)
        for i in range(Len):
            Dic = {self.Name[i]:self.overall[i]}
            Overall.append(Dic)
        return Overall
    
    def FW_Overall(self):
        FW = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="ST" or self.Position[i][0:2]=="LW" or self.Position[i][0:2]=="RW" or self.Position[i][0:2]=="CF":
                FW.append(int(self.overall[i]))
        return FW
    
    def MF_Overall(self):
        MF = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="CM" or self.Position[i][0:3]=="CDM" or self.Position[i][0:3]=="CAM" or self.Position[i][0:2]=="LM" or self.Position[i][0:2]=="RM":
                MF.append(int(self.overall[i]))
        return MF
    
    def DF_Overall(self):
        DF = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="CB" or self.Position[i][0:2]=="RB" or self.Position[i][0:2]=="LB":
                DF.append(int(self.overall[i]))
        return DF
    
    def GK_Overall(self):
        GK = []
        Len = len(self.data)
        for i in range(Len):
            if self.Position[i][0:2]=="GK":
                GK.append(int(self.overall[i]))
        return GK
        