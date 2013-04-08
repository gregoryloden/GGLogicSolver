# Python Logic Language implementation

class Puzzle(object):
  def __init__(self):
    self.categories = []
    self.relationships = []

  def alloy(self):
    # returns a string
    # optimization opportunity: more efficient string concatenation
    string = ""
    ordered_cat = None
    for category in self.categories:
      if category.ordered:
        string +="open util/ordering[" + category.name + "]\n"
        ordered_cat = category.name

    # create abstract signatures
    for index in range(len(self.categories)):
      before_names = [cat.name for cat in self.categories[:index]]
      after_names = [cat.name for cat in self.categories[index + 1:]]
      name = self.categories[index].name
      # try for a single pass through the lists for optimization later
      string += "abstract sig " + name + " {\n"
      for aname in after_names:
        string += "\t" + name.lower() + "_" + aname.lower() + " : one " + aname + ",\n"
      string += "} {\n" 
      for bname in before_names:
        string += "\tone this.~" + bname.lower() + "_" + name.lower() + "\n"
      if index != 0:
        firstname = self.categories[0].name
        string += "\tone x : " + firstname + " | x." + firstname.lower() + "_" + name.lower() + " = this"
        for aname in after_names:
          string += " and\n\t\tx." + firstname.lower() + "_" + aname.lower() + " = this.@" + name.lower() + "_" + aname.lower()
        string += "\n"
      string += "}\n\n"
      members = self.categories[index].members
      for member in members:
        string += "one sig " + member.name + " extends " + name + " {}\n"
      string += "\n"
      if self.categories[index].ordered:
        string += "fact {\n"
        string += "\tfirst = " +  members[0].name + "\n"
        for m1, m2 in zip(members[:-1], members[1:]):
          string += "\t" + m1.name + ".next = " + m2.name + "\n"
        string += "}\n\n"
      string += "\n"
    # create clues
    string += "fact {\n"
    for relationship in self.relationships:
      string += "\t" + relationship.alloy([cat.name for cat in self.categories], ordered_cat) + "\n"
    string += "}\n"
    string += "pred example {}\nrun example\n"
    return string
   
class Category(object):
  def __init__(self, name = "Category", amount = 5, ordered = False):
    self.amount = amount
    self.ordered = ordered
    self.members = []
    self.name = name

  def add(self, member):
    self.members.append(member)
    member.category = self

class Member(object):
  def __init__(self, name = "Object"):
    self.name = name
    self.category = None

class Relationship(object):
  def __init__(self, obj1 = None, obj2 = None):
   self.obj1 = obj1
   self.obj2 = obj2
  
  def get_field_name(self, order, cat1 = None, cat2 = None):
    cat1 = self.obj1.category.name if cat1 == None else cat1
    cat2 = self.obj2.category.name if cat2 == None else cat2
    if order.index(cat1) < order.index(cat2):
      return cat1.lower() + "_" + cat2.lower()
    else:
      return "~" + cat2.lower() + "_" + cat1.lower()


class Is (Relationship):
  def alloy(self, order, trash):
    fname = self.get_field_name(order)
    return self.obj1.name + "." + fname + " = " + self.obj2.name

class IsNot (Relationship):
  def alloy(self, order, trash):
    fname = self.get_field_name(order)
    return self.obj1.name + "." + fname + " != " + self.obj2.name

class Before (Relationship):
  def alloy(self, order, ordered_cat):
    part1 = self.obj1.name
    if self.obj1.category.name != ordered_cat:
      part1 += "." + self.get_field_name(order, cat2 = ordered_cat)
    part2 = self.obj2.name
    if self.obj2.category.name != ordered_cat:
      part2 += "." + self.get_field_name(order, cat1 = self.obj2.category.name, cat2 = ordered_cat)
    return part1 + " in " + part2 + ".prevs"

class After (Relationship):
  def alloy(self, order, ordered_cat):
    part1 = self.obj1.name
    if self.obj1.category.name != ordered_cat:
      part1 += "." + self.get_field_name(order, cat2 = ordered_cat)
    part2 = self.obj2.name
    if self.obj2.category.name != ordered_cat:
      part2 += "." + self.get_field_name(order, cat1 = self.obj2.category.name, cat2 = ordered_cat)
    return part1 + " in " + part2 + ".nexts"

class ImmBefore (Relationship):
  def alloy(self, order, ordered_cat):
    part1 = self.obj1.name
    if self.obj1.category.name != ordered_cat:
      part1 += "." + self.get_field_name(order, cat2 = ordered_cat)
    part2 = self.obj2.name
    if self.obj2.category.name != ordered_cat:
      part2 += "." + self.get_field_name(order, cat1 = self.obj2.category.name, cat2 = ordered_cat)
    return part1 + " = " + part2 + ".prev"

class ImmAfter (Relationship):
  def alloy(self, order, ordered_cat):
    part1 = self.obj1.name
    if self.obj1.category.name != ordered_cat:
      part1 += "." + self.get_field_name(order, cat2 = ordered_cat)
    part2 = self.obj2.name
    if self.obj2.category.name != ordered_cat:
      part2 += "." + self.get_field_name(order, cat1 = self.obj2.category.name, cat2 = ordered_cat)
    return part1 + " = " + part2 + ".next"

class Or (Relationship):
  def alloy(self, order, ordered_cat):
    part1 = self.obj1.alloy(order, ordered_cat)
    part2 = self.obj2.alloy(order, ordered_cat)
    return part1 + " or " + part2
