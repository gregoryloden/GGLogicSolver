# Python Logic Language implementation

class Category(object):
  def __init__(self, name = "Category", amount = 5, ordered = True):
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
