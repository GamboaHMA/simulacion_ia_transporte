from variable import System, Vehicle, OrderVar, Rute, RuteNode
import random

#generar soluciones iniciales a partir de un conjunto de vehiculos y ordenes
class MetaheuristicAgent:
    def __init__(self, id=1) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Metaheuristica para encontrar soluciones a problemas de asignacion muy grandes. ID:{self.id}"
    
    def __repr__(self) -> str:
        return f"Metaheuristica {self.id}"
    
    def initial_solution(self, system:System):
        result:dict[OrderVar, Vehicle] = {}
        system.orders = system.ordered_orders_t(system.orders.copy())
        for order in system.orders:
            # conjunto para elegir aleatorio, con la condicion de que el que se seleccione este disponible
            domain = set()
            for vehicle in system.orders_domain[order]:
                domain.add(vehicle)
            while(len(domain) != 0):
                vehicle:Vehicle = random.choice(tuple(domain))
                if vehicle.disponible(order=order):
                    result[order] = vehicle
                    vehicle.assign_order(order=order)
                    break
                else:
                    domain.remove(vehicle)
            if order not in result.keys():
                result[order] = None

            print("asd")
        
        return result #asd