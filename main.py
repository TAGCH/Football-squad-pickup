from typing import Final
import tkinter as tk
from Graphic import App, MyGUI

SCREEN_WIDTH: Final = 1200
SCREEN_HEIGHT: Final = 700

if __name__ == "__main__":
    root = tk.Tk()
    pick = App(root)
    pick.create_widgets()
    gui = MyGUI(root)
    root.mainloop()