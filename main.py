from data import rutas, vehicles, new_vehicles, new_orders, vehicles_json
from variable import System, Vehicle
import json
import modelo_de_lenguaje as ml
'''
def main():
    id_to_remove = [1, 2, 4, 5, 6, 7, 8, 9]
    count = 0
    while(count < len(rutas)):
        if rutas[count].id in id_to_remove:
            rutas.pop(count)
            continue
        count+=1

    count = 0
    while(count < len(orders)):
        if orders[count].rute_node.rute_id in id_to_remove:
            orders.pop(count)
            continue
        count += 1 

    system_ = System(rutes=rutas, orders=orders, vehicles=vehicles)
    domain = system_.rutes_domain

    for rute, rute_domain in domain.items():
        for vehicle in rute_domain:
            print(f"  Vehicle: {vehicle}")
        print("\n")

    for order in orders:
        print(order)
        rute_id = order.rute_node.rute_id
        for rute in rutas:
            if rute.id == rute_id:
                print(f"{rute}")
                break

    print("\n")

    initial_solution = system_.initial_solution()
    if initial_solution:
        for key, value in initial_solution.items():
            print(f"Order {key.id} assigned to Vehicle {value.id}")
    else:
        print("solucion vacia")
'''

def main():
    for rute in rutas:
        print(rute)
    for order in new_orders:
        print(order)
    vehiculos = []
    vehicles_data = json.loads(vehicles_json)
    for vehicle_data in vehicles_data:
        vehicle_ = Vehicle(
            id=vehicle_data["id"],
            altura=vehicle_data["altura"],
            capacidad=vehicle_data["capacidad"],
            tipo_de_combustible=vehicle_data["tipo_de_combustible"]
        )
        vehiculos.append(vehicle_)
    for vehiculo in vehiculos:
        print(vehiculo)
    system = System(rutes=rutas, orders=new_orders, vehicles=vehiculos)
    initial_solution = system.initial_solution()
    if initial_solution:
        for key, value in initial_solution.items():
            print(f"Order {key.id} assigned to Vehicle {value.id}")
        vehicles = set()
        for vehicle in initial_solution.values():
            vehicles.add(vehicle)
        for vehicle in vehicles:
            print(vehicle)
        print(f"Cantidad de vehiculos usados: {len(vehicles)}")
        print(f"cantidad de back dados: {system.num_of_back}")
    print("asd")
    '''
    #vehiculos_ = ml.obtain_vehicles(20)
    vehiculos = ml.obtain_vehicles_grad()
    for vehiculo in vehiculos:
        vehiculo.reset_dist_max()
    system = System(rutes=rutas, orders=new_orders, vehicles=vehiculos)
    #system = System(rutes=rutas, orders=new_orders, vehicles=new_vehicles)
    for order in system.orders:
        print(order)
    initial_solution = system.initial_solution()
    if initial_solution:
        for key, value in initial_solution.items():
            print(f"Order {key.id} assigned to Vehicle {value.id}")
        vehicles = set()
        for vehicle in initial_solution.values():
            vehicles.add(vehicle.id)
        print(f"Cantidad de vehiculos usados: {len(vehicles)}")
        print(f"cantidad de back dados: {system.num_of_back}")
    else: print("solucion vacia")

    print("finalizado")    
    '''
if __name__ == "__main__":
    main()