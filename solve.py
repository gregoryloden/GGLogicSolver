from subprocess import call
from parse_output import parse_output
# puts things into als, gets the answer, reads things from out.xml
def main(categories):
  # sometime later parse to als
  # save file as in.als
  category = "Nationality"
  call(["java","-cp", "alloy4.2.jar:.","AlloyCompiler","in.als"])
  solution = parse_output(category)
  #display solution
  print solution

if __name__ == "__main__":
  main(None)

