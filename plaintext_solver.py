# this transforms a file into the LL
from LogicLanguage import *
from solve import solve
import sys

def parse_file(filename):
  f = open(filename, 'r')
  header = f.readline()
  tokens = header.split()
  num_cat = int(tokens[0])
  num_mem = int(tokens[1])
  ordered = bool(tokens[2])
  puzzle = Puzzle()
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
  for line in f.readlines():
    tokens = line.split()
    m1 = helper[tokens[0]]
    m2 = helper[tokens[2]]
    fun_string = tokens[1] + "(m1, m2)"
    puzzle.relationships.append(eval(fun_string))
  return puzzle

if __name__ == "__main__":
  solve(parse_file(sys.argv[1]))

