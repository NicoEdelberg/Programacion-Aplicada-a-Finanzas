class myarray_2():
	"""La clase myarray_2 toma una lista de numeros, la cantidad de filas, la canttidad de columnas
	y la forma en la que va a ser ordenada (by_row). En el caso en que esta ultima variable sea True 
	== > primero completara las filas y luego las columnas
	"""
	def __init__ (self, row, col, by_row, lista):
		self.lista = lista
		self.row = row
		self.col = col
		self.by_row = by_row

	def lista_fila_def(self, row, col, by_row, lista):
		"""Este metodo toma las matriz dada por el usuario y la conviere en una lista de listas 
		donde la primera lista seria la primera fila arrancando por el 0
		"""
		lista_fila = []
		m_lista_1 = self.lista.copy()
		
		if self.by_row == True:

			for i in range(0, (self.row)):
				parto_m_lista_1 = m_lista_1[:self.row]
				lista_fila.append(parto_m_lista_1)

				for j in range(0, len(parto_m_lista_1)):
					m_lista_1.pop(0)

		elif self.by_row == False:

			contador_local = 0
			for i in range(1, (self.row)):
				parto_m_lista_1 = m_lista_1[contador_local::row]
				lista_fila.append(parto_m_lista_1)
				contador_local+=1

		return lista_fila

	def lista_col_def(self, row, col, by_row, lista):
		"""Este metodo toma las matriz dada por el usuario y la conviere en una lista de listas 
		donde la primera lista seria la primera columna arrancando por el 0
		"""
		lista_col = []
		m_lista_2 = self.lista.copy()

		for j in range(0, len(lista_fila[0])):
			columna = []
			for i in range(0, len(lista_fila)):
				columna.append(lista_fila[i][j])
			lista_col.append(columna)
		return lista_col

	def get_pos(self, j, k):
		"""
		Devuelve el valor m en lista (la matriz del ususario)
		j = filas
		k = columnas

		"""
		if j <= row-1 and j >= 0 and k <= col-1 and k >= 0:
			index = j*col + k
			salida = (f'La posicion {j,k} en la matriz es el lugar {index} en la lista de la matriz')

		else:
			salida = (f'La posicion {j,k} no se encuentra en la matriz')

		return salida

	def get_coords(self, m):
		"""
		Devuelve las coordenadas en la matriz del elemento dado
		m = un elemento de la matriz
		"""

		if m in range(0, len(lista)-1):
			cociente = m // col
			resto = m % col

			salida = (f'Las coordenadas del elemento {m} son {(cociente, resto)}')
		
		else:
			salida = (f'El elemento {m} no es un indice de la matriz')

		return salida

	def switch(self):
		"""Primero cambia el orden del la lista que provee por el usuario
		Luego invierte el valor booleano de by_row (o sea, lo invierte)
		y retorna la nueva matriz en forma de lista de listas
		"""
		switch_lista = []

		for i in lista:
			switch_lista.insert(0,i)

		if by_row == True:
			matriz_switch = self.lista_fila_def(row, col, False, switch_lista)

		elif by_row == False:
			matriz_switch = self.lista_fila_def(row, col, True, switch_lista)

		return (f'Despues del switch la nueva matriz es: {matriz_switch}')

	def get_row(self, j):
		"""Devuelve todos los valores de que estan la la fila j en forma de lista
		"""
		
		if j >= row and j < 0:
			salida = (f'La fila {j} no esta dentro de la matriz')
		else:
			salida = (f'La fila {j} contiene los valores {lista_fila[j]}')

		return salida

	def get_col(self, k):
		"""Devuelve todos los valores de que estan la la columns k en forma de lista
		"""

		if k >= col and k < 0:
			salida = (f'La columna {k} no esta dentro de la matriz')
		else:
			salida = (f'La columna {k} contiene los valores {lista_col[k]}')

		return salida

	def elem(self, j, k):
		"""Devuelve el elemento que esta en las coordenadas (j,k) 
		j = filas
		k = columnas  
		"""
		
		if j < row-1 and j >= 0 and k < col-1 and k >= 0:
			index = j*col + k
			salida = (f'Las coordenadas {j,k} corresponden al elemento {lista[index]}')
		
		else: 
			salida = (f'Las coordenadas {j,k} no se encuentran en la matiz')
		
		return salida

	def del_row(self,j):
		"""El metodo borra la fila j que le pasa el usuario
		"""

		if j <= row-1 and j >= 0:

			nueva_lista_fila = lista_fila.copy()
			del nueva_lista_fila[j]

			salida = (f'Se elimino la fila {j}: {lista_fila[j]} de la matriz\nLa nueva matriz: {nueva_lista_fila}')

		else:
			salida = (f'La fila {j} no se encuentra en la matriz')

		return salida

	def del_col (self, k):
		"""El metodo borra la columna k que le pasa el usuario
		"""

		if k <= col-1 and k >= 0:

			nueva_lista_col = lista_col.copy()
			del nueva_lista_col[k]

			salida = (f'Se elimino la columna {k}: {lista_col[k]} de la matriz\nLa nueva matriz: {nueva_lista_col}')

		else:
			salida = (f'La columna {k} no se encuentra en la matriz')

		return salida

	def swap_rows(self, j, k):
		"""El metodo intercambia dos filas en la matriz
		"""

		if j <= row-1  and j >= 0 and k <= row-1 and k >= 0:
			nueva_lista_fila = lista_fila.copy()

			values_j = nueva_lista_fila[j]
			values_k = nueva_lista_fila[k]

			nueva_lista_fila.pop(j)
			nueva_lista_fila.insert(j, values_k)

			nueva_lista_fila.pop(k)
			nueva_lista_fila.insert(k, values_j)

			salida = (f'Se intercambieron las filas {j,k}\nLa nueva matriz: {nueva_lista_fila}')

		else:
			salida = (f'Las filas {j,k} no se encuntran en la matriz')

		return salida

	def swap_cols (self, l, m):
		"""El metodo intercambia dos columnas en la matriz
		"""

		if l <= row-1  and l >= 0 and m <= row-1 and m >= 0:
			nueva_lista_col = lista_col.copy()

			values_l = nueva_lista_col[l]
			values_m = nueva_lista_col[m]

			nueva_lista_col.pop(l)
			nueva_lista_col.insert(l, values_m)

			nueva_lista_col.pop(m)
			nueva_lista_col.insert(m, values_l)

			salida = (f'Se intercambieron las columnas {l,m}\nLa nueva matriz: {nueva_lista_col}')

		else:
			salida = (f'Las columnas {l,m} no se encuntran en la matriz')

		return salida

	def scale_row(self, j, x):
		"""El metodo multiplica a los elementos de una fila j por un escalar x
		"""

		if j <= row-1 and j >= 0 and (isinstance(x, float) or isinstance(x, int)):
			nueva_lista_fila = lista_fila.copy()

			values_j = nueva_lista_fila[j]
			values_j_x = []

			for i in values_j:
				multiplicado = i * x
				values_j_x.append(multiplicado)

			nueva_lista_fila.pop(0)
			nueva_lista_fila.insert(0,values_j_x)

			salida = (f'Se multimplico la fila por {j} por el escalar {x}\nNueva matriz: {nueva_lista_fila}')

		elif isinstance(x, str):	
			slida = (f'El escalar {x} es un string tiene que ser float o integer')

		else:
			salida = (f'{j} no es una fila de la matriz')

		return salida

	def scale_col(sel, k, y):
		"""El metodo multiplica a los elementos de una columna k por un escalar y
		"""

		if k <= col-1 and k >= 0 and (isinstance(y, float) or isinstance(y, int)):
			nueva_lista_col = lista_col.copy()

			values_k = nueva_lista_col[k]
			values_k_y = []

			for i in values_k:
				multiplicado = i * y
				values_k_y.append(multiplicado)

			nueva_lista_col.pop(0)
			nueva_lista_col.insert(0,values_k_y)

			salida = (f'Se multimplico la columna por {k} por el escalar {y}\nNueva matriz: {nueva_lista_col}')

		elif isinstance(y, str):	
			slida = (f'El escalar {y} es un string tiene que ser float o integer')

		else:
			salida = (f'{k} no es una columna de la matriz')

		return salida

	def transpose(self):
		"""El metodo intercambia las filas de una matriz por sus columnas
		"""

		matriz_transpuesta = list(self.lista_col_def(col, row, by_row, lista))
		return (f'La matriz transpuesta de {lista_fila} \nes: {matriz_transpuesta}')

	def flip_rows(self):
		"""El metodo de intercambia las filas de la matriz de forma especular
		o sea, desde la fila del medio hacia afuera
		"""
		nueva_lista_fila = lista_fila.copy()

		for i in range(0, len(nueva_lista_fila) // 2):
			aux = nueva_lista_fila[i]

			nueva_lista_fila[i] = nueva_lista_fila[len(nueva_lista_fila)-(1+i)]

			nueva_lista_fila[len(nueva_lista_fila)-(1+i)] = aux
	
		salida = (f'Se cambiaron las filas especularmente \nLa nueva matriz: {nueva_lista_fila}')

		return salida

	def flip_cols(self):
		"""El metodo de intercambia las columnas de la matriz de forma especular
		o sea, desde la columna del medio hacia afuera
		"""

		nueva_lista_col = lista_col.copy()

		for i in range(0, len(nueva_lista_col) // 2):
			aux = nueva_lista_col[i]

			nueva_lista_col[i] = nueva_lista_col[len(nueva_lista_col)-(1+i)]

			nueva_lista_col[len(nueva_lista_col)-(1+i)] = aux
	
		salida = (f'Se cambiaron las columnas especularmente \nLa nueva matriz: {nueva_lista_col}')

		return salida
		
	def det(self):
		"""El metodo calcula el determinante de la matriz de forma recursiva hasta 
		tener una matriz de 1x1 donde el determinante es el mismo numero
		"""
		
		determinante = 0
		if len(lista_fila) == 2:
			determinante = (lista_fila[0][0] * lista_fila[1][1]) - (lista_fila[0][1] * lista_fila[1][0])
		else:
			for j in range(0, len(lista_fila[0])):
				determinante += lista_fila[0][j] * ((-1) ** j) * self.det(self.del_row(0), self.del_col(j))


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

			print(nueva_matriz)

			lista_fila_B = self.lista_fila_def(row, col, by_row, nueva_matriz)


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

			lista_tepm = [2,4,6,8,10,12,14,16,18,20,22,24]

			lista_fila_B = self.lista_fila_def_def(row, col, by_row, lista_tepm)

			print(nueva_matriz)
			print(lista_fila_B)

			salida = (f'La nueva matriz: {lista_fila_B}')

		else:
			salida = (f'B: no es una lista de numeros')

		return salida

	def rprod(self, B):
		if col == row_B and isinstance(B, list):
			lista_col_B = self.lista_col_def(row_B, col_B, by_row, B)

		else:
			lista_col_B = 5

		return lista_col_B






lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

row = 3

col = 3

by_row = True


B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

row_B = 3

col_B = 4

by_row_B = True



z = myarray_2(row, col, by_row, lista)

b = myarray_2(row_B, col_B, by_row_B, B)

lista_fila = z.lista_fila_def(row, col, by_row, lista)
lista_col = z.lista_col_def(row, col, by_row, lista)

print(b.lista_col_def(row_B, col_B, by_row_B, B))




