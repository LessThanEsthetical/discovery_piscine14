#!/usr/bin/python3

import numpy as np

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

def array_of_names(arr):
	arr = np.array([f"{k.capitalize()} {v.capitalize()}" for k, v in arr.items()])
	return list(arr)
	
def main():
	print(array_of_names(persons))

if __name__ == "__main__":
	main()
