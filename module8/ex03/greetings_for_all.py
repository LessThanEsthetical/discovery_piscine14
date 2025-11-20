#!/usr/bin/python3

ls = ["Alexandra", "Will", "", 42, 432.3]

def greetings(txt = "noble stranger"):
	if isinstance(txt, int|float):
		print("Error! That was not a name.")
	elif not txt:
		greetings()
	else:
		print(f"Hello, {txt}.")

def main():
	for i in ls:
		greetings(i)

if __name__ == "__main__":
	main()
