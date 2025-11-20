#!/usr/bin/python3

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

def find_the_redheads(arr):
	arr = list(filter(lambda x: arr[x] == "red", arr))
	return arr

def main():
	print(find_the_redheads(dupont_family))

if __name__ == "__main__":
	main()
