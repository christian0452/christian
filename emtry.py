import tkinter as tk
from datetime import datetime


# Create instance of Tk class
root = tk.Tk()

# set size of the window
root.geometry("400x400")

# Set title for window
root.title("Calculator App")
# Create label widget
label = tk.Label(root, background='black', width= 250, text="DATE & TIME !", foreground='blue' )
label.grid(row=0, column=0, columnspan=2)

# Place label on the root window
time_label = tk.Label(root, font=('calibri', 80, 'bold italic'), background='purple')
time_label.grid(row=1, column=0, columnspan=2)

# define a function to update the time
def update_time():
     # get current time
    now = datetime.now()
    
    # format the time string
    time_string = now.strftime("%H:%M:%S:%Z")
    
    # format the date string
    date_string = now.strftime("%A, %B %d, %Y")
    
    # update the time label with new time and date strings
    time_label.config(text=time_string + "\n" + date_string)

    # call the update_time function after 2 second
    time_label.after(2000, update_time)
    # call the update_time function to initialize the time label
update_time()

# Create a label and add it to the window
tk.Label(root, text= 'First Name:', width= 50).grid(row=2, column=0)
tk.Label(root, text= 'Last Name:', width= 50).grid(row=3, column=0)
tk.Label(root, text= 'Username:', width= 50).grid(row=4, column=0)
tk.Label(root, text= 'Password:', width= 50).grid(row=5, column=0)

# Create entry fields and add them to the window
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=2, column=1)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=3, column=1)
username_entry = tk.Entry(root)
username_entry.grid(row=4, column=1)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=5, column=1)

# Define login button click event handler
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'guest' and password == 'password':
        message_label.config(text="Login successful!")
    else:
        message_label.config(text="Incorrect username or password")
# Create login and sign up buttons and add them to the window
login_button = tk.Button(root, text='LOGIN', command=handle_login, width= 25, background='blue', foreground='white', font='Bold')
login_button.grid(row=6, column=0, pady=10)
signup_button = tk.Button(root, text='SIGN UP', command=lambda: print('Sign up button clicked'), width=25, background='blue', foreground='white', font='Bold')
signup_button.grid(row=6, column=1, pady=10)

# Create label for displaying login status message
message_label = tk.Label(root, width=50)
message_label.grid(row=7, column=0, columnspan=2, pady=10)
img = tk.PhotoImage(file="img-20220103-wa0004.jpg",)
# Resize image using zoom method
new_img = img.zoom(2, 2)
# Set custom icon for window
root.iconphoto(True, img)
# Run the event loop
root.mainloop()