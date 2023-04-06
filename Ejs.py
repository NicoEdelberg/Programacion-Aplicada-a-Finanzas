def suma(x):
	s = 0
	for i in range(len(x)):
		s += x[i]
	return s

# suma(100)

# Funcion Recursiva
def sum_to(n):
	if n <= 0:
		return 0 #Basecase
	else:
		return n + sum_to(n - 1) # Recursive case

# # Compute the sum of the integers from 0 up to and including a value entered by the user
# num = int(input("Enter a non-negative integer: "))
# total = sum_to(num)
# print("The total of the integers from 0 up to and including", \
#       num, "is", total)

# Numeros de Fibonacci

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1

	return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Enter a non-negative integer: "))
# print("fibonacci(%d) is %d." % (n, fibonacci(n)))


# 174 Euclides MCD

def euclides(a, b):
		
	if b == 0:
		return a
	else:
		c = a % b
		if c == 0:
			return b
		a = c
		
	return euclides(b,a)

# a = int(input("Ingrese un numero a dividir:")) 
# b = int(input("Ingrese un numero divisor:"))
# print("El Maximo Comun Denominador es: ", euclides(a,b))

# 174 Euclides MCD con primos

def primos():
	x = 0
	

def euclides_primos (a, b):
	if b == 0:
		return a
	else:
		c = a % b
		if c == 0:
			return b
		a = c
	
	return euclides(b,a)


# 175 Decimal a Binario

def binario(n, numero_b):

	if n < 0:
		print("ERROR! Ingrese un numero positivo")

	if n >= 0:
		
		if n == 0:
			return print("El numero binario es: 0")

		if n == 1:
			return print("El numero binario es: 1")
		
		else:
			r = n % 2

			if r == 0:
				numero_b.insert(0, '0')
				nuevo = n / 2
			
			if r != 0:
				numero_b.insert(0, '1')
				nuevo = (n - r) / 2
			
			if nuevo == 1:
				numero_b.insert(0, '1')

				numero_b_string = ''
				for i in numero_b:
					numero_b_string += '' + i

				return numero_b_string

		return (binario(nuevo, numero_b))

# n = int(input("Ingrese un numero: "))
# numero_b = []

# print("El numero binario es: ", binario(n, numero_b))

# 183 Cadena de elementos de la tabla periodica

def cadena_elementos (elemento, l_elementos):

	if elemento not in l_elementos:
		print (elemento, 'no esta en la tabla periodica')
		return 
		# cadena_elementos(elemento)
	else:
		l_elemento_seleccionado = []
		for i in elemento:
			l_elemento_seleccionado.append(i)

		ultima_letra = l_elemento_seleccionado [-1]

		elemento_a_probar = []
		for i in l_elementos:
			for j in i:
				elemento_a_probar.append(j)

			if elemento_a_probar[0] == ultima_letra:
				
				nuevo_elemento = ''
				for i in elemento_a_probar:
					nuevo_elemento += 'i'
				return cadena_elementos(nuevo_elemento)


def ele (l_elementos):
	

	word_chain = []

	word_chain.append(l_elementos[0])

	for word in l_elementos:
		for char in word[0]:
			if char == word_chain[-1][-1]:
				word_chain.append(word)

	print(word_chain)



l_elementos = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 
	'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Californium', 
	'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copernicium', 'Copper', 'Curium', 
	'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium', 'Erbium', 'Europium', 'Fermium', 'Flerovium', 
	'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Hassium', 'Helium', 
	'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iridium', 'Iron', 'Krypton', 'Lanthanum', 'Lawrencium', 
	'Lead', 'Lithium', 'Livermorium', 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 
	'Mercury', 'Molybdenum', 'Moscovium', 'Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium', 
	'Nitrogen', 'Nobelium', 'Oganesson', 'Osmium', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Plutonium', 
	'Polonium', 'Potassium', 'Praseodymium', 'Promethium', 'Protactinium', 'Radium', 'Radon', 'Rhenium', 'Rhodium', 
	'Roentgenium', 'Rubidium', 'Ruthenium', 'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 
	'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 'Tennessine', 'Terbium', 'Thallium', 
	'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']		
ele(l_elementos)

# elemento = str(input("Ingrese el nombre del elemento quimico para armar la cadena: "))
# print(cadena_elementos(elemento))













