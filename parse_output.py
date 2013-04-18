import os
def parse_output(category):
    """ parse the output of the Alloy compiler from XML into a list of lists."""
  label = "this/" + category
  import xml.etree.ElementTree as ET
  # get the tree
  # file name is hard coded
  tree = ET.parse(os.getcwd()+"/out.xml")
  # get the root of the tree so we can work with it
  root = tree.getroot()
  # find the ID of the item we want
  pid = root.find(".//sig[@label='"+label+"']").attrib["ID"]
  # find the fields
  elems = root.findall(".//field[@parentID='"+pid+"']")
  # find the categories
  types = root.findall(".//sig[@parentID='"+pid+"']")
  # parse the categories from xml
  types = [x.attrib["label"][5:] for x in types]
  # parse the types
  solution = {}
  for tipe in types:
    solution[tipe] = [tipe]

  for elem in elems:
    tups = elem.findall("tuple")
    tups = [(tup.find("atom[1]").attrib["label"][:-2], tup.find("atom[0]").attrib["label"][:-2]) for tup in tups]
    for k, v in tups:
      solution[k].append(v)

  # return the solution as a list of lists
  return solution.values()

