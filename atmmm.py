from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.geometry('650x750')
root.title('ATM')

# disable window resizing
root.resizable(False, False)

image = Image.open("sc.png")
icon_file = "icon.ico"
image.save(icon_file, format="ICO")
icon = ImageTk.PhotoImage(file=icon_file)

# Set the icon of the window to the .ico file
root.iconphoto(False, icon)
# create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# create a file menu item and its sub-items
file_menu = tk.Menu(menu)
menu.add_cascade(label="FILE", menu=file_menu)
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Open")
file_menu.add_separator()
menu.add_cascade(label="EXIT", command=root.quit)
frame = tk.Frame(root)
label = tk.Label(frame, background='blue', width=200, text= 'ATM MACHINE', foreground='gold', font=('Bell MT', 36, 'italic'))
#use the grid method here 
label.pack(side='top')
frame.pack(side='top')

Frame1 = tk.Frame(root)

Label1 = tk.Label(Frame1, background='blue', height=2, foreground='gold', width=15, text='WITHDRAW', font=('Arial', 12, 'italic'))
Label1.grid(row=0, column=0, padx=5, pady=15)
button1 = tk.Button(Frame1, width=10, height=2, background='gold', text='X', activebackground='blue')
button1.grid(row=0, column=1, pady=20, padx=20)

Label2 = tk.Label(Frame1, background='blue', height=2, foreground='gold', width=15, text='TRANSFER', font=('Arial', 12, 'italic'))
Label2.grid(row=2, column=0, padx=5, pady=15)
button2 = tk.Button(Frame1, width=10, height=2, background='gold', text='X', activebackground='blue')
button2.grid(row=2, column=1, pady=20, padx=20)

Label3 = tk.Label(Frame1, background='blue', height=2, foreground='gold', width=15, text='AIRTIME', font=('Arial', 12, 'italic'))
Label3.grid(row=4, column=0, padx=5, pady=15)
button3 = tk.Button(Frame1, width=10, height=2, background='gold', text='X', activebackground='blue')
button3.grid(row=4, column=1, pady=20, padx=20)

Label4 = tk.Label(Frame1, background='blue', height=2, foreground='gold', width=15, text='BALANCE', font=('Arial', 12, 'italic'))
Label4.grid(row=6, column=0, padx=5, pady=15)
button4 = tk.Button(Frame1, width=10, height=2, background='gold', text='X', activebackground='blue')
button4.grid(row=6, column=1, pady=20, padx=20)

Label5 = tk.Label(Frame1, background='blue', height=2, foreground='gold', width=15, text='QUICK TELLER', font=('Arial', 12, 'italic'))
Label5.grid(row=8, column=0, padx=5, pady=15)
button5 = tk.Button(Frame1, width=10, height=2, background='gold', text='X', activebackground='blue')
button5.grid(row=8, column=1, pady=20, padx=20)

Frame1.pack()
Frame2 = tk.Frame(root)
textbox = tk.Text(Frame2, height=10, width=50, font=('Arial', 12), bd=12)
# set the state of Textbox widget to readonly
textbox.configure(state="disabled")
textbox.grid(row=10, column=0, padx=10, pady=10)
Frame2.pack()


root.mainloop()