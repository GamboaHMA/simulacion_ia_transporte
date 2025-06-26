from data import rutas, orders, vehicles, new_vehicles, new_orders
from variable import System
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
    
    #vehiculos_ = ml.obtain_vehicles()
    #system = System(rutes=rutas, orders=orders, vehicles=vehiculos_)
    system = System(rutes=rutas, orders=new_orders, vehicles=new_vehicles)
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

if __name__ == "__main__":
    main()