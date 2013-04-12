import tkinter
import sys
from LogicLanguage import *
from tkinter import *

#handle button 1 clicks
def b1click(event):
	global li1
	global e
	if goodstring():
		li1.insert(END, e.get())
		e.delete(0, END)

#handle button 2 clicks
def b2click(event):
	global li1
	global e
	if goodstring() and somethingselected(li1):
		li1.insert(li1.index(ACTIVE) + 1, "- " + e.get())
		e.delete(0, END)

#handle button 3 clicks
def b3click(event):
	global li2
	global e
	if properrelation():
		li2.insert(END, e.get())
		e.delete(0, END)

#handle button 3 clicks
def b4click(event):
	global li1
	global li2
	if len(sys.argv) > 1:
		name = sys.argv[1]
	else:
		name = "puzzle.txt"
	f = open(name, "wb")
	ls = list(li1.get(0, END))
	ls.extend(list(li2.get(0, END)))
	for l in ls:
		f.write(bytes(l + "\n", "UTF-8"))
	print("Saving to " + name)
	f.close()

#make sure the string can be used
def goodstring():
	global e
	return len(e.get()) > 0 and not e.get().startswith("-") and not " " in e.get()

#make sure the listbox has a selected object
def somethingselected(l):
	return len(l.curselection()) > 0

#make sure the syntax of the relation is correct
def properrelation():
	return True

window = Tk()
#c = Canvas(window, width=600, height=600, highlightthickness=0)
#c = Canvas(window, width=600, height=600, bg='black', highlightthickness=0)
#c.bind("<Button-1>", click)
b1 = Button(window, text="Add Category")
b1.pack()
b2 = Button(window, text="Add Item")
b2.pack()
b3 = Button(window, text="Add Relation")
b3.pack()
e = Entry(window, font=('Courier New', 10), width=20)
e.pack()
la1 = Label(window, text="Categories")
la1.pack()
li1 = Listbox(window, font=('Courier New', 10), width=20)
li1.pack()
la2 = Label(window, text="Relations")
la2.pack()
li2 = Listbox(window, font=('Courier New', 10), width=20)
li2.pack()
b4 = Button(window, text="Export!")
b4.pack()
b1.bind("<Button-1>", b1click)
b2.bind("<Button-1>", b2click)
b3.bind("<Button-1>", b3click)
b4.bind("<Button-1>", b4click)

window.mainloop()