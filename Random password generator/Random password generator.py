import random
from tkinter import *
import string
from tkinter import messagebox
from tkinter.ttk import *

def low():
	entry.delete(0, END)
	length = var1.get()
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789!@#$%^&*()_-+/;"
	password=''
	if var.get()==1:
		for i in range(length):
			password+=random.choice(lowercase)
		return password

	elif var.get()==0:
		for i in range(length):
			password+=random.choice(uppercase)
		return password

	elif var.get()==3:
		for i in range(length):
			password+=random.choice(numbers)
		return password

	else:
		messagebox.showwarning('Warning','Select One of the options')

def copy1():
	random_pwd1 = entry.get()
	root.clipboard_clear()
	root.clipboard_append(random_pwd1)

def generate():
	p = low()
	entry.insert(10,p)

#GUI Window
root = Tk()
var,var1 = IntVar(), IntVar()
root.title('Random Password Generator')
pk = Label(root,text="Password")
pk.grid(row=0)
entry = Entry(root)
entry.grid(row=0,column=1)

c_label = Label(root,text="Length")
c_label.grid(row=1)

copy = Button(root,text="Copy",command=copy1)
copy.grid(row=0,column=2)

generate = Button(root,text="Generate",command=generate)
generate.grid(row=0,column=3)

Quit = Button(root,text="Quit",command=root.quit)
Quit.grid(row=0,column=4)

#Radio Buttons to set password length
radio_low = Radiobutton(root,text="Low Password",variable=var,value=1)
radio_low.grid(row=1,column=2,sticky='E')
radio_medium = Radiobutton(root,text="Medium Password",variable=var,value=0)
radio_medium.grid(row=1,column=3,sticky='E')
radio_strong = Radiobutton(root,text="Strong Password",variable=var,value=3)
radio_strong.grid(row=1,column=4,sticky='E')
combo = Combobox(root,textvariable=var1)

#Combobox for password lengths
combo['values'] = (4,6,8,9,10,11,12,13,14,15,16,
				   17,18,19,20,21,22,23,24,25,
				   26,27,28,29,30,31,32,33)
combo.current(0)
#combo.bind('<<ComboboxSelected>>')
combo.grid(column=1,row=1)
root.mainloop()