import tkinter as tk
window = tk.Tk()
window.geometry("400x400")
window.title("ATM")
label = tk.Label(window, background='blue', width= 250, font=('calibri', 50, 'bold'), text='ATM MACHINE', foreground='white')
label.pack()
# create a menu
menu = tk.Menu(window)
window.config(menu=menu)

# create a file menu item and its sub-items
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="save")
file_menu.add_separator()
file_menu.add_command(label="Open")
file_menu.add_separator()
menu.add_cascade(label="Exit", command=window.quit)
button = tk.Button(window, background='yellow')
frame = tk.Frame(window)
btn_withdraw = tk.Button(window, text="Withdraw", command='withdraw')
btn_deposit = tk.Button(window, text="Deposit", command='deposit')
btn_transfer = tk.Button(window, text="Transfer", command='transfer')
btn_checkbalance = tk.Button(window, text="Check Balance", command='check balance')
btn_airtime = tk.Button(window, text="Airtime", command='airtime')

# Pack the buttons onto the window
btn_withdraw.pack(side=tk.LEFT, padx=50, pady=100)
btn_deposit.pack(side=tk.LEFT, padx=50, pady=100)
btn_transfer.pack(side=tk.LEFT, padx=50, pady=100)
btn_checkbalance.pack(side=tk.LEFT, padx=50, pady=100)
btn_airtime.pack(side=tk.LEFT, padx=50, pady=100)

window.mainloop()