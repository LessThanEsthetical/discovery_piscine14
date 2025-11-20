#!/usr/bin/python3

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(ls):
	ls = ls.values()
	ls = sorted(ls, lambda x: x["date_of_birth"])
	return f"{ls['name']} is a great scientist born in {ls['date_of_birth']}."

def main():
	print(famous_births(women_scientists))

if __name__ == "__main__":
	main()
