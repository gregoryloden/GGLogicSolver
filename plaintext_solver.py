# this transforms a file into the LL
from LogicLanguage import *
from solve import solve
import sys

def parse_file(filename):
  """ Parse a file written in plaintext logic language format that is horrifyingly undocumented and specific."""
  f = open(filename, 'r')
  header = f.readline()
  # parse the header
  tokens = header.split()
  num_cat = int(tokens[0])
  num_mem = int(tokens[1])
  ordered = bool(tokens[2])
  puzzle = Puzzle()
  # get the members, add them to the puzzle, and to the helper.
  helper = {}
  for x in range(num_cat):
    cat = Category(f.readline().strip(), num_mem, ordered)
    ordered = False
    for y in range(num_mem):
      mem_name = f.readline().strip()
      mem = Member(mem_name)
      cat.add(mem)
      helper[mem_name] = mem
    puzzle.categories.append(cat)
  # use reflection to read the rest of the lines as clues!
  # TODO fix it so it doesn't crash if there are empty lines at the end of the file
  for line in f.readlines():
    tokens = line.split()
    # special rules for Or. Hacky.
    if len(tokens) == 7 and tokens[3] == "Or":
      m1 = helper[tokens[0]]
      m2 = helper[tokens[2]]
      fun_string1 = tokens[1] + "(m1, m2)"
      m3 = helper[tokens[4]]
      m4 = helper[tokens[6]]
      fun_string2 = tokens[5] + "(m3, m4)"
      fun_string = "Or("+fun_string1+","+fun_string2+")"
    else: 
      m1=helper[tokens[0]]
      m2 = helper[tokens[2]]
      fun_string = tokens[1] + "(m1, m2)"
    puzzle.relationships.append(eval(fun_string))
  # return the puzzle object
  return puzzle

if __name__ == "__main__":
  # if called from the command line also solve the puzzle
  # intended for informed debugging only; may break in startling ways
  solve(parse_file(sys.argv[1]))

