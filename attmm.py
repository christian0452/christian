import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
root = tk.Tk()
root.geometry('550x750')
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

def save_file():
    # Open file dialog for selecting a file path to save
    save_file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetype=[('Text files', '*.txt')])
    if save_file_path:
        with open(save_file_path,'w') as f:
            for transaction in transactions:
                f.write(transaction + '\n')
        # Display success message
        messagebox.showinfo('Success', 'file saved successfully.')

def open_file():
    # Open file dialog to select a file for opening
    open_file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if open_file_path:
        with open(open_file_path, 'w') as f:
            for transaction in transactions:
                f.write(transaction + '\n')
                f.close()
        # Dialog to show successful saving of the file
        messagebox.showinfo('Success', 'file open success')
    else:
        # Dialog to show no file was selected
        messagebox.showarning('Warning', 'No file selected.')

# create a file menu item and its sub-items
file_menu = tk.Menu(menu)
menu.add_cascade(label="FILE", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
menu.add_cascade(label="EXIT", command=root.quit)

frame = tk.Frame(root)
label = tk.Label(frame, background='blue', width=200, text= 'ATM MACHINE', foreground='gold', font=('Bell MT', 36, 'italic'))
#use the grid method here 
label.pack(side='top')
frame.pack(side='top')

# Load and resize the image
imagefile = "3670896-1466801735.jpg"
img = Image.open(imagefile)
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
Background_img = ImageTk.PhotoImage(img)
balance = 100000 
transactions = []
def withdraw():
    popup= tk.Toplevel(root, bg='yellow')
    popup.geometry('300x250')
    popup.title('Withdrawal Amount')
    image = Image.open("sc.png")
    icon_file = "icon.ico"
    image.save(icon_file, format="ICO")
    icon = ImageTk.PhotoImage(file=icon_file)
    popup.iconphoto(False, icon)

    label= tk.Label(popup, text='Select Amount Withdraw', font=('Arial', 12))
    label.pack(pady=15)
    amount=[1000, 2000, 5000, 10000, 20000]
    option_var = tk.StringVar()
    option_var.set(amount[0])
    amount_dropdown = tk.OptionMenu(popup, option_var, *amount)
    amount_dropdown.config(width=10, font=('Arial', 12))
    amount_dropdown.pack()
    #label for Other Amounts 
    labelSearch = tk.Label(popup, text='Other Amounts:', font=('Arial', 12))
    labelSearch.pack(pady=10)
    entrySearch = tk.Entry(popup, width=20, bd=3)
    entrySearch.pack()
    
    # Add a button to confirm the withdrawal and update the balance
    def confirm_withdraw():
        global balance
        selected_amount = None
        other_amount = entrySearch.get()
        if other_amount:
            try:
                selected_amount = int(other_amount)
            except ValueError:
                pass
        if selected_amount is None:
            selected_amount = int(option_var.get())

        # Assuming balance is a static variable with the current balance available
        global balance
        if selected_amount > balance:  
            statement = 'insufficient funds!'
        else:
                checkbalance()
                new_balance = balance - selected_amount
                statement = f'withdrawal of {selected_amount} was succesful.'
                # Update the balance and call the checkbalance method
                balance = new_balance

                # Store the transaction in the list
                transactions.append(statement)

        textbox.configure(state='normal', font=('Arial', 12, 'bold'))
        textbox.delete('1.0', tk.END)
        textbox.insert(tk.END, statement)
        textbox.configure(state='disabled')

        popup.destroy()      

    confirm_button = tk.Button(popup, text='Confirm', width=10, height=2, command=lambda:confirm_withdraw())
    confirm_button.pack(pady=20)


#implementing my transfer function
def transfer():
    
    transferPop = tk.Toplevel(root, bg='grey')
    transferPop.geometry('300x250')
    transferPop.title('Transfer Money')
    
    image = Image.open("sc.png")
    icon_file = "icon.ico"
    image.save(icon_file, format="ICO")
    icon = ImageTk.PhotoImage(file=icon_file)

    # Set the icon of the window to the .ico file
    transferPop.iconphoto(False, icon)
    Labels = tk.Label(transferPop, text='Enter your Acc Number :', font=('Arial', 12))
    Labels.pack(pady=5)
    AcctEntry = tk.Entry(transferPop, width= 10, font=('arial', 12))
    AcctEntry.pack(pady=5)
    label= tk.Label(transferPop, text='Select your Bank', font=('Arial', 12))
    label.pack(pady=5)
    banks = {
        'bank1':'GTB',
        'bank2':'FIRST BANK',
        'bank3':'UBA',
        'bank4':'ZENITH',
        'bank5':'STANBIC IBTC',
        'bank6':'FCMB',
        'bank7':'UNION',
        'bank8':'KEYSTONE',
        'bank9':'ACCESS',
        'bank10':'ECO',
        'bank11':'WEMA',
        'bank12':'UNITY',
        'bank13':'POLARIS',
        'bank14':'FIDELITY',
        'bank15':'STERLING',
        'bank16':'HERITAGE',
        'bank17':'PROVIDUS',
        'bank18':'STANDARD CHARTERED',
        'bank19':'SUNTRUST',
        'bank20':'CITIBANK NG',
        'bank21':'CENTRAL BANK',
        'bank22':'JAIZ',
        'bank23':'OPAY',
    }
    newBank = banks.values()
    option_var = tk.StringVar()
    option_var.set(newBank)
    amount_dropdown = tk.OptionMenu(transferPop, option_var, *newBank)
    amount_dropdown.config(width=10, font=('Arial', 12))
    amount_dropdown.pack()
    transferLabel = tk.Label(transferPop, text='Enter Amount to Transfer :', font=('Arial', 12))
    transferLabel.pack(pady=5)
    AmountEntry = tk.Entry(transferPop, width=10, font=('arial', 12))
    AmountEntry.pack(pady=5)
    
    def transferfun():
        global balance
        acc_num = AcctEntry.get()
        select_banks =option_var.get()
    
        # Ensure account number is exactly 10 digits long
        if len(acc_num) != 10:
            statement = 'Account number must be 10 digits!'
        else:
            transfer_amt = int(AmountEntry.get())
            if transfer_amt > balance:
                statement = 'Insufficient funds!'
        
            else:
                checkbalance()
                new_balance = balance -transfer_amt
                statement = f'Transferred {transfer_amt}. to {select_banks} ({acc_num}) was successful.'
                transactions.append(statement)
                balance = new_balance

            textbox.configure(state='normal', font=('Arial',12, 'bold'))
            textbox.delete('1.0', tk.END)
            textbox.insert(tk.END, statement)
            textbox.configure(state='disabled')
            
        transferPop.destroy()

            
    transfer_button = tk.Button(transferPop, text='Transfer', width=15, height=4, command=lambda:transferfun())
    transfer_button.pack(pady=5)

def checkbalance():
    statement = f'Your new balance is {balance}'
    transactions.append(statement)
    textbox.configure(state='normal', font=('Arial', 12, 'bold'))
    textbox.delete('1.0', tk.END)
    textbox.insert(tk.END, statement)
    textbox.configure(state='disabled')

def airtime():
    
    airtimePop = tk.Toplevel(root, bg='grey')
    airtimePop.geometry('300x300')
    airtimePop.title('Airtime')
    
    image = Image.open("sc.png")
    icon_file = "icon.ico"
    image.save(icon_file, format="ICO")
    icon = ImageTk.PhotoImage(file=icon_file)

    Labels = tk.Label(airtimePop, text='Enter Your Network :', font=('Arial', 12))
    Labels.pack(pady=5)
    network = ['MTN', 'GLO', 'AIRTEL', 'ETISALAT']
    option_var = tk.StringVar()
    option_var.set(network[0])
    network_dropdown = tk.OptionMenu(airtimePop, option_var, *network)
    network_dropdown.config(width=10, font=('Arial', 12))
    network_dropdown.pack()
    #label for phone number
    phoneno = tk.Label(airtimePop, text='Enter Your Phone Number :', font=('Arial', 12))
    phoneno.pack(pady=5)
    numberEntry = tk.Entry(airtimePop, width=10, font=('arial', 12))
    numberEntry.pack(pady=5)
    #label for amount
    amountLabel = tk.Label(airtimePop, text='Enter Amount :', font=('Arial', 12))
    amountLabel.pack(pady=5)
    AmountEntry = tk.Entry(airtimePop, width=10, font=('arial', 12))
    AmountEntry.pack(pady=5)

    def airtimecon():
        airtime_phone_entry = numberEntry.get()
        airtime_amount_entry = AmountEntry.get()
        select_network = option_var.get()
        if len(airtime_phone_entry) !=11:

            textbox.configure(state='normal', font=('Arial',12, 'bold'))
            textbox.delete('1.0', tk.END)
            textbox.insert(tk.END, 'Phone number must be 11 digit')
            textbox.configure(state='disabled')
        else:
            airtime_amount = int(airtime_amount_entry)
        global balance
        if balance > airtime_amount:
            checkbalance()
            newbalance = balance - airtime_amount

            textbox.configure(state='normal', font=('Arial',12, 'bold'))
            textbox.delete('1.0', tk.END)
            textbox.insert(tk.END, f'You have sent {airtime_amount_entry} airtime to {airtime_phone_entry} {select_network} network')
            textbox.configure(state='disabled')
            balance = newbalance
        else:
            #Display an error message if there is not enough balance
            textbox.configure(state='normal', font=('Arial',12, 'bold'))
            textbox.delete('1.0', tk.END)
            textbox.insert(tk.END, 'Insufficient funds')
            textbox.configure(state='disabled')
        airtimePop.destroy()

    airtime_button = tk.Button(airtimePop, text='Purchase', width=10, height=2, command=lambda:airtimecon())
    airtime_button.pack(pady=10)
    

Frame1 = tk.Frame(root)
Frame1.pack(fill='both', expand=True)

# Create a label widget with the image as its background

# Create a label widget with the image as its background
bg_label = tk.Label(Frame1, image=Background_img)
bg_label.grid(row=0, column=0, sticky="nsew")

# Configure the row and column to stretch
Frame1.rowconfigure(0, weight=1)
Frame1.columnconfigure(0, weight=1)
# Configure the bg_label to center-align its contents vertically
bg_label.grid_rowconfigure(0, weight=1)

# Add a dummy label to push Label1 to the center
dummy_label1 = tk.Label(bg_label, width=30, highlightthickness=0)
dummy_label1.grid(row=1, column=0)
Label1 = tk.Label(bg_label,  background='blue', height=2, foreground='gold', width=15, text='WITHDRAW', font=('Arial', 12, 'italic'))
Label1.grid(row=1, column=1,padx=5,  pady=15, sticky="nsew")
button1 = tk.Button(bg_label, width=10, height=2, activebackground='blue', background='gold', text='X', command=lambda:withdraw())
button1.grid(row=1, column=2, pady=20, padx=20)
# Add a dummy label to push Label2 to the center
dummy_label2 = tk.Label(bg_label, width=30, highlightthickness=0)
dummy_label2.grid(row=3, column=0)
Label2 = tk.Label(bg_label, background='blue', height=2, foreground='gold', width=15, text='TRANSFER', font=('Arial', 12, 'italic'))
Label2.grid(row=3, column=1, padx=5, pady=15, sticky="nsew")
button2 = tk.Button(bg_label, width=10, height=2, command=lambda:transfer(), activebackground='blue', background='gold', text='X')
button2.grid(row=3, column=2, pady=20, padx=20)

# Add a dummy label to push Label3 to the center
dummy_label3 = tk.Label(bg_label, width=30, highlightthickness=0)
dummy_label3.grid(row=5, column=0)
Label3 = tk.Label(bg_label, background='blue', height=2, foreground='gold', width=15, text='AIRTIME', font=('Arial', 12, 'italic'))
Label3.grid(row=5, column=1, padx=5, pady=15, sticky="nsew")
button3 = tk.Button(bg_label, width=10, height=2, command=lambda:airtime(), activebackground= 'blue', background='gold', text='X')
button3.grid(row=5, column=2, pady=20, padx=20)

# Add a dummy label to push Label4 to the center
dummy_label4 = tk.Label(bg_label, width=30, highlightthickness=0)
dummy_label4.grid(row=7, column=0)
Label4 = tk.Label(bg_label, background='blue', height=2, foreground='gold', width=15, text='BALANCE', font=('Arial', 12, 'italic'))
Label4.grid(row=7, column=1, padx=5, pady=15, sticky="nsew")
button4 = tk.Button(bg_label, width=10, height=2, command=lambda:checkbalance(), activebackground='blue', background='gold', text='X')
button4.grid(row=7, column=2, pady=20, padx=20)

# Add a dummy label to push Label5 to the center
dummy_label5 = tk.Label(bg_label, width=30, highlightthickness=0)
dummy_label5.grid(row=9, column=0)
Label5 = tk.Label(bg_label, background='blue', height=2, foreground='gold', width=15, text='STATEMENT', font=('Arial', 12, 'italic'))
Label5.grid(row=9, column=1, padx=5, pady=15, sticky="nsew")
button5 = tk.Button(bg_label, width=10, height=2, command=lambda:save_file(), activebackground='blue', background='gold', text='X')
button5.grid(row=9, column=2, pady=20, padx=20)


Frame2 = tk.Frame(root)
Frame2.pack()



textbox = tk.Text(Frame2, height=10, width=50, font=('Arial', 12), bd=12)
# set the state of Textbox widget to readonly
textbox.configure(state="disabled")
textbox.grid(row=10, column=2, padx=15, pady=10)

root.mainloop()