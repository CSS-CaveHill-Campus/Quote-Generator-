from random import choice

with open("quotes.txt") as fp:
    lines = fp.readlines()

quotes = []

for line in lines:
    if line != "\n":
        quotes.append(line.replace("\n", ""))

print(choice(quotes))
