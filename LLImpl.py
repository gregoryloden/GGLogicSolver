from LogicLanguage import *

house = Category("House", 5, True)
h1 = Member("H1")
h2 = Member("H2")
h3 = Member("H3")
h4 = Member("H4")
h5 = Member("H5")
house.add(h1)
house.add(h2)
house.add(h3)
house.add(h4)
house.add(h5)

color = Category("Color", 5, False)
red = Member("Red")
green = Member("Green")
ivory = Member("Ivory")
yellow = Member("Yellow")
blue = Member("Blue")
color.add(red)
color.add(green)
color.add(yellow)
color.add(blue)
color.add(ivory)

nationality = Category("Nationality", 5, False)
english = Member("English")
spaniard = Member("Spaniard")
ukranian = Member("Ukranian")
norwegian = Member("Norwegian")
japanese = Member("Japanese")
nationality.add(english)
nationality.add(spaniard)
nationality.add(ukranian)
nationality.add(norwegian)
nationality.add(japanese)

smoking = Category("Smoking", 5, False)
oldgold = Member("OldGold")
kools = Member("Kools")
chesterfields = Member("Chesterfields")
luckystrike = Member("LuckyStrike")
parliaments = Member("Parliaments")
smoking.add(oldgold)
smoking.add(kools)
smoking.add(chesterfields)
smoking.add(luckystrike)
smoking.add(parliaments)

drink = Category("Drink", 5, False)
coffee = Member("Coffee")
tea = Member("Tea")
milk = Member("Milk")
orangejuice = Member("OrangeJuice")
water = Member("Water")
drink.add(coffee)
drink.add(tea)
drink.add(milk)
drink.add(orangejuice)
drink.add(water)

pet = Category("Pet", 5, False)
dog = Member("Dog")
snails = Member("Snails")
fox = Member("Fox")
horse = Member("Horse")
zebra = Member("Zebra") 
pet.add(dog)
pet.add(snails)
pet.add(fox)
pet.add(horse)
pet.add(zebra)

f1 = Is(english, red)
f2 = Is(spaniard, dog)
f3 = Is(coffee, green)
f4 = Is(ukranian, tea)
f5 = ImmAfter(green, ivory)
f6 = Is(oldgold, snails)
f7 = Is(kools, yellow)
f8 = Is(milk, h3)
f9 = Is(norwegian, h1)
f10 = Or(ImmBefore(chesterfields, fox), ImmAfter(chesterfields, fox))
f11 = Or(ImmBefore(kools, horse), ImmAfter(kools, horse))
f12 = Is(luckystrike, orangejuice)
f13 = Is(japanese, parliaments)
f14 = Is(norwegian, blue)

puzzle = Puzzle()
puzzle.categories = [house, color, nationality, smoking, drink, pet]
puzzle.relationships = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]