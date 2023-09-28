import tkinter as tk

root = tk.Tk()

# create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# create a file menu item and its sub-items
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create an edit menu item and its sub-items
exit_menu = tk.Menu(menu)
menu.add_cascade(label="Exit", menu=exit_menu)
exit_menu.add_command(label="Cut")
exit_menu.add_command(label="Copy")
exit_menu.add_command(label="Paste")

root.mainloop()