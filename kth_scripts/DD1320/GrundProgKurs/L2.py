def inmatning():
	x = 0
	väderlista = []
	while x!=12:
		i = input("Ange månad " + str(x+1))
		väderlista.append(i)
		x += 1

inmatning()