import sys
from LogicLanguage import *
import re
if re.match("^win.*", sys.platform):
	from tkinter import *
else:
	from Tkinter import *
from plaintext_solver import parse_file
from solve import solve


#handle Add Category clicks
def b1click(event):
	global li1
	global e
	#acceptable category
	if goodstring("category"):
		#add to the list of categories, and clear the entry box
		li1.insert(END, e.get())
		li1.see(END)
		e.delete(0, END)

#handle Add Item clicks
def b2click(event):
	global li1
	global e
	#acceptable item
	if goodstring("item") and somethingselected(li1):
		#add above an item
		if li1.get(ACTIVE).startswith("-"):
			spot = li1.index(ACTIVE)
		#add to the end of a category
		else:
			spot = li1.index(ACTIVE) + 1
			end = li1.index(END)
			while spot < end and li1.get(spot).startswith("-"):
				spot += 1
		li1.insert(spot, "- " + e.get())
		li1.see(spot)
		e.delete(0, END)

#handle Add Relation clicks
def b3click(event):
	global li2
	global e
	#acceptable relation
	if properrelation(e.get()):
		#add to the list of relations
		li2.insert(END, e.get())
		li2.see(END)
		e.delete(0, END)

#handle Solve! clicks
def b4click(event):
	global li1
	global li2
	f = open("puzzle.txt", "wb")
	#check for validity
	categories = categoriesList()
	topinfo = topInfo(categories)
	if topinfo == None:
		return
	#start building the list of items
	ls = [topinfo]
	#add all the category information
	for c in categories:
		ls.extend(c)
	#add all the relation information
	ls.extend(list(li2.get(0, END)))
	#save the file
	for l in ls:
		f.write(bytes(l + "\n", "UTF-8"))
	print("Saving to puzzle.txt")
	f.close()
	#solve the puzzle and print it
	print("Solving the puzzle")
	answer = sortedAnswer(list(solve(parse_file("puzzle.txt"))))
	#show the answer in a window
	response = Tk()
	#make a grid with each row being the entity
	for row in answer:
		r = Frame(response)
		r.pack()
		#each item belonging to the entity
		for item in row:
			l = Label(r, text=item + "\t", width=12)
			l.pack(side=LEFT)
	response.mainloop()

#BONUS FEATURE- INCOMPLETE
#delete an item from the categories list
def li1backspace(event):
	global li1
	if not somethingselected(li1):
		return
	if li1.get(ACTIVE).startswith("-"):
		li1.delete(ACTIVE)
	else:
		spot = li1.index(ACTIVE) + 1
		end = li1.index(END)
		while spot < end and li1.get(spot).startswith("-"):
			spot += 1
		li1.delete(ACTIVE, spot - 1)
	pass

#BONUS FEATURE- INCOMPLETE
#delete an item from the relations list
def li2backspace(event):
	global li2
	if somethingselected(li2):
		li2.delete(ACTIVE)

#make sure the string can be used
def goodstring(type):
	global e
	#empty string
	if len(e.get()) <= 0:
		print("Your " + type + " is empty")
		return False
	#can't start with "-"
	if e.get().startswith("-"):
		print("Your " + type + " cannot start with \"-\"")
		return False
	#names can't have spaces
	if " " in e.get():
		print("Your " + type + " cannot contain spaces")
		return False
	#names must start with a letter
	if not re.match("^[A-Za-z].*", e.get()):
		print("Your " + type + " must start with a letter")
		return False
	return True

#make sure the listbox has a selected object
def somethingselected(l):
	if len(l.curselection()) <= 0:
		print("You have nothing selected")
		return False
	return True

#make sure the syntax of the relation is correct
def properrelation(s):
	s = s.split(" ")
	for i in range(0, len(s)):
		s[i] = relationType(s[i], categoriesList())
	changed = True
	ors = 0
	#keep reducing it until it hasn't changed anymore
	while changed:
		changed = False
		spot = 1
		#go through all the tokens and see if we can reduce the string
		while spot < len(s) and len(s) > 1:
			#relation between two items: [Item] [Relation] [Item] => [VerifiedRelation]
			if ((s[spot] == 1 or s[spot] == 2) and spot > 0 and s[spot - 1] == 0 and spot < len(s) - 1 and s[spot + 1] == 0):
				#replace it
				s[spot - 1:spot + 2] = [4]
				spot = 0
				changed = True
			#boolean relation between two relations: [VerifiedRelation] Or [VerifiedRelation] = [VerifiedRelation]
			elif s[spot] == 3 and spot > 0 and s[spot - 1] == 4 and spot < len(s) - 1 and s[spot + 1] == 4:
				if ors > 0:
					print("You cannot have multiple boolean relations")
					return False
				#replace it
				s[spot - 1:spot + 2] = [4]
				spot = 0
				changed = True
				ors = 1
			spot += 1
	#must end with 1 token, which is a VerifiedRelation
	if len(s) != 1 or s[0] != 4:
		print("You need a proper relation")
		return False
	return True

#get the lists of categories and items
def categoriesList():
	global li1
	ls = list(li1.get(0, END))
	end = len(ls)
	categories = []
	spot = 0
	#go through all the categories
	while spot < end:
		items = [ls[spot]]
		spot += 1
		#add all items for the category
		while spot < end and ls[spot].startswith("-"):
			items.append(ls[spot][2:])
			spot += 1
		categories.append(items)
	return categories

#make sure the categories are properly formatted
def topInfo(categories):
	global li1
	ccount = len(categories)
	#must have at least 2 categories
	if ccount < 2:
		print("You need at least 2 categories with at least 1 item each")
		return None
	#must have at least 1 item
	icount = len(categories[0])
	if icount < 2:
		print("You need at least 1 item")
		return None
	#make sure all categories have the same number of items
	for c in categories:
		if len(c) != icount:
			print("All categories need the same number of items")
			return None
	#check if the first category is ordered
	isordered = ordered(categories)
	if isordered == None:
		return None
	return str(ccount) + " " + str(icount - 1) + " " + str(isordered)

#check if the first category is ordered
def ordered(categories):
	global li2
	ordered = False
	ls = list(li2.get(0, END))
	#loop through all the relations
	for rel in ls:
		s = rel.split(" ")
		#get all the tokens
		for i in range(0, len(s)):
			#check if it's an ordered relation
			if relationType(s[i], categories) == 1:
				ordered = True
				#check that the syntax doesn't put any two first-category items in a ordered operation together
				if s[i - 1] in categories[0][1:] and s[i + 1] in categories[0][1:]:
					print("You can't relate order for ordered items")
					return None
	return ordered

#check if the string represents an ordered relation operator, an equality relation operator, a boolean relation operator, or an item
def relationType(s, categories):
	if s == "Before" or s == "After" or s == "ImmBefore" or s == "ImmAfter":
		return 1
	if s == "Is" or s == "IsNot":
		return 2
	if s == "Or":
		return 3
	for i in categories:
		if s in i[1:]:
			return 0
	return -1

#order the items in the grid by the first one
def sortedAnswer(answer):
	result = []
	#loop through all the items
	for a in answer:
		placed = False
		#find its place in the list
		for i in range(0, len(result)):
			#add it when it's at the right spot
			if a[0] < result[i][0]:
				result.insert(i, a)
				placed = True
				break
		#add it to the end of the list if it belongs there
		if not placed:
			result.append(a)
	return result

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
f1 = Frame(window)
f1.pack()
f2 = Frame(f1)
f2.pack(side=LEFT)
la1 = Label(f2, text="Categories")
la1.pack()
li1 = Listbox(f2, font=('Courier New', 10), width=20)
li1.pack()
f3 = Frame(f1)
f3.pack(side=RIGHT)
la2 = Label(f3, text="Relations")
la2.pack()
li2 = Listbox(f3, font=('Courier New', 10), width=20)
li2.pack()
b4 = Button(window, text="Solve!")
b4.pack()
b1.bind("<Button-1>", b1click)
b2.bind("<Button-1>", b2click)
b3.bind("<Button-1>", b3click)
b4.bind("<Button-1>", b4click)
li1.bind("<BackSpace>", li1backspace)
li2.bind("<BackSpace>", li2backspace)

window.mainloop()