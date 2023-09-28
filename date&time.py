from ctypes import alignment
import tkinter as tk
from datetime import datetime


# Create instance of Tk class
root = tk.Tk()

# set size of the window
root.geometry("400x400")

# Set title for window
root.title("Calculator App")
# Create label widget
label = tk.Label(root, background='black', width= 250, anchor='e', text="DATE & TIME !", foreground='orange', )
label.pack(expand=False)
# Place label on the root window

time_label = tk.Label(root, font=('cooper black', 20, 'bold'), background='purple')
time_label.pack(fill='both', expand=True)

# define a function to update the time
def update_time():
    # get current time
    now = datetime.now()
     # format the time string
    time_string = now.strftime("%H:%M:%S")
    
    # format the date string
    date_string = now.strftime("%A, %B %d, %Y, %Z")
    
    # update the time label with new time and date strings
    time_label.config(text=time_string + "\n" + date_string)

    # call the update_time function after 1 second
    time_label.after(2000, update_time)

# call the update_time function to initialize the time label
update_time()
# Run the event loop
root.mainloop() 