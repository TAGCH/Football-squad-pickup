import tkinter as tk
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

        # Create a radar graph
        fig = Figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)

        # Define the variables and their values
        categories = ['Attack', 'Passing', 'Defend', 'Protect']
        values = [72, 65, 86, 88]
        
        values2 = [80, 88, 52, 75]

        # Duplicate the first value to complete the loop
        values.append(values[0])
        
        values2.append(values2[0])

        # Calculate angles for each variable
        angles = [n / float(len(categories)) * 2 * 3.14159 for n in range(len(categories))]
        angles += angles[:1]

        # Plot the radar graph
        ax.plot(angles, values, marker='o', linestyle='-', color='red')
        ax.fill(angles, values, facecolor='red', alpha=0.25)
        
        ax.plot(angles, values2, marker='o', linestyle='-', color='yellow')
        ax.fill(angles, values2, facecolor='yellow', alpha=0.25)

        # Set the labels for each variable
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)

        # Set the limit for the radial axis
        ax.set_yticks([20, 40, 60, 80, 100])

        # Set the title for the radar graph
        ax.set_title('Radar Graph', size=16)

        # Create a Tkinter canvas for the radar graph
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()

        # Place the radar graph within the white rectangle
        canvas.get_tk_widget().place(x=460, y=10)

# Create the root Tkinter window
root = tk.Tk()

# Create an instance of YourClassName and pass the root window
app = YourClassName(root)

# Start the Tkinter event loop
root.mainloop()