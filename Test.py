from My_Squad import My_Squad
from MySquadManagement import MySquadManagement
import tkinter.ttk as ttk


# Create an instance of the My_Squad class
instance = My_Squad(ttk)  # Replace 'parent' with the appropriate parent widget

# Call the ST method and store the returned list
st_list = instance.ST()

# Use the st_list in your code as needed
for name in st_list:
    print(name)