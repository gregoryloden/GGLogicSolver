from subprocess import call
from parse_output import parse_output
#fix this later
from LLImpl import puzzle

# puts things into als, gets the answer, reads things from out.xml
def main(imported_puzz = None):
  if imported_puzz:
    category = imported_puzz.categories[0].name
    inals = imported_puzz.alloy()
  else:
    category = puzzle.categories[0].name
    inals = puzzle.alloy()
  #write data to in.als
  f = open('in.als', 'w')
  f.write(inals)
  f.close()
  call(["java","-cp", "alloy4.2.jar:.","AlloyCompiler","in.als"])
  solution = parse_output(category)
  #display solution
  print solution
  return solution

if __name__ == "__main__":
  main()

