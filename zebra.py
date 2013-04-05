import LogicLanguage.py

house = Category("House", 5, True)
red = Member("Red")
green = Member("Green")
ivory = Member("Ivory")
yellow = Member("Yellow")
blue = Member("Blue")
house.members = [red, green, yellow, blue, ivory]

nationality = Category("Nationality", 5, False)
english = Member("English")
spaniard = Member("Spaniard")
ukranian = Member("Ukranian")
norwegian = Member("Norwegian")
japanese = Member("Japanese")
nationality.members = [english, spaniard, ukranian, norwegian, japanese]

smoking = Category("Smoking", 5, False)
oldgold = Member("Old Gold")
kools = Member("Kools")
chesterfields = Member("Chesterfields")
luckystrike = Member("Lucky Strike")
parliaments = Member("Parliaments")
smoking.members = [oldgold, kools, chesterfields, luckystrike, parliaments]

drink = Category("Drink", 5, False)
coffee = Member("Coffee")
tea = Member("Tea")
milk = Member("Milk")
orangejuice = Member("Orange Juice")
water = Member("Water")
drink.members = [coffee, tea, milk, orangejuice, water]

pet = Category("Pet", 5, False)
dog = Member("Dog"))
snails = Member("Snails"))
fox = Member("Fox"))
horse = Member("Horse"))
zebra = Member("Zebra"))

f1 = Is(english, red)
f2 = Is(spaniard, dog)
f3 = Is(coffee, green)
f4 = Is(ukranian, tea)
f5 = ImmAfter(green, ivory)
f6 = Is(oldgold, snails)
f7 = Is(kools, yellow)
#How do we represent these?
#looks like we'd need a way to represent {next to}, as well as a specific spot number
#f8 = Is(milk, the house in spot 2)
#f9 = Is(norwegian, the house in spot 0)
#f10 = Before(chesterfields, fox) OR After(chesterfields, fox)
#f11 = Before(kools, horse) OR After(kools, horse)
f12 = Is(luckystrike, orangejuice)
f13 = Is(japanese, parliaments)
f14 = Is(norwegian, blue)
