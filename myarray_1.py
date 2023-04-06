class myarray():
	"""La clase myarray toma una lista de numeros, la cantidad de filas, la canttidad de columnas
	y la forma en la que va a ser ordenada (by_row). En el caso en que esta ultima variable sea True 
	== > primero completara las filas y luego las columnas
	"""

	def __init__ (self, row, col, by_row, lista):
		self.lista = lista
		self.row = row
		self.col = col
		self.by_row = by_row

	def lista_matriz(self, row, col, by_row, lista):
		"""Este metodo toma las matriz dada por el usuario y la conviere en un diccionario 
		donde las claves son el numero de fila arrancando por el 1 y dentro contiene los valores
		de esa fila en forma de lista
		"""
		dict_matriz = {}

		m_lista = self.lista.copy()

		if self.by_row == True:

			for i in range(1, (self.row+1)):
				nombre_lista = str(i)
				numeros = []
				parto_m_lista = m_lista[:self.col]
				dict_matriz[nombre_lista] = parto_m_lista

				for j in range(0, len(parto_m_lista)):
					m_lista.pop(0)

		elif self.by_row == False:

			contador_local = 0
			for i in range(1, (self.row+1)):
				nombre_lista = str(i)
				numeros = []

				parto_m_lista = m_lista[contador_local::row]
				print(parto_m_lista)
				dict_matriz[nombre_lista] = parto_m_lista
				contador_local+=1

		return dict_matriz

	def get_pos(self, j, k):
		"""
		Devuelve un valor m en lista (la matriz del ususario)
		j = filas
		k = columnas
		"""
		if j <= row and j > 0 and k <= col and k > 0:
			fila = dict_matriz[str(j)]
			posisicon_col = k-1
			valor = fila[posisicon_col]

			contador_local = 0
			for i in lista:
				if i == valor:
					break

				contador_local += 1

			posicion_m = contador_local

			salida = (f'La posicion {j,k} en la matriz es el lugar {contador_local} en la lista de la matriz')

		else:
			salida = (f'La posicion {j,k} no se encuentra en la matriz')

		return salida

	def get_coords(self, m):
		"""
		Devuelve las coordenadas en la matriz del elemento dado
		m = un elemento de la matriz
		"""
		if m in lista:
			coords = []

			for key in dict_matriz:
				for value in dict_matriz[key]:
					if value == m:
						coords.append(int(key))
						coords.append(value)
						break

			salida = (f'Las coordenadas del elemento {m} son {coords}')
		
		else:
			salida = (f'El elemento {m} no se encuentra en la matiz')

		return salida

	def switch(self):
		"""Primero cambia el orden del la lista que provee por el usuario
		Luego invierte el valor booleano de by_row (o sea, lo invierte)
		y retorna la nueva matriz en forma de diccionario
		"""
		switch_lista = []

		for i in lista:
			switch_lista.insert(0,i)

		print(switch_lista)

		if by_row == True:
			nuevo_dict_matriz = self.lista_matriz(row, col, False, switch_lista)

		elif by_row == False:
			nuevo_dict_matriz = self.lista_matriz(row, col, True, switch_lista)

		return (f'Despues del switch la nueva matriz es: {nuevo_dict_matriz}')

	def get_row(self, j):
		"""Devuelve todos los valores de que estan la la fila j en forma de lista
		"""
		
		l_keys = list(dict_matriz.keys())

		if j not in l_keys:
			salida = (f'La fila {j} no esta dentro de la matriz')
		else:
			fila = dict_matriz[str(j)]
			salida = (f'La fila {j} contiene los valores {fila}')

		return salida

	def get_col(self, k):
		"""Devuelve todos los valores de que estan la la columna k en forma de lista 
		"""

		values_col = []

		if k <= col and k > 0:
			for key in dict_matriz:
				valores = dict_matriz[key]
				values_col.append(valores[k-1])
			salida = (f'La columna {k} contiene los valores {values_col}')

		else:
			salida = (f'La columna {k} no esta dentro de la matriz')

		return salida

	def elem(self,j,k):
		"""Devuelve el elemento que esta en las coordenadas (j,k) 
		j = filas
		k = columnas  
		"""
		
		if j <= row and j > 0 and k <= col and k > 0:
			fila = dict_matriz[str(j)]
			posisicon_col = k-1
			valor = fila[posisicon_col]

			salida = (f'Las coordenadas {j,k} corresponden al elemento {valor}')
		
		else: 
			salida = (f'Las coordenadas {j,k} no se encuentran en la matiz')
		
		return salida

	def del_row(self,j):
		"""El metodo borra la fila j que le pasa el usuario
		"""

		if j <= row and j > 0:

			nuevo_dict_matriz = dict_matriz.copy()
			del nuevo_dict_matriz[str(j)]

			salida = (f'Se elimino la fila {j}: {dict_matriz[str(j)]} de la matriz\nLa nueva matriz: {nuevo_dict_matriz}')

		else:
			salida = (f'La fila {j} no se encuentra en la matriz')

		return salida

	def del_col (self, k):
		"""El metodo borra la columna k que le pasa el usuario
		"""

		if k <= col:
			nuevo_dict_matriz = dict_matriz.copy()
			l_temp = []

			for key in dict_matriz:
				contador_local = 0
				for value in dict_matriz[key]:
					if contador_local == k-1:
						l_temp.append(value)
						nuevo_dict_matriz[key].remove(value)
						break

					else:
						contador_local += 1

			salida = (f'Se elimino la columna {k}: {l_temp} de la matriz\nLa nueva matriz: {nuevo_dict_matriz}')

		else:
			salida = (f'La columna {k} no se encuentra en la matriz')

		return salida

	def swap_rows(self, j, k):
		"""El metodo intercambia dos filas en la matriz
		"""

		if j <= row  and j > 0 and k <= row and k > 0:
			nuevo_dict_matriz = dict_matriz.copy()

			values_j = nuevo_dict_matriz[str(j)]
			values_k = nuevo_dict_matriz[str(k)]

			nuevo_dict_matriz[str(j)] = values_k
			nuevo_dict_matriz[str(k)] = values_j

			salida = (f'Se intercambieron las filas {j,k}\nLa nueva matriz: {nuevo_dict_matriz}')

		else:
			salida = (f'Las filas {j,k} no se encuntran en la matriz')

		return salida

	def swap_cols (self, l, m):
		"""El metodo intercambia dos columnas en la matriz
		"""

		if l <= col  and l > 0 and m <= col and m > 0:
			nuevo_dict_matriz = dict_matriz.copy()

			for key in nuevo_dict_matriz:
				nuevo_dict_matriz[key][l-1], nuevo_dict_matriz[key][m-1] =  nuevo_dict_matriz[key][m-1], nuevo_dict_matriz[key][l-1]

			salida = (f'Se intercambiaron las columnas {l,m}\nLa nueva matriz: {nuevo_dict_matriz}')

		else:
			salida = (f'Las columnas {j,k} no se encuntran en la matriz')

		return salida

	def scale_row(self, j, x):
		"""El metodo multiplica a los elementos de una fila j por un escalar x
		"""

		if j <= row and j > 0 and (isinstance(x, float) or isinstance(x, int)):
			nuevo_dict_matriz = dict_matriz.copy()

			values_j = nuevo_dict_matriz[str(j)]
			values_j_x = []

			for i in values_j:
				multiplicado = i * x
				values_j_x.append(multiplicado)

			nuevo_dict_matriz[str(j)] = values_j_x

			salida = (f'Se multimplico la fila por {j} por el escalar {x}\nNueva matriz: {nuevo_dict_matriz}')

		elif isinstance(x, str):	
			slida = (f'El escalar {x} es un string tiene que ser float o integer')

		else:
			salida = (f'{j} no es una fila de la matriz')

		return salida

	def scale_col(self, k, y):
		"""El metodo multiplica a los elementos de una columna k por un escalar y
		"""

		dict_matriz = {'1': [1,2,3], '2': [4,5,6], '3': [7,8,9]}

		if k <= col and k > 0 and (isinstance(y, float) or isinstance(y, int)):
		    nuevo_dict_matriz = dict_matriz.copy()

		    for key in nuevo_dict_matriz:
		        contador_local = 0
		        for value in nuevo_dict_matriz[str(key)]:
		            if k-1 == contador_local:
		                nuevo_dict_matriz[key][k-1] *= y
		            contador_local += 1
		                
		    salida = (f'Se multimplico en la columna {k} por el escalar {y}\nNueva matriz: {nuevo_dict_matriz}')

		elif isinstance(y, str):    
		    salida = (f'El escalar {y} es un string tiene que ser float o integer')

		else:
		    salida = (f'{k} no es una fila de la matriz')

		return salida

	def transpose(self):
		"""El metodo intercambia las filas de una matriz por sus columnas
		"""

		nuevo_dict_matriz = {}

		for key, valores in dict_matriz.items():
			for i, valor in enumerate(valores):
				if i + 1 not in nuevo_dict_matriz:
					nuevo_dict_matriz[i+1] = []
				nuevo_dict_matriz[i+1].append(valor)

		return (f'La matriz transpuesta de {dict_matriz} \nes: {nuevo_dict_matriz}')

	def flip_rows(self):
		"""El metodo de intercambia las filas de la matriz de forma especular
		o sea, desde la fila del medio hacia afuera
		"""
		nuevo_dict_matriz = dict_matriz.copy()

		if row % 2 == 0:
			contador_local = 0
			for j in range(1, int(row/2+1)):
				values_j = nuevo_dict_matriz[str(j)]
				values_k = nuevo_dict_matriz[str(row - contador_local)]

				nuevo_dict_matriz[str(j)] = values_k
				nuevo_dict_matriz[str(row - contador_local)] = values_j
				contador_local += 1
	
		elif row % 2 != 0:
			contador_local = 0
			for j in range(1, int(((row/2+0.5)))):
				values_j = nuevo_dict_matriz[str(j)]
				values_k = nuevo_dict_matriz[str(row - contador_local)]

				nuevo_dict_matriz[str(j)] = values_k
				nuevo_dict_matriz[str(row - contador_local)] = values_j
				contador_local += 1
	
		salida = (f'Se cambiaron las filas especularmente \nLa nueva matriz: {nuevo_dict_matriz}')

		return salida

	# def flip_cols(self):
	# 	"""El metodo de intercambia las columnas de la matriz de forma especular
	# 	o sea, desde la columna del medio hacia afuera
	# 	"""
	# 	nuevo_dict_matriz = dict_matriz.copy()

	# 	if col % 2 == 0:

	# 	elif col % 2 != 0:

	def det(self):
		"""El metodo calcula el determinante de la matriz de forma recursiva hasta 
		tener una matriz de 1x1 donde el determinante es el mismo numero
		"""
		determinante = 0

		k = col

		if row == col:
			if k == 1:
					self.elem(1,1) * slef.elem(2,2) - self.elem(1,2) * self.elem(2,1)

			else:
				for i in range(1, k):
					nuevo_dict_matriz = dict_matriz
					nuevo_dict_matriz = self.del_row(1), self.del_col(i)
					print(nuevo_dict_matriz)
					# nuevo_dict_matriz = self.del_col(i)
					determinante += self.elem(1,i) * ((-1) ** (1 + i)) * self.det()


		return determinante

	def __add__(self, B):

		if isinstance(B, list) and len(B) == len(lista):
			m_lista = lista.copy()
			m_B = B.copy()

			nueva_matriz = []

			contador_local = 0
			for i in m_B:
				add = m_B[contador_local] + m_lista[contador_local]
				nueva_matriz.append(add)

				contador_local += 1

			lista_fila_B = self.lista_matriz(row, col, by_row, nueva_matriz)

			# print(nueva_matriz)
			# print(lista_fila_B)

			salida = (f'La nueva matriz: {lista_fila_B}')

		else:
			salida = (f'B: no es una lista de numeros')

		return salida

	def __sub__(self, B):

		if isinstance(B, list) and len(B) == len(lista):
			m_lista = lista.copy()
			m_B = B.copy()

			nueva_matriz = []

			contador_local = 0
			for i in m_B:
				sub = m_B[contador_local] - m_lista[contador_local]
				nueva_matriz.append(sub)

				contador_local += 1

			lista_fila_B = self.lista_fila(row, col, by_row, nueva_matriz)

			# print(nueva_matriz)
			# print(lista_fila_B)

			salida = (f'La nueva matriz: {lista_fila_B}')

		else:
			salida = (f'B: no es una lista de numeros')

		return salida


lista = [1, 2, 3, 4, 5, 6,7, 8, 9]

B = [1, 2, 3, 4, 5, 6, 7, 8, 9]

row = 3

col = 3

by_row = True



z = myarray(row, col, by_row, lista)

dict_matriz = z.lista_matriz(row, col, by_row, lista)

print(z.__add__(B))






