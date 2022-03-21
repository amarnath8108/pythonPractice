from tkinter import *
import tkinter as tk
root =Tk()
root.geometry("600x400")
name_var = tk.StringVar()
USN_var = tk.StringVar()
def submit():
    name = name_var.get()
    USN = USN_var.get()
    newWindow = Toplevel(root)
    newWindow.geometry("600x400")
    e = Entry(newWindow, width=100, fg='blue',font=('Arial', 16, 'bold'))
    e.grid(row=1)
    e.insert(END, "The name is : " + name)
    e.grid(row=2)
    e.insert(END, "The USN is : " + USN)


name_label = tk.Label(root, text='STU_Name', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
USN_label = tk.Label(root, text='USN', font=('calibre', 10, 'bold'))
USN_entry = tk.Entry(root, textvariable=USN_var, font=('calibre', 10, 'normal'), show='*')
sub_btn = tk.Button(root, text='Submit', command=submit)
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
USN_label.grid(row=1, column=0)
USN_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)
root.mainloop()
