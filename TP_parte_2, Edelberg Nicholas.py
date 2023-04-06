class myarray():

	def __init__(self, elems, r, c, by_row):
		self.elems = elems
		self.r = r
		self.c = c
		self.by_row = by_row

	def get_pos(self, j,k):
		"""Funcion en la que se ponen como parametros las coordenadas de un elemento de la matriz y se devuelve la posicion del elemento en la lista, elems
		"""
		p = 0
		if self.by_row == True: 
			for i in range(0, self.r): 
				if i == j:
					p = i * self.c + k 
		else: 
			for i in range(self.c):
				if i == k: 
					p = i * self.r + j
		return p

	def get_coords(self, p):
		""""Funcion que toma como parametro la posicion de un elemento en la lista, elems y devuelve las coordenadas del elemento en la matriz"""
		if self.by_row == True: 
			j = p // self.c
			k = p % self.c

		else : 
			j = p // self.r
			k = p % self.r
		return (j,k)

	def switch(self):
		""""Funcion que altera el orden de los elementos de la lista, elems y cambia el valor de la variable by_row por su valor opuesto"""
		new_elems = self.elems[::-1] 
		new_by_row = not self.by_row  
		return myarray(new_elems, self.r, self.c, new_by_row)

	def get_row(self, j):
		""""Funcion que toma como parametro un numero de fila y te devuelve los elementos de la fila """
		if self.by_row ==True: 
			start = j * self.c
			end = start + self.c
			salida = self.elems[start:end:]

		else: 
			start = j 
			end = (self.r * self.c) + start 
			salida = self.elems[start:end:self.r]
		return salida

	def get_col(self, k): 
		""""Funcion que toma como parametro un numero de columna y te devuelve los elementos de la fila """
		if self.by_row == True: 
			start = k
			end = (self.r * self.c) + start 
			salida = self.elems[start:end:self.c]

		else : 
			start = k * self.r
			end = start + self.r
			salida = self.elems[start:end:]
		return salida

	def get_elem(self, i):
		""""Funcion que toma como parametro la posicion de un elemento de la matriz y te devuelve el valor del elemento """
		j,k = i
		if self.by_row == True : 
			row = self.get_row(j)
			salida = row[k]

		else: 
			col = self.get_col(k)
			salida = col[j]
		return salida

	def del_row (self, j):
		""""Funcion que toma como parametro un numero de fila para poder borrar dicha fila y te devuelve los elementos de la matriz que no fueron eliminados """
		elems = []
		for i in range(len(self.elems)):
			if self.get_coords(i)[0] != j:
				elems.append(self.elems[i])
		else:
			pass

		return myarray(elems, self.r, self.c-1, self.by_row)

	def del_col (self, k):
		""""Funcion que toma como parametro un numero de columna para poder borrar dicha fila y te devuelve los elementos de la matriz que no fueron eliminados """
		elems = []
		for i in range(len(self.elems)):
			if self.get_coords(i)[1] != k:
				elems.append(self.elems[i])
		else:
			pass

		return myarray(elems, self.r, self.c-1, self.by_row)

	def swap_rows(self, j , k):
		""""Funcion que toma como parametro dos filas de la matriz y las intercambia de poscion """
		elems_2 = self.elems.copy()
		for i in range (self.c) : 
			row1 = self.get_pos(j, i)
			row2 = self.get_pos(k, i)
			x = elems_2[row1]
			elems_2[row1] = elems_2[row2]
			elems_2[row2] = x
		return elems_2

	def swap_cols (self, l, m):
		""""Funcion que toma como parametro dos columnas de la matriz y las intercambia de poscion """
		elems_2 = self.elems.copy()
		for i in range (self.r) : 
			col1 = self.get_pos(i, l)
			col2 = self.get_pos(i, m)
			x = elems_2[col1]
			elems_2[col1] = elems_2[col2]
			elems_2[col2] = x
		return elems_2

	def scale_row (self, j, x):
		""""Funcion que toma como parametro, una fila de la matriz y un numero por el cual va a multiplicar la fila ingresada de la matriz"""
		elems_2 = self.elems.copy()
		row = self.get_row(j)
		for i, e in enumerate(row) : 
			p_row = self.get_pos(j, i)
			elems_2[p_row] = e * x
		return elems_2

	def scale_col (self, k, y):
		""""Funcion que toma como parametro, una columna de la matriz y un numero por el cual va a multiplicar la columna ingresada de la matriz"""
		elems_2 = self.elems.copy()
		col = self.get_col(k)
		for i, e in enumerate(col) : 
			p_col = self.get_pos(i , k)
			elems_2[p_col] = e * y
		return elems_2

	def transpose(self): 
		""""Funcion que cambia las columnas por las filas y las filas por las columnas, es decri que calcula la transversa de la matriz"""
		new_list = []
		count = 0
		while count < self.c:
			new_list.extend(self.elems[count::self.c])
			count += 1
		return myarray(new_list, self.c, self.r, self.by_row)

	def flip_row(self):
		""""Funcion que devuelvenuna copia del los elemementos de la clase, pero reflejado especularmente en sus filas."""
		lista = []
		for i in range (self.r-1, -1, -1): 
			row = self.get_row(i)
			for e in row : 
				lista.append(e)
		return lista

	def flip_cols(self): 
		""""Funcion que devuelvenuna copia del los elemementos de la clase, pero reflejado especularmente en sus columnas."""
		lista = []
		for i in range (self.c-1, -1, -1) : 
			row = self.get_col(i)
			for e in row : 
				lista.append(e)
		return lista

	def __add__(self, b):
		"""Este metodo permite al ususario sumarle un escalar a su matriz original (matriz + escalar)
		"""
			
		if isinstance(b, int):
			nuevo_elems = []

			for i in self.elems:
				add = i + b
				nuevo_elems.append(add)
			salida = myarray(nuevo_elems, self.r, self.c, self.by_row).elems

		else:
			salida = (f'{b} no es un integer')

		return salida

	def __radd__(self, b):
		"""Este metodo permite al ususario sumarle un escalar a su matriz original (escalar + matriz)
		"""

		if isinstance(b, int):
			nuevo_elems = []

			for i in self.elems:
				add = i + b
				nuevo_elems.append(add)
			salida = myarray(nuevo_elems, self.r, self.c, self.by_row).elems

		else:
			salida = (f'{b} no es un integer')

		return salida

	def __sub__(self, b):
		"""Este metodo permite al ususario restarle un escalar a su matriz original (matriz + escalar)
		"""

		if isinstance(b, int):
			nuevo_elems = []

			for i in self.elems:
				add = i - b
				nuevo_elems.append(add)
			salida = myarray(nuevo_elems, self.r, self.c, self.by_row).elems

		else:
			salida = (f'{b} no es un integer')

		return salida

	def __rsub__ (self, b):
		"""Este metodo permite al ususario sumarle un escalar a su matriz original (escalar + matriz)
		"""

		if isinstance(b, int):
			nuevo_elems = []

			for i in self.elems:
				add = i - b
				nuevo_elems.append(add)
			salida = myarray(nuevo_elems, self.r, self.c, self.by_row).elems

		else:
			salida = (f'{b} no es un integer')

		return salida

	def __pow__(self, b):
		"""Este metodo permite al ususario potencia su matriz a un escalar (matriz ** escalar)
		"""

		matriz_1 = myarray([1,2,3,4,5,6,7,8,9], 3, 3, True)
		matriz_2 = myarray([1,2,3,4,5,6,7,8,9], 3, 3, True)

		if isinstance(b, int):
			if b == 1:
				salida = matriz_1

			elif b == 0:
				salida = 1

			else:
				for i in range((b-1)):
					x = matriz_1 @ matriz_2
					matriz_2 = myarray(x, self.r, self.c, self.by_row)

			salida = x

		else:
			salida = (f'{b} no es una lista (matriz)')

		return salida

	def __rpow__(self, b):
		"""Este metodo permite al ususario potencia su matriz a un escalar (escalat ** matriz)
		"""

		matriz_1 = myarray([1,2,3,4,5,6,7,8,9], 3, 3, True)
		matriz_2 = myarray([1,2,3,4,5,6,7,8,9], 3, 3, True)

		if isinstance(b, int):
			if b == 1:
				salida = matriz_1

			elif b == 0:
				salida = 1

			else:
				for i in range((b-1)):
					x = matriz_1 @ matriz_2
					matriz_2 = myarray(x, self.r, self.c, self.by_row)

			salida = x

		else:
			salida = (f'{b} no es una lista (matriz)')

		return salida

	def __mul__(self, b):
		"""Este metodo permite al ususario multiplicar su matriz por un escalar (matriz * escalar)
		"""

		if isinstance(b, int) or isinstance(b, float):
			nuevo_elems = []

			for i in self.elems:
				nuevo_elems.append(i * b)
			salida = nuevo_elems
		else:
			print(f'{b} no es un numero')
			salida = None

		return salida

	def __rmul__(self, b):
		"""Este metodo permite al ususario multiplicar su matriz por un escalar (escalar * matriz)
		"""

		if isinstance(b, int) or isinstance(b, float):
			nuevo_elems = []

			for i in self.elems:
				nuevo_elems.append(i * b)
			salida = nuevo_elems
		else:
			print(f'{b} no es un numero')
			salida = None

		return salida

	def __matmul__(self, b):
		"""Este metodo permite al ususario multiplicar su matriz por otra matriz (matriz @ matriz_2)
		"""

		res = []
		for i in range(0, matriz.r):
			for j in range(0, matriz.c):
				prod = 0
				fila = matriz.get_row(i)
				columna = b.get_col(j)

				for k in range(0, len(fila)):
					prod += fila[k] * columna[k]

				res.append(prod)

		return res

	def swap_rows_identidad(self, j, k):
		"""Este metodo permite al ususario intercambiar filas, mutiplicando su matriz por la matriz de identidad
		"""

		identidad = creador_identidad(self.r, self.c, self.by_row)
		m_identidad = identidad.swap_rows(j, k)

		nueva_matriz = myarray(m_identidad, self.r, self.c, self.by_row) @ matriz

		return nueva_matriz

	def swap_cols_identidad(self, l, m):
		"""Este metodo permite al ususario intercambiar columnas, mutiplicando su matriz por la matriz de identidad
		"""

		identidad = creador_identidad(self.r, self.c, self.by_row)
		m_identidad = identidad.swap_cols(l, m)

		nueva_matriz = matriz @ myarray(m_identidad, self.r, self.c, self.by_row)

		return nueva_matriz

	def del_row_identidad(self, j):
		"""Este metodo permite al ususario borrar una fila, mutiplicando su matriz por la matriz de identidad
		"""

		identidad = creador_identidad(self.r, self.c, self.by_row)
		m_identidad = identidad.del_row(j).elems
		
		nueva_matriz = myarray(m_identidad, self.r-1, self.c, self.by_row) @ matriz

		return nueva_matriz

	def del_col_identidad(self, k):
		"""Este metodo permite al ususario borrar una columna, mutiplicando su matriz por la matriz de identidad
		"""

		identidad = creador_identidad(self.r, self.c, self.by_row)
		m_identidad = identidad.del_row(k).elems
		m_matriz = matriz.transpose()

		matriz_temp = myarray(m_identidad, self.r-1, self.c, self.by_row) @ m_matriz
		nueva_matriz = myarray(matriz_temp, self.r-1, self.c, False).transpose()

		return nueva_matriz.elems


class creador_identidad(myarray):
	def __init__(self, r, c, by_row):
		self.r = r
		self.c = c
		self.by_row = by_row
		elems = []
		for i in range(self.r * self.c):
			elems.append(0)
		contador = 0	
		for j in range(self.r):
			elems[contador] = 1
			contador += (self.c+1)

		self.elems = elems



matriz = myarray([1,2,3,4,5,6,7,8,9], 3, 3, True)
matriz_2 = myarray([1,2,3,4,5,6,7,8,9], 3, 3, True)

# Get Position
print()
print('# Get Position') 
position = matriz.get_pos(0,1)
print (f"La posicion del elemento en la lista es: {position}\n")

# Get Coordenadas
print('# Get Coordinates')
coordenadas = matriz.get_coords(0)
print (f'Las coordenadas en la matriz de la posicion dada en la lista son: {coordenadas}\n')

# Get Row
print('# Get Row')
row = matriz.get_row(0)
print (f'Los elementos de la fila dada son: {row}\n')

# Get Column 
print('# Get Column')
col = matriz.get_col(0)
print (f'Los elementos de la columna dada son: {col}\n')

# Get Element
print('# Get Element')
element = matriz.get_elem((0,1))
print (f'El elemento es: {element}\n')

# Delete Row
print('# Delete Row')
del_row = matriz.del_row(0).elems
print (f'La nueva matriz es: {del_row}\n')

# Delete Column
print('# Delete Column') 
del_col = matriz.del_col(0).elems
print (f'La nueva matriz es: {del_col}\n')

# Swap Rows
print('# Swap Rows')
swap_rows = matriz.swap_rows(0,1)
print (f'La nueva matriz es: {swap_rows}\n')

# Swap Columns
print('# Swap Columns')
swap_cols = matriz.swap_cols(0,1)
print (f'La nueva matriz es: {swap_cols}\n')

# Scale Row
print('# Scale Row')
scale_row = matriz.scale_row(1,2)
print (f'La nueva matriz es: {scale_row}\n')

# Scale Column
print('# Scale Column')
scale_col = matriz.scale_col(1,2)
print (f'La nueva matriz es: {scale_col}\n')

# Transpose
print('# Transpose')
transpose = matriz.transpose().elems
print (f'La nueva matriz es: {transpose}\n')

# Flip Rows
print('# Flip Rows')
flip_rows = matriz.flip_row()
print (f'La nueva matriz es: {flip_rows}\n')

# Flip Columns
print('# Flip Columns')
flip_cols = matriz.flip_cols()
print (f'La nueva matriz es: {flip_cols}\n')

# __add__
print('# Suma')
x = (matriz + 4)
print(f'La nueva matriz es: {x}\n')

# __radd__
print('# Suma Derecha')
x = (4 + matriz)
print(f'La nueva matriz es: {x}\n')

# __sub__
print('# Resta')
x = (matriz - 4)
print(f'La nueva matriz es: {x}\n')

# __rsub__
print('# Resta Derecha')
x = (4 - matriz)
print(f'La nueva matriz es: {x}\n')

# __pow__
print('# Potencia')
x = (matriz ** 3)
print(f'La nueva matriz es: {x}\n')

# __rpow__
print('# Potencia Derecha')
x = (3 ** matriz)
print(f'La nueva matriz es: {x}\n')

# __matmul__
print('# Mautiplicacion Matrices')
x = (matriz @ matriz_2)
print(f'La nueva matriz es: {x}\n')

# __mul__
print('# Multiplicacion Escalar')
x = (matriz * 2)
print(f'La nueva matriz es: {x}\n')

# __rmul__
print('# Multiplicacion Derecha')
x = (2 * matriz)
print(f'La nueva matriz es: {x}\n')

# swap_row_identidad
print('# Intercambio Fila con Identidad')
fila = matriz.swap_rows_identidad(0,1)
print(f'La nueva matriz es: {fila}\n')

# swap_col_identidad
print('# Intercambio Columna con Identidad')
columna = matriz.swap_cols_identidad(0,1)
print(f'La nueva matriz es: {columna}\n')

# del_row_identidad
print('# Borrar Fila con Identidad')
borrar_fila = matriz.del_row_identidad(0)
print(f'La nueva matriz es: {borrar_fila}\n')

#del_col_identidad
print('# Borrar Columna con Identidad')
borrar_columna = matriz.del_col_identidad(0)
print(f'La nueva matriz es: {borrar_columna}\n')




