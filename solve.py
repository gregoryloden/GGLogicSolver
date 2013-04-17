from subprocess import call
from parse_output import parse_output
#fix this later
from LLImpl import puzzle
from os import getcwd

# puts things into als, gets the answer, reads things from out.xml
def solve(imported_puzz = None):
  cwd = getcwd()
  if imported_puzz:
    category = imported_puzz.categories[0].name
    inals = imported_puzz.alloy()
  else:
    category = puzzle.categories[0].name
    inals = puzzle.alloy()
  #write data to in.als
  f = open(cwd+"\\in.als", 'w')
  f.write(inals)
  f.close()
  call(["java","-cp", cwd+"\\alloy4.2.jar:"+cwd,cwd+"\\AlloyCompiler",cwd+"\\in.als"])
  solution = parse_output(category)
  #display solution
  widths = [max(len(value) for value in column) + 4 for column in zip(*solution)]
  for line in solution:
    print(''.join('%-*s' % item for item in zip(widths, line)))
  return solution

if __name__ == "__main__":
  solve()

