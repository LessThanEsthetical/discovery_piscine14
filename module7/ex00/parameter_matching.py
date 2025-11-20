#!/usr/bin/python3

import sys

if int(len(sys.argv)) == 2:

	param = input("What was the parameter? ")
	if param == sys.argv[1]:
		print("Good job!")
	else:
		print("Nope, sorry...")
else:
	print("None")
