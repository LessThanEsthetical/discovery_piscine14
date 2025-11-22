#!/usr/bin/python3

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(ls):
	ls = dict(sorted(ls.items(), key=lambda x: x[1]["date_of_birth"]))
	for i in ls.values():
		yield f"{i['name']} is a great scientist born in {i['date_of_birth']}."

def main():
	print(*(i for i in famous_births(women_scientists)), sep="\n")

if __name__ == "__main__":
	main()
