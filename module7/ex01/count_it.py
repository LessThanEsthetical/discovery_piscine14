#!/usr/bin/python3

import sys

if int(len(sys.argv[1:])) > 0:
	print("Parameters:", int(len(sys.argv[1:])))
	for i in range(1, len(sys.argv)):
		print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:
	print("None")
