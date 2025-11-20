#!/usr/bin/python3

import sys

def shrink(txt):
	txt = txt[:8]
	return txt

def enlarge(txt):
	txt = (txt + "ZZZZZZZZ")[:8]
	return txt

def main():
	for i in sys.argv[1:]:
		if len(i) > 8:
			print(shrink(i))
		elif len(i) < 8:
			print(enlarge(i))
		else:
			print(i)

if __name__ == "__main__":
	main()
