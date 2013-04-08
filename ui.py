import tkinter
import sys
from LogicLanguage import *
from tkinter import *

#handle drawing
def draw(d):
	d.create_rectangle(0, 0, 600, 600, fill='black', outline='black')
	d.create_text(100, 100, anchor=W, fill='white', font=('Courier New', 24, 'bold'), text='Test')
#	d.create_rectangle(x, y, w, h, fill='white', outline='black')
#	d.create_line(x1, y1, x2, y2, fill='white')
#	d.create_oval(x1, y2, x2, y2, fill='white', color='black')
#	d.create_text(x, y, anchor=W, font='Courier New', text='?')

#handle clicks
def click(event):
	pass

window = Tk()
w = Canvas(window, width=600, height=600, bg='black', highlightthickness=0)
w.pack()
w.bind("<Button-1>", click)
draw(w)

window.mainloop()