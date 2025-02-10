total = 0
cb = 0
esp = 0

with open("sold_panini") as f:
	for line in f:
		price = float(line.split()[0])
		total += price
		
		if "CB" in line:
			cb += price
		else:
			esp += price

print(f"Total: {total} ")
print(f"CB: {cb} ")
print(f"ESP: {esp} ")