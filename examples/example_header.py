import re
import os
cwd = os.getcwd()
if re.match(".*examples", cwd):
  cwd = cwd[:-8]
else:
  cwd += "/"

import sys
sys.path.append(cwd)
