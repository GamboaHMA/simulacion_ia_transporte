class Node:
	def __init__(self, id, map:"Map") -> None:
		self.id:int = id
		self.map:Map = map
		self.adyacents:list[Node] = []
		self.adyacents_distances:dict[Node, float] = { }
	
	def __str__(self) -> str:
		adyacents_str = ""
		for adyacent in self.adyacents:
			adyacents_str += str(adyacent.id)  # Solo usar el ID para evitar recursión
			adyacents_str += " "
		return f"ID: {self.id} Adyacents: {adyacents_str}"

	def __repr__(self) -> str:
		return str(self.id)

	def __eq__(self, other):
		if not isinstance(other, Node):
			return False
		return self.id == other.id and self.map.id == other.map.id

	def __hash__(self):
		return hash((self.id, self.map.id))

	def add_adyacent(self, distance, node:"Node"):
		if node.map.id != self.map.id:
			raise Exception(f"El nodo {self} tiene mapa {self.map.id} y el nodo {node} tiene como mapa {node.map.id}")
		if node in self.adyacents:
			raise Exception(f"Ya el nodo {node} esta contenido en los adyacentes de {self}")
		self.adyacents.append(node)
		if node in self.adyacents_distances.keys():
			raise Exception(f"Ya el nodo {node} esta contenido en el diccionario de distancias de los adyacentes de {self}")
		self.adyacents_distances[node] = distance

class Map:
	def __init__(self, id, nodes:list["Node"], edges:dict[tuple[int,int], float]) -> None:
		self.id = id
		self.nodes:list[Node] = nodes
		self.edges:dict[tuple[int,int], float] = edges
	
	def __str__(self) -> str:
		return f"ID: {self.id} Cantidad de Nodos: {len(self.nodes)} Cantidad de Aristas: {len(self.edges)}"
	
	def __repr__(self) -> str:
		return self.id