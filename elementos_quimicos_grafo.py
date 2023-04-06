import networkx as nx
import matplotlib.pyplot as plt

G = nx.cycle_graph(0)
pos = nx.circular_layout(G)

def edges(dic_nodes, abc, l_edges):
	"""
	Toma como argumentos:
	dic_nodes: es un diccionario donde su key son las letras del abcedario y 
	los values que toma son todas la palabras que comenzan con esa letra
	abc: es un lista que contiene todas las letras del abecedario
	l_edges: es una lista vacia donde van a esrar todas las ramas del grafo

	RETRUN: la fincion devuelve una lista (l_edges) que contiene todas las
	combincioonex posibles entre dos palabras. Va a ser una lista con listas adentro.
	Estas sub listas va a ser coordenadas ==> ['Actinium', 'Magnesium']
	"""
	for i in abc:
		palabras = dic_nodes.get(i)

		for j in palabras:
			
			ultima_letra = j[-1]

			posibles_palabras_siguentes = dic_nodes.get(ultima_letra)

			for h in posibles_palabras_siguentes:
				l_edges.append([j, h])
	return l_edges


l_edges = []

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dic_nodes = {
	'a': ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine'], 
	'b': ['Barium', 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine'], 
	'c': ['Cadmium', 'Calcium', 'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copernicium', 'Copper', 'Curium'], 
	'd': ['Darmstadtium', 'Dubnium', 'Dysprosium'], 
	'e': ['Einsteinium', 'Erbium', 'Europium'], 
	'f': ['Fermium', 'Flerovium', 'Fluorine', 'Francium'], 
	'g': ['Gadolinium', 'Gallium', 'Germanium', 'Gold'], 
	'h': ['Hafnium', 'Hassium', 'Helium', 'Holmium', 'Hydrogen'], 
	'i': ['Indium', 'Iodine', 'Iridium', 'Iron'], 
	'j': [],
	'k': ['Krypton'],
	'l': ['Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 'Livermorium', 'Lutetium'], 
	'm': ['Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury', 'Molybdenum', 'Moscovium'], 
	'n': ['Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium', 'Nitrogen', 'Nobelium'], 
	'o': ['Oganesson', 'Osmium', 'Oxygen'], 
	'p': ['Palladium', 'Phosphorus', 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 'Praseodymium', 'Promethium', 'Protactinium'], 
	'q': [],
	'r': ['Radium', 'Radon', 'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 'Ruthenium', 'Rutherfordium'], 
	's': ['Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Sulfur'], 
	't': ['Tantalum', 'Technetium', 'Tellurium', 'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten'], 
	'u': ['Uranium'], 
	'v': ['Vanadium'], 
	'w': [],
	'x': ['Xenon'], 
	'y': ['Ytterbium', 'Yttrium'], 
	'z': ['Zinc', 'Zirconium']
	}

edges(dic_nodes, abc, l_edges)

nodes = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 
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
l_edges_sin_duplicados = []

for i in l_edges:
	if i not in l_edges_sin_duplicados:
		l_edges_sin_duplicados.append(i)

G.add_nodes_from(nodes)
G.add_edges_from(l_edges_sin_duplicados)

plt.figure(1, figsize = (10,8))
nx.draw_circular(G, with_labels = True, node_size = 300, font_size = 5)

plt.show()

