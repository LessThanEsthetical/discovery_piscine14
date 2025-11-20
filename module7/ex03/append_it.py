#!/usr/bin/python3

import sys
import re

if len(sys.argv) > 1:
	for i in range(1, len(sys.argv)):
		if re.search("ism$", sys.argv[i]) : continue
		print(sys.argv[i] + "ism")
else:
	print("None")
