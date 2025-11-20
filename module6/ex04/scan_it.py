#!/usr/bin/python3

import sys
import re

print(len(search)) if int(len(sys.argv)) == 3 and [search := re.findall(sys.argv[1], sys.argv[2])] else print("None")
