#!/usr/bin/python3

import sys

def downcase_it(txt):
	txt = txt.lower()
	return txt

def main():
	if len(sys.argv) > 1:
		for i in range(1, len(sys.argv)):
			print(downcase_it(sys.argv[i]))
	else:
		print("None")

if __name__ == "__main__":
	main()
