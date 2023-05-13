import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches

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
        self.dataset_values = [0.6, 0.8, 0.4, 0.9]

        # Create a radar graph
        self.fig = Figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111, polar=True)

        # Create a FigureCanvasTkAgg instance to draw the graph on the canvas
        self.figure_canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.figure_canvas.get_tk_widget().place(x=480, y=100)

        # Initialize the radar graph with initial values
        self.plot_radar_graph()

        # Create Entry widgets to enter the values
        self.entries = []
        for i in range(len(self.dataset_values)):
            entry = tk.Entry(self.master, width=5)
            entry.insert(tk.END, self.dataset_values[i])
            entry.place(x=500, y=200 + 50 * i)
            self.entries.append(entry)

    def plot_radar_graph(self):
        self.ax.clear()

        categories = ['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4']

        # Duplicate the first value to complete the loop
        values = [0.2,0.1, 0.4, 0.9]
        values.append(values[0])

        # Calculate angles for each variable
        angles = [n / float(len(categories)) * 2 * 3.14159 for n in range(len(categories))]
        angles += angles[:1]

        # Plot the radar graph
        red_line = self.ax.plot(angles, values, marker='o', linestyle='-', color='red', label='Value 1')
        self.ax.fill(angles, values, facecolor='red', alpha=0.25)

        # Set the labels for each variable
        self.ax.set_xticks(angles[:-1])
        self.ax.set_xticklabels(categories)

        # Set the limit for the radial axis
        self.ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])

        # Set the title for the radar graph
        self.ax.set_title('Radar Graph', size=16)

        # Add a legend to show the color-value associations
        yellow_patch = mpatches.Patch(color='yellow', alpha=0.25, label='Value 2')
        self.ax.legend(handles=[red_line[0], yellow_patch], loc='upper right', bbox_to_anchor=(1.2, 1))

        # Redraw the canvas
        self.figure_canvas.draw()

    def update_values(self):
        self.dataset_values = [float(entry.get()) for entry in self.entries]
        self.plot_radar_graph()

# Create the root Tkinter window
root = tk.Tk()

# Create an instance of YourClassName and pass the root window
app = YourClassName(root)

# Create a button to update the values
update_button = tk.Button(root, text="Update Values", command=app.update_values)
update_button.place(x=500, y=400)

# Start the Tkinter event loop
root.mainloop()






