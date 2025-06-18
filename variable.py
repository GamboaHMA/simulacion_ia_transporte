#variable pedido, a cada variable se le asignara un camion designado a hacer la entrega, el camion debe cumplir requisitos
		
class RuteNode():
	def __init__(self, node_id: int, rute_id: int, distance: float):
		self.node_id: int = node_id
		self.rute_id: int = rute_id
		self.distance: float = distance
	
	def __str__(self) -> str:
		return f"Node ID: {self.node_id}, Rute ID: {self.rute_id}, Distance: {self.distance}"


class OrderVar():
	def __init__(self, id: int, rute_node:RuteNode, cant: float, t_lim: float):
		self.id: int = id
		self.rute_node: RuteNode = rute_node
		self.cant: float = cant
		self.t_lim: float = t_lim
	
	def __str__(self) -> str:
		return f"Order ID: {self.id}, RuteNode: {self.rute_node}, Cantidad: {self.cant}, TiempoLimite: {self.t_lim}"

	def __repr__(self) -> str:
		return f"Order: {self.id} Cant: {self.cant} Time: {self.t_lim}"
	
	def vehicle_ok(self, vehicle: "Vehicle"):
		return True if self.cant <= vehicle.capacidad else False 


#una ruta contiene varios puntos de posibles pedidos que se generaran, cada punto contiene la distancia, y cada ruta tiene especificaciones
#que deben cumplir los vehiculos que transitan por el mismo
class Rute():
	def __init__(self, id:int, ancho_m:float, altura_m:float, peso_m:float, tipo_de_combustible:list[str], tipo_de_zona:str, rute_nodes:list[RuteNode]):
		self.id: int = id
		self.ancho_m: float = ancho_m
		self.altura_m: float = altura_m
		self.peso_m: float = peso_m
		self.tipo_de_combustible: list[str] = tipo_de_combustible
		self.tipo_de_zona: str = tipo_de_zona
		self.rute_nodes: list[RuteNode] = rute_nodes

	def add_rute_node(self, rute_node: RuteNode):
		self.rute_nodes.append(rute_node)
	
	def __str__(self) -> str:
		return f"Rute ID: {self.id}, Ancho: {self.ancho_m}, Altura: {self.altura_m}, PesoMaximo: {self.peso_m}, \n TiposDeComb: {self.tipo_de_combustible}, TipoDeZona: {self.tipo_de_zona}, Nodos: {[str(rute_node) for rute_node in self.rute_nodes]} \n"	

	def __repr__(self) -> str:
		return f"Rute: {self.id}"

#cada vehiculo tiene una capacidad y un conjunto de rutas a las que pueden ir
class Vehicle():  
	def __init__(self, id:int, ancho:float, altura:float, capacidad:float, tipo_de_combustible: list[str]):
		self.id: int = id
		self.ancho: float = ancho
		self.altura: float = altura
		self.capacidad: float = capacidad
		self.tipo_de_combustible: list[str] = tipo_de_combustible
		self.horarios_ocupados:dict[OrderVar, tuple[float,float]] = {}
		#propuesta tener un limite de viajes
	
	def __str__(self) -> str:
		return f"Vehicle ID: {self.id}, Ancho: {self.ancho}, Altura: {self.altura}, Capacidad: {self.capacidad}, TipoDeCombustible: {self.tipo_de_combustible}"

	#def __str__(self) -> str:
	#	return f"Vehicle: {self.id} Capacidad: {self.capacidad}"

	def __repr__(self) -> str:
		return f"Vehicle: {self.id} Cap: {self.capacidad}"

	def disponible(self, order: OrderVar) -> bool:  #por ahora chequea los horarios asignados del vehiculo en busca de tiempo libre, con la restriccion del tiempo limite del pedido
		tiempo_estimado = self.estimate_time(order)
		last = 0
		for horario_ocupado in self.horarios_ocupados.values():
			if last + tiempo_estimado > order.t_lim:
				print(f"{self} no disponible, tiempo estimado: {last}, {last + tiempo_estimado}")
				return False
			if last + tiempo_estimado < horario_ocupado[0]:
				self.horarios_ocupados[order] = (last, last+tiempo_estimado)
				return True
			else:
				last = horario_ocupado[1]
		if last + tiempo_estimado > order.t_lim:
			print(f"{self} no disponible, tiempo estimado {last}, {last + tiempo_estimado}, tiempo limite de la orden: {order.t_lim}")
			return False
		else:
			self.horarios_ocupados[order] = (last, last+tiempo_estimado)
			return True
	
	def estimate_time(self, order: OrderVar):  #ida y vuelta 
		return 2*order.rute_node.distance/60
	
	def reset_order(self, order: OrderVar):
		if order in self.horarios_ocupados:
			self.horarios_ocupados.pop(order, None)
		else:
			return None


# sistema que llevara el control de los dominios de las variables, y el que asignara vehiculos a pedidos
class System():
	def __init__(self, vehicles: list[Vehicle], rutes: list[Rute], orders: list[OrderVar]):
		self.vehicles: list[Vehicle] = vehicles
		self.rutes:list[Rute] = rutes
		self.orders: list[OrderVar] = orders
		self.rutes_domain: dict[Rute, list[Vehicle]] = { rute:[] for rute in self.rutes }

		self.ass_rutes_domain()


	def __str__(self):
		result = ""
		result += f"Cantidad de Vehiculos: { len(self.vehicles) } .\n"
		for vehicle in self.vehicles:
			result += f"  {vehicle} \n"
		result += "\n"

		result += f"Cantidad de Rutas: { len(self.rutes) } .\n"
		for rute in self.rutes:
			result += f"   {rute} \n"
		result += "\n"

		result += f"Cantidad de pedidos: { len(self.orders) } .\n"
		for order in self.orders:
			result += f"   {order} \n"
		result += "\n"

		return result
	
	def ass_rutes_domain(self):    
		for rute in self.rutes:
			for vehicle in self.vehicles:
			
				if (vehicle.ancho < rute.ancho_m and vehicle.altura < rute.altura_m and vehicle.capacidad < rute.peso_m and all(tipo_de_combustible in rute.tipo_de_combustible for tipo_de_combustible in vehicle.tipo_de_combustible) ):
					self.rutes_domain[rute].append(vehicle)
				

	def initial_solution(self):
		self.orders = self.ordered_orders_t(self.orders.copy())
		return self.backtrack(dict())


	def ordered_orders_t(self, orders) -> list[OrderVar]:
		return orders
	
	def ordered_domain_values(self, var:OrderVar, assignment) -> list[Vehicle]:
		rute_node = var.rute_node
		rute_ = None
		for rute in self.rutes:
			if rute.id == rute_node.rute_id:
				rute_ = rute
				break
		result = [vehicle for vehicle in self.rutes_domain[rute_] if var.vehicle_ok(vehicle)]
		return result

	def unasigned_var(self, assignment) -> OrderVar:
		for var in self.orders:
			if var not in assignment:
				return var
	
	def backtrack(self, assignment: dict[OrderVar, Vehicle]):
		if len(assignment) == len(self.orders):
			return assignment
		var:OrderVar = self.unasigned_var(assignment)
		print(f"{var}")
		for vehicle in self.ordered_domain_values(var, assignment):
			print(f"{vehicle}")
			if vehicle.disponible(var):
				print(f"vehiculo {vehicle} disponible, lapso: {vehicle.horarios_ocupados[var]}")
				assignment[var] = vehicle
				result = self.backtrack(assignment)
				
				if result is not None:
					return result
				else:
					vehicle.reset_order(var)
					print(f"{vehicle} resetear orden {var}")
					assignment.pop(var, None)
		return None


