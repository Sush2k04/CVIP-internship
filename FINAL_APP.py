import tkinter as tk

#Part 1
root = tk.Tk()
root.title("Expense Sharing App")
root.geometry("500x750+400+50")
root.config(bg="MediumPurple1")

#Functions
def add_user():
    name = name_entry.get()
    roommates.append(name)
    bln[name] = 0
    upd_lst()

def add_amount():
    n_to = to_entry.get()
    name_from = from_entry.get()
    amount = int(amt_entry.get())
    if name_from == "":
        name_from = n_to
        bln[n_to] += amount
    bln[n_to] += amount
    bln[name_from] -= amount
    upd_lst()
def split_amount():
    amount = int(amt_entry.get())
    num_roommates = len(roommates)
    split_share = amount / num_roommates
    for name in roommates:
        bln[name] += split_share
    upd_lst()



def upd_lst():
    listbox.delete(0, tk.END)
    for name in roommates:
        listbox.insert(tk.END, f"{name}: {bln[name]}")

def who_owes_whom():
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Owing:\n")
    for name1 in roommates:
        for name2 in roommates:
            if bln[name1] < bln[name2] and bln[name1] > 0:
                amount = min(bln[name2] - bln[name1], abs(bln[name1]))
                result_text.insert(tk.END, f"{name2} owes {name1} Rs. {amount}\n")
    result_text.config(state=tk.DISABLED)


#Part 3
frame = tk.Frame(root)
frame.pack(pady=10)

#Part 4
name_label = tk.Label(frame, text="Enter Name:", font=('Helvetica', 12, 'bold'),bg="Powder Blue")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, font=('Helvetica', 12, 'italic'),bg="Powder Blue")
name_entry.grid(row=0, column=1, padx=5, pady=5)

aduser_btn = tk.Button(frame, text="Add User", font=('Helvetica', 12, 'bold'),bg="Powder Blue", command=add_user)
aduser_btn.grid(row=0, column=2, padx=5, pady=5)

to_label = tk.Label(frame, text="To:", font=('Helvetica', 12, 'bold'),bg="Powder Blue")
to_label.grid(row=1, column=0, padx=5, pady=5)
to_entry = tk.Entry(frame, font=('Helvetica', 12, 'italic'),bg="Powder Blue")
to_entry.grid(row=1, column=1, padx=5, pady=5)

from_label = tk.Label(frame, text="From:", font=('Helvetica', 12, 'bold'),bg="Powder Blue")
from_label.grid(row=2, column=0, padx=5, pady=5)
from_entry = tk.Entry(frame, font=('Helvetica', 12, 'italic'),bg="Powder Blue")
from_entry.grid(row=2, column=1, padx=5, pady=5)

amt_label = tk.Label(frame, text="Amount:", font=('Helvetica', 12, 'bold'),bg="Powder Blue")
amt_label.grid(row=3, column=0, padx=5, pady=5)
amt_entry = tk.Entry(frame, font=('Helvetica', 12, 'italic'),bg="Powder Blue")
amt_entry.grid(row=3, column=1, padx=5, pady=5)

ad_amt_btn = tk.Button(frame, text="Add Amount", font=('Helvetica', 12, 'bold'),bg="Powder Blue", command=add_amount)
ad_amt_btn.grid(row=3, column=2, padx=5, pady=5)

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

listbox_label = tk.Label(listbox_frame, text="Balance:", font=('Helvetica', 12, 'bold'),bg="Powder Blue")
listbox_label.pack(pady=5)

listbox = tk.Listbox(listbox_frame, width=40, height=10, font=('Helvetica', 12, 'bold'),bg="Powder Blue")
listbox.pack(pady=5)

#Part4 (continued)
split_button = tk.Button(frame, text="Split Amount Equally", font=('Helvetica', 12, 'bold'), bg="Powder Blue", command=split_amount)
split_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)


owe = tk.Button(root, text="Check Who Owes Whom", font=('Helvetica', 12, 'bold'),bg="Powder Blue", command=who_owes_whom)
owe.pack(pady=5)

result_text = tk.Text(root, width=40, height=10, font=('Helvetica', 12),bg="Powder Blue")
result_text.pack(pady=10)
result_text.config(state=tk.DISABLED)

bln = {}
roommates = []

root.mainloop()
