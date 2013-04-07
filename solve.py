from subprocess import call
from parse_output import parse_output
#fix this later
import zebra as data

# puts things into als, gets the answer, reads things from out.xml
def main():
  category = data.puzzle.categories[0].name
  inals = data.puzzle.alloy()
  #write data to in.als
  f = open('in.als', 'w')
  f.write(inals)
  f.close()
  call(["java","-cp", "alloy4.2.jar:.","AlloyCompiler","in.als"])
  solution = parse_output(category)
  #display solution
  print solution

if __name__ == "__main__":
  main()

