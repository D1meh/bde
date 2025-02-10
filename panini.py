PANINI_NUT = 2.5
PANINI_JAMBON_FROMAGE = 3.5
PANINI_TOMATE_MOZZA_PESTO = 4
PANINI_POULET_CHEDDAR = 4

nut = float(input("Panini nutella:"))
jambon = float(input("Panini jambon fromage:"))
tomate_mozza = float(input("Panini tomate mozza pesto:"))
poulet_cheddar = float(input("Panini poulet cheddar:"))
payment = input("Mode de paiement (CB/ESP):")

total = (PANINI_NUT * nut) + (PANINI_JAMBON_FROMAGE * jambon) + (PANINI_TOMATE_MOZZA_PESTO * tomate_mozza) + (PANINI_POULET_CHEDDAR * poulet_cheddar)

with open("sold_panini", "a") as file:
	file.write(f"{total} {payment}\n")