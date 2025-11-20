#!/usr/bin/python3

class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
}

class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13
}

def average(summ):
	summ = sum([i for i in summ.values()]) / len(summ.values())
	return summ

def main():
	print(f"Average for class 3B: {average(class_3B)}.")
	print(f"Average for class 3C: {average(class_3C)}.")

if __name__ == "__main__":
	main()
