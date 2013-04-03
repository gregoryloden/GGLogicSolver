# Python Logic Language implementation

class Puzzle(object):
  def __init__(self):
    self.categories = []

  def alloy(self):
    # returns a string
    # optimization opportunity: more efficient string concatenation
    string = ""
    # create abstract signatures
    for index in range(len(self.categories)):
      before_names = [cat.name for cat in self.categories[:index]]
      after_names = [cat.name for cat in self.categories[index + 1:]]
      name = self.categories[index]
      # try for a single pass through the lists for optimization later
      string += "abstract sig " + name + " {\n"
      for aname in after_names:
        string += "\t" + name.lower() + "_" + aname.lower() + " : one " + aname + ",\n"
      string += "} {" 
      for bname in before_names:
        string += "\t this.~" + bname.lower() + "_" + name.lower() + "\n"
      if index != 0:
        firstname = self.categories[0].name
        string += "\tall x : " + firstname + " | x." + firstname.lower() + "_" + name.lower() + " = this"
        for aname in after_names:
          string += "and\n\t\tx." + firstname.lower() + "_" + aname.lower() + " = this.@" + name.lower() + "_" + aname.lower()
        string += "\n"
      string += "}\n\n"
      for member in self.categories[index].members:
        string += "one sig " + member.name + " extends " + name + " {}\n"
      string += "\n\n"

    # if ordered, add ordering
    # create clues

class Category(object):
  def __init__(self, name = "Category", amount = 5, ordered = False):
    self.amount = amount
    self.ordered = ordered
    self.members = []
    self.name = name

class Member(object):
  def __init__(self, name = "Object"):
    self.name = name

class Relationship(object):
  def __init__(self, obj1 = None, obj2 = None):
   self.obj1 = obj1
   self.obj2 = obj2

class Is (Relationship):
  pass

class IsNot (Relationship):
  pass

class Before (Relationship):
  pass

class After (Relationship):
  pass

class ImmBefore (Relationship):
  pass

class ImmAfter (Relationship):
  pass
