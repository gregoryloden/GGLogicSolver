open util/ordering[House] 

abstract sig Nationality {
  nat_house: one House,
  nat_pet: one Pet,
  nat_cig: one Cigarette,
  nat_drink: one Drink,
  nat_color: one Color,
}{}
one sig English, Spanish, Ukranian, Japanese, Norwegian extends Nationality {}

abstract sig House {
  house_pet: one Pet,
  house_cig: one Cigarette,
  house_drink: one Drink,
  house_color: one Color,
  next_to: set House,
}{
  one this.~nat_house
  one x: Nationality | x.nat_house = this and x.nat_pet = this.@house_pet and x.nat_cig = this.@house_cig and x.nat_drink = this.@house_drink and x.nat_color = this.@house_color
  this.@next_to in {x: House | x = this.next or x = this.prev} 
}
one sig H1, H2, H3, H4, H5 extends House {}
fact {
  first = H1
  next[H1] = H2
  next[H2] = H3
  next[H3] = H4
  next[H4] = H5
}

abstract sig Pet {
  pet_cig: one Cigarette,
  pet_drink: one Drink,
  pet_color: one Color,
}{
  one this.~nat_pet
  one this.~house_pet
  one x: Nationality | x.nat_pet = this and x.nat_cig = this.@pet_cig and x.nat_drink = this.@pet_drink and x.nat_color = this.@pet_color
}
one sig Dog, Fox, Horse, Zebra, Snail extends Pet {}

abstract sig Cigarette {
  cig_drink: one Drink,
  cig_color: one Color,
}{
  one this.~nat_cig
  one this.~house_cig
  one this.~pet_cig
  one x: Nationality | x.nat_cig = this and x.nat_drink = this.@cig_drink and x.nat_color = this.@cig_color
}
one sig OldGold, Chesterfield, Kool, LuckyStrike, Parliament extends Cigarette {}

abstract sig Drink {
  drink_color: one Color,
}{
  one this.~nat_drink
  one this.~house_drink
  one this.~pet_drink
  one this.~cig_drink
  one x: Nationality | x.nat_drink = this and x.nat_color = this.@drink_color
}
one sig Coffee, Tea, Milk, OrangeJuice, Water extends Drink {}

abstract sig Color {}{
  one this.~nat_color
  one this.~house_color
  one this.~pet_color
  one this.~cig_color
  one this.~drink_color
  one x: Nationality | x.nat_color = this
}
one sig Red, Green, Ivory, Yellow, Blue extends Color {}

fact{
  English.nat_color = Red
  Spanish.nat_pet = Dog
  Coffee.drink_color = Green
  Ukranian.nat_drink = Tea
  next[Ivory.~house_color] = Green.~house_color
  OldGold.~pet_cig = Snail
  Kool.cig_color = Yellow
  Milk.~house_drink = H3
  Norwegian.nat_house = H1
  Chesterfield.~house_cig.next_to = Fox.~house_pet
  Kool.~house_cig.next_to = Horse.~house_pet
  LuckyStrike.cig_drink = OrangeJuice
  Japanese.nat_cig = Parliament
  Norwegian.nat_house.next_to = Blue.~house_color
}

pred solution {}
run solution
