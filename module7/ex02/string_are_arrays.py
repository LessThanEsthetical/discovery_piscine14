#!/usr/bin/python3

import sys
import re

if int(len(sys.argv)) == 2 and re.findall("z", sys.argv[1]):
	print("".join(re.findall("z", sys.argv[1])))
else:
	print("None")
