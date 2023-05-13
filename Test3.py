import tkinter as tk
from tkinter import ttk, Scale
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class YourClassName:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=1600, height=650, bg='seagreen', highlightbackground="seagreen")
        self.canvas.pack()

        self.canvas.create_text(225, 50, text="My Squad", font=('Helvetica 24 bold'))
        self.canvas.create_rectangle(450, 0, 1050, 900, fill='white')

        # Define the initial values for the variables
        self.dataset1_values = [0.6, 0.8, 0.4, 0.9]
        self.dataset2_values = [0.2, 0.5, 0.7, 0.3]

        # Create a radar graph
        self.fig = Figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111, polar=True)

        # Create a FigureCanvasTkAgg instance to draw the graph on the canvas
        self.figure_canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.figure_canvas.get_tk_widget().place(x=480, y=100)

        # Initialize the radar graph with initial values
        self.plot_radar_graph()

        # Create Scale widgets to adjust the values
        self.scales = []
        for i in range(len(self.dataset1_values)):
            scale = Scale(self.master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL,
                          command=lambda value, index=i: self.update_value(value, index))
            scale.set(self.dataset1_values[i])
            scale.place(x=500, y=200 + 50 * i)
            self.scales.append(scale)

        # Create a combo box to select the dataset
        self.combo_box = ttk.Combobox(self.master, values=["Dataset 1", "Dataset 2"], state="readonly",
                                      command=self.on_combo_box_select)
        self.combo_box.current(0)
        self.combo_box.place(x=500, y=100)

    def plot_radar_graph(self):
        self.ax.clear()

        # Define the variables and their values based on the selected dataset
        if self.combo_box.get() == "Dataset 1":
            categories = ['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4']
            values = self.dataset1_values.copy()
        else:
            categories = ['Variable A', 'Variable B', 'Variable C', 'Variable D']
            values = self.dataset2_values.copy()

        # Duplicate the first value to complete the loop
        values.append(values[0])

        # Calculate angles for each variable
        angles = [n / float(len(categories)) * 2 * 3.14159 for n in range(len(categories))]
        angles += angles[:1]

        # Plot the radar graph
        self.ax.plot(angles, values, marker='o', linestyle='-', color='red')
        self.ax.fill(angles, values, facecolor='red', alpha=0.25)

        # Set the labels for each variable
        self.ax.set_xticks(angles[:-1])
        self.ax.set_xticklabels(categories)

        # Set the limit for the radial axis
        self.ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
            # Set the title for the radar graph
        self.ax.set_title('Radar Graph', size=16)

        # Redraw the canvas
        self.figure_canvas.draw()

    def update_value(self, value, index):
        if self.combo_box.get() == "Dataset 1":
            self.dataset1_values[index] = float(value)
        else:
            self.dataset2_values[index] = float(value)
        self.plot_radar_graph()

    def on_combo_box_select(self, event):
        self.plot_radar_graph()

root = tk.Tk()
app = YourClassName(root)
app.create_widgets()
root.mainloop()