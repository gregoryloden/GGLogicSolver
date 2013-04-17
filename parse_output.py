import os
def parse_output(category):
  label = "this/" + category
  import xml.etree.ElementTree as ET
  tree = ET.parse(os.getcwd()+"/out.xml")
  root = tree.getroot()
  pid = root.find(".//sig[@label='"+label+"']").attrib["ID"]
  elems = root.findall(".//field[@parentID='"+pid+"']")
  types = root.findall(".//sig[@parentID='"+pid+"']")
  types = [x.attrib["label"][5:] for x in types]
  solution = {}
  for tipe in types:
    solution[tipe] = [tipe]

  for elem in elems:
    tups = elem.findall("tuple")
    tups = [(tup.find("atom[1]").attrib["label"][:-2], tup.find("atom[0]").attrib["label"][:-2]) for tup in tups]
    for k, v in tups:
      solution[k].append(v)

  return solution.values()

