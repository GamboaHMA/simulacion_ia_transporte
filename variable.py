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
	def __init__(self, id:int, altura_m:float, peso_m:float, tipo_de_combustible:list[str], tipo_de_zona:str, rute_nodes:list[RuteNode]):
		self.id: int = id
		self.altura_m: float = altura_m
		self.peso_m: float = peso_m
		self.tipo_de_combustible: list[str] = tipo_de_combustible
		self.tipo_de_zona: str = tipo_de_zona
		self.rute_nodes: list[RuteNode] = rute_nodes

	def add_rute_node(self, rute_node: RuteNode):
		self.rute_nodes.append(rute_node)
	
	def __str__(self) -> str:
		return f"Rute ID: {self.id}, Altura: {self.altura_m}, PesoMaximo: {self.peso_m}, \n TiposDeComb: {self.tipo_de_combustible}, TipoDeZona: {self.tipo_de_zona}, Nodos: {[str(rute_node) for rute_node in self.rute_nodes]} \n"	

	def __repr__(self) -> str:
		return f"Rute: {self.id}"

#cada vehiculo tiene una capacidad y un conjunto de rutas a las que pueden ir
class Vehicle():  
	def __init__(self, id:int, altura:float, capacidad:float, tipo_de_combustible: list[str]):
		self.id: int = id
		self.altura: float = altura
		self.capacidad: float = capacidad
		self.tipo_de_combustible: list[str] = tipo_de_combustible
		self.horarios_ocupados:dict[OrderVar, tuple[float,float]] = {}
		self.distancia_max:float = -0.01 * self.capacidad + 550  
		self.distancia_restante:float = self.distancia_max 
		#propuesta tener un limite de viajes
	
	def __str__(self) -> str:
		return f"Vehicle ID: {self.id}, Altura: {self.altura}, Capacidad: {self.capacidad}, TipoDeCombustible: {self.tipo_de_combustible}, DistMax: {self.distancia_max}"

	#def __str__(self) -> str:
	#	return f"Vehicle: {self.id} Capacidad: {self.capacidad}"

	def __repr__(self) -> str:
		return f"Vehicle: {self.id} Cap: {self.capacidad}"

	def reset_dist_max(self):  # funcion que devuelve para 5000(minima cap) 500km y para 40000(max cap) 150km, valores entre ellos proporcinal
		self.distancia_restante = self.distancia_max

	def disponible(self, order: OrderVar) -> bool:  #por ahora chequea los horarios asignados del vehiculo en busca de tiempo libre, con la restriccion del tiempo limite del pedido
		if 2*order.rute_node.distance > self.distancia_restante:
			return False
		else:
			return True
	
	def assign_order(self, order:OrderVar):
		self.distancia_restante -= 2*order.rute_node.distance

	def estimate_distance(self, order: OrderVar):  #ida y vuelta 
		return 2*order.rute_node.distance
	
	def reset_order(self, order: OrderVar):
		self.distancia_restante += 2*order.rute_node.distance


class Register():
	def __init__(self, cant_vehiculos, ):
		self.cant_vehiculos = cant_vehiculos
		self.cant_ordenes

# sistema que llevara el control de los dominios de las variables, y el que asignara vehiculos a pedidos
class System():
	def __init__(self, vehicles: list[Vehicle], rutes: list[Rute], orders: list[OrderVar]):
		self.vehicles: list[Vehicle] = vehicles
		self.rutes:list[Rute] = rutes
		self.orders: list[OrderVar] = orders
		self.rutes_domain: dict[Rute, list[Vehicle]] = { rute:[] for rute in self.rutes }
		self.orders_domain: dict[OrderVar, list[Vehicle]] = { order:[] for order in self.orders }

		self.num_of_back = 0

		self.ass_rutes_domain()
		self.ass_orders_domain()


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
			
				if ( vehicle.altura <= rute.altura_m and vehicle.capacidad <= rute.peso_m and all(tipo_de_combustible in rute.tipo_de_combustible for tipo_de_combustible in vehicle.tipo_de_combustible) ):
					self.rutes_domain[rute].append(vehicle)
				
	def ass_orders_domain(self):
		for order in self.orders:
			rute_id = order.rute_node.rute_id
			rute_: Rute = None
			for rute in self.rutes:
				if rute_id == rute.id:
					rute_ = rute
					break
			for vehicle in self.rutes_domain[rute_]:
				if vehicle.capacidad >= order.cant:
					self.orders_domain[order].append(vehicle)

	def initial_solution(self):
		self.orders = self.ordered_orders_t(self.orders.copy())
		self.num_of_back = 0
		return self.backtrack(dict())

#	ordenando pedidos de menor a mayor, segun la cantidad de vehiculos que pueden tomar dicho pedido
#	si se selecciona los que tienen menos vehiculos disponibles, se evita que los pocos vehiculos disponibles no los tomen otros pedidos
	def ordered_orders_t(self, orders:list[OrderVar]) -> list[OrderVar]:
		vehicles_to_order_dict = { order:0 for order in orders}
		for order in orders:
			for vehicle in self.vehicles:
				if order.vehicle_ok(vehicle) and vehicle.disponible(order):
					vehicles_to_order_dict[order] += 1
		return sorted(orders, key=lambda v: vehicles_to_order_dict[v], reverse=False)
	
#	ordenando teniendo en cuenta la distancia restante por recorrer o cantidad de viajes restantes
#	de mayor a menor, ya que elegimos primero los vehiculos que tienen mas viajes disponibles [una opcion seria para optimizar la explotacion del vehiculo, ordenarlo a la inversa]
	def ordered_domain_values_dist_restante(self, var:OrderVar, assignment) -> list[Vehicle]:
		rute_node = var.rute_node
		rute_ = None
		for rute in self.rutes:
			if rute.id == rute_node.rute_id:
				rute_ = rute
				break
		result = [vehicle for vehicle in self.rutes_domain[rute_] if var.vehicle_ok(vehicle)]

		result = sorted(result, key=lambda v: v.distancia_restante, reverse=False)
		
		return result

#	igual que el anterior pero teniendo en cuenta la distancia maxima permitida
	def ordered_domain_values_dist_max(self, var:OrderVar, assignment) -> list[Vehicle]:
		rute_node = var.rute_node
		rute_ = None
		for rute in self.rutes:
			if rute.id == rute_node.rute_id:
				rute_ = rute
				break
		result = [vehicle for vehicle in self.rutes_domain[rute_] if var.vehicle_ok(vehicle)]

		result = sorted(result, key=lambda v: v.distancia_max, reverse=False)
		
		return result

#	teniendo en cuenta la cantidad de pedidos que pueden satisfacer los vehiculos, si se escoge
#	un vehiculo que puede satisfacer menos pedidos, entonces el vehiculo no corre riesgo de quedarse sin asignar
	def ordered_domain_values_dom_a_satisfacer(self, var:OrderVar, assignment) -> list[Vehicle]:
		rute_node = var.rute_node
		rute_ = None
		for rute in self.rutes:
			if rute.id == rute_node.rute_id:
				rute_ = rute
				break
		result = [vehicle for vehicle in self.rutes_domain[rute_] if var.vehicle_ok(vehicle)]
		orders_to_vehicle_dict = { vehicle: 0 for vehicle in result }
		for vehicle in result:
			for order in self.orders:
				if order.vehicle_ok(vehicle) and vehicle.disponible(order):
					orders_to_vehicle_dict[vehicle] += 1
		result = sorted(result, key=lambda v: orders_to_vehicle_dict[v], reverse=False) #
		

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
		domain_values = self.ordered_domain_values_dist_max(var, assignment)
		for vehicle in domain_values:
			if(domain_values[0] != vehicle):
				self.num_of_back += 1
			print(f"{vehicle}")
			if vehicle.disponible(var):
				vehicle.assign_order(var)
				print(f"vehiculo {vehicle} disponible, dist_restante: {vehicle.distancia_max}")
				assignment[var] = vehicle
				result = self.backtrack(assignment)
				
				if result is not None:
					return result
				else:
					self.num_of_back += 1
					vehicle.reset_order(var)
					print(f"{vehicle} resetear orden {var}")
					assignment.pop(var, None)
		return None


