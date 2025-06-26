import json
import random
from variable import Rute,RuteNode,Vehicle,OrderVar



rutas = [
    Rute(
        id=1,
        altura_m=3.80,
        peso_m=15000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=102, rute_id=1, distance=45),
            RuteNode(node_id=103, rute_id=1, distance=60),
            RuteNode(node_id=101, rute_id=1, distance=70),
        ]
    ),
    Rute(
        id=2,
        altura_m=3.80,
        peso_m=10000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="rural",
        rute_nodes=[
            RuteNode(node_id=202, rute_id=2, distance=55),
            RuteNode(node_id=203, rute_id=2, distance=70),
            RuteNode(node_id=201, rute_id=2, distance=60),
        ]
    ),
    Rute(
        id=3,
        altura_m=3.80,
        peso_m=30000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=302, rute_id=3, distance=40),
            RuteNode(node_id=303, rute_id=3, distance=50),
            RuteNode(node_id=301, rute_id=3, distance=70),
        ]
    ),
    Rute(
        id=4,
        altura_m=3.40,
        peso_m=8000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="urbana",
        rute_nodes=[
            RuteNode(node_id=402, rute_id=4, distance=90),
            RuteNode(node_id=403, rute_id=4, distance=120),
            RuteNode(node_id=401, rute_id=4, distance=80),
        ]
    ),  
    Rute(
        id=5,
        altura_m=4.00,
        peso_m=45000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=502, rute_id=5, distance=50),
            RuteNode(node_id=503, rute_id=5, distance=65),
            RuteNode(node_id=501, rute_id=5, distance=75),
        ]
    ),
    Rute(
        id=6,
        altura_m=3.70,
        peso_m=6000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="urbana",
        rute_nodes=[
            RuteNode(node_id=602, rute_id=6, distance=100),
            RuteNode(node_id=603, rute_id=6, distance=120),
            RuteNode(node_id=601, rute_id=6, distance=140),
        ]
    ),
    Rute(
        id=7,
        altura_m=3.85,
        peso_m=25000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="mixta",
        rute_nodes=[
            RuteNode(node_id=702, rute_id=7, distance=60),
            RuteNode(node_id=703, rute_id=7, distance=70),
            RuteNode(node_id=701, rute_id=7, distance=80),
        ]
    ),
    Rute(
        id=8,
        altura_m=3.65,
        peso_m=18000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="rural",
        rute_nodes=[
            RuteNode(node_id=802, rute_id=8, distance=80),
            RuteNode(node_id=803, rute_id=8, distance=90),
            RuteNode(node_id=801, rute_id=8, distance=50),
        ]
    ),
    Rute(
        id=9,
        altura_m=3.90,
        peso_m=35000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=902, rute_id=9, distance=40),
            RuteNode(node_id=903, rute_id=9, distance=75),
            RuteNode(node_id=901, rute_id=9, distance=65),
        ]
    ),
    Rute(
        id=10,
        altura_m=3.55,
        peso_m=11000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="mixta",
        rute_nodes=[
            RuteNode(node_id=1002, rute_id=10, distance=80),
            RuteNode(node_id=1003, rute_id=10, distance=40),
            RuteNode(node_id=1001, rute_id=10, distance=100),
        ]
    )
]

vehicles = [
    Vehicle(id=1, altura=3.30, capacidad=8000, tipo_de_combustible= ["diesel", "gasolina"]),   # Estrecho, estándar, baja
    Vehicle(id=2, altura=3.60, capacidad=20000, tipo_de_combustible=["diesel", "gasolina"]),  # Estándar, alto, media
    Vehicle(id=3, altura=4.00, capacidad=50000, tipo_de_combustible=["diesel", "gasolina"]), # Muy ancho, muy alto, muy alta
    Vehicle(id=4, altura=3.40, capacidad=10000, tipo_de_combustible=["diesel", "gasolina"]), # Estrecho, estándar, baja
    Vehicle(id=5, altura=3.70, capacidad=30000, tipo_de_combustible=["diesel", "gasolina"]), # Estándar, alto, alta
    Vehicle(id=6, altura=3.25, capacidad=35000, tipo_de_combustible=["diesel", "gasolina"]), # Muy ancho, estándar, alta
    Vehicle(id=7, altura=4.10, capacidad=55000, tipo_de_combustible=["diesel", "gasolina"]), # Estándar, muy alto, muy alta
    Vehicle(id=8, altura=3.45, capacidad=18000, tipo_de_combustible=["diesel", "gasolina"])  # Muy ancho, estándar, media
]

rangos_cantidad = [5000, 6000, 7000, 8000, 9000,
                   10000, 11000, 12000, 13000, 14000,
                   15000, 16000, 17000, 18000, 19000,
                   20000, 21000, 22000, 23000, 24000,
                   25000, 26000, 27000, 28000, 29000,
                   30000, 31000, 32000, 33000, 34000,
                   35000, 36000, 37000, 38000, 39000,
                   40000]

# Función para obtener una cantidad aleatoria según la categoría
def get_cantidad_aleatoria(rute_node:RuteNode):

    rute = rutas[rute_node.rute_id-1]
    peso_max = rute.peso_m
    rangos_validos = [rango for rango in rangos_cantidad if rango <= peso_max]
    cant_r_index = random.randint(0, len(rangos_validos)-1)
    return rangos_validos[cant_r_index]


orders = [
    OrderVar(id=1, rute_node=rutas[0].rute_nodes[1], cant=get_cantidad_aleatoria(rutas[0].rute_nodes[1]), t_lim=random.randint(5, 24)),
    OrderVar(id=2, rute_node=rutas[1].rute_nodes[0], cant=get_cantidad_aleatoria(rutas[1].rute_nodes[0]), t_lim=random.randint(5, 24)),
    OrderVar(id=3, rute_node=rutas[2].rute_nodes[2], cant=get_cantidad_aleatoria(rutas[2].rute_nodes[2]), t_lim=random.randint(5, 24)),
    OrderVar(id=4, rute_node=rutas[3].rute_nodes[1], cant=get_cantidad_aleatoria(rutas[3].rute_nodes[1]), t_lim=random.randint(5, 24)),
    OrderVar(id=5, rute_node=rutas[4].rute_nodes[0], cant=get_cantidad_aleatoria(rutas[4].rute_nodes[0]), t_lim=random.randint(5, 24)),
    OrderVar(id=6, rute_node=rutas[5].rute_nodes[2], cant=get_cantidad_aleatoria(rutas[5].rute_nodes[2]), t_lim=random.randint(5, 24)),
    OrderVar(id=7, rute_node=rutas[6].rute_nodes[1], cant=get_cantidad_aleatoria(rutas[6].rute_nodes[1]), t_lim=random.randint(5, 24)),
    OrderVar(id=8, rute_node=rutas[7].rute_nodes[0], cant=get_cantidad_aleatoria(rutas[7].rute_nodes[0]), t_lim=random.randint(5, 24)),
    OrderVar(id=9, rute_node=rutas[8].rute_nodes[2], cant=get_cantidad_aleatoria(rutas[8].rute_nodes[2]), t_lim=random.randint(5, 24)),
    OrderVar(id=10, rute_node=rutas[9].rute_nodes[1], cant=get_cantidad_aleatoria(rutas[9].rute_nodes[1]), t_lim=random.randint(5, 24)),
    OrderVar(id=11, rute_node=rutas[0].rute_nodes[0], cant=get_cantidad_aleatoria(rutas[0].rute_nodes[0]), t_lim=random.randint(5, 24)),
    OrderVar(id=12, rute_node=rutas[1].rute_nodes[2], cant=get_cantidad_aleatoria(rutas[1].rute_nodes[2]), t_lim=random.randint(5, 24)),
    OrderVar(id=13, rute_node=rutas[2].rute_nodes[1], cant=get_cantidad_aleatoria(rutas[2].rute_nodes[1]), t_lim=random.randint(5, 24)),
    OrderVar(id=14, rute_node=rutas[3].rute_nodes[0], cant=get_cantidad_aleatoria(rutas[3].rute_nodes[0]), t_lim=random.randint(5, 24)),
    OrderVar(id=15, rute_node=rutas[4].rute_nodes[2], cant=get_cantidad_aleatoria(rutas[4].rute_nodes[2]), t_lim=random.randint(5, 24)),
    OrderVar(id=16, rute_node=rutas[5].rute_nodes[1], cant=get_cantidad_aleatoria(rutas[5].rute_nodes[1]), t_lim=random.randint(5, 24)),
    OrderVar(id=17, rute_node=rutas[6].rute_nodes[0], cant=get_cantidad_aleatoria(rutas[6].rute_nodes[0]), t_lim=random.randint(5, 24)),
    OrderVar(id=18, rute_node=rutas[7].rute_nodes[2], cant=get_cantidad_aleatoria(rutas[7].rute_nodes[2]), t_lim=random.randint(5, 24)),
    OrderVar(id=19, rute_node=rutas[8].rute_nodes[1], cant=get_cantidad_aleatoria(rutas[8].rute_nodes[1]), t_lim=random.randint(5, 24)),
    OrderVar(id=20, rute_node=rutas[9].rute_nodes[0], cant=get_cantidad_aleatoria(rutas[9].rute_nodes[0]), t_lim=random.randint(5, 24))
]

#----------------------------------------------------------------------------------------------------------------------------------------
# Para experimentar


vehicles_json = '[  {    "id": 1,    "altura": 3.5,    "capacidad": 25000.0,    "tipo_de_combustible": ["gasolina", "diesel"],    "horarios_ocupados": {}  },  {    "id": 2,    "altura": 3.2,    "capacidad": 10000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 3,    "altura": 3.8,    "capacidad": 30000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 4,    "altura": 2.8,    "capacidad": 5000.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 5,    "altura": 4.0,    "capacidad": 40000.0,    "tipo_de_combustible": ["gasolina", "diesel", "gas"],    "horarios_ocupados": {}  },  {    "id": 6,    "altura": 3.3,    "capacidad": 15000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 7,    "altura": 3.6,    "capacidad": 22000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 8,    "altura": 2.9,    "capacidad": 7000.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 9,    "altura": 3.9,    "capacidad": 35000.0,    "tipo_de_combustible": ["gasolina", "diesel"],    "horarios_ocupados": {}  },  {    "id": 10,    "altura": 3.1,    "capacidad": 8000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 11,    "altura": 3.7,    "capacidad": 28000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 12,    "altura": 2.7,    "capacidad": 4000.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 13,    "altura": 4.1,    "capacidad": 45000.0,    "tipo_de_combustible": ["gasolina", "diesel", "gas"],    "horarios_ocupados": {}  },  {    "id": 14,    "altura": 3.4,    "capacidad": 12000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 15,    "altura": 3.5,    "capacidad": 20000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 16,    "altura": 3.0,    "capacidad": 6000.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 17,    "altura": 3.8,    "capacidad": 32000.0,    "tipo_de_combustible": ["gasolina", "diesel"],    "horarios_ocupados": {}  },  {    "id": 18,    "altura": 3.2,    "capacidad": 9000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 19,    "altura": 3.6,    "capacidad": 24000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 20,    "altura": 2.8,    "capacidad": 5500.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 21,    "altura": 3.9,    "capacidad": 38000.0,    "tipo_de_combustible": ["gasolina", "diesel", "gas"],    "horarios_ocupados": {}  },  {    "id": 22,    "altura": 3.3,    "capacidad": 13000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 23,    "altura": 3.7,    "capacidad": 26000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 24,    "altura": 2.9,    "capacidad": 6500.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 25,    "altura": 4.0,    "capacidad": 42000.0,    "tipo_de_combustible": ["gasolina", "diesel"],    "horarios_ocupados": {}  },  {    "id": 26,    "altura": 3.1,    "capacidad": 7500.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 27,    "altura": 3.8,    "capacidad": 29000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 28,    "altura": 2.7,    "capacidad": 4500.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 29,    "altura": 4.1,    "capacidad": 48000.0,    "tipo_de_combustible": ["gasolina", "diesel", "gas"],    "horarios_ocupados": {}  },  {    "id": 30,    "altura": 3.4,    "capacidad": 11000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 31,    "altura": 3.5,    "capacidad": 19000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 32,    "altura": 3.0,    "capacidad": 6800.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 33,    "altura": 3.8,    "capacidad": 33000.0,    "tipo_de_combustible": ["diesel", "gasolina"],    "horarios_ocupados": {}  },  {    "id": 34,    "altura": 3.2,    "capacidad": 8500.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },   {    "id": 35,    "altura": 3.6,    "capacidad": 23000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 36,    "altura": 2.8,    "capacidad": 5200.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 37,    "altura": 3.9,    "capacidad": 37000.0,    "tipo_de_combustible": ["gasolina", "diesel", "gas"],    "horarios_ocupados": {}  },  {    "id": 38,    "altura": 3.3,    "capacidad": 14000.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 39,    "altura": 3.7,    "capacidad": 27000.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 40,    "altura": 2.9,    "capacidad": 7200.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 41,    "altura": 4.0,    "capacidad": 41000.0,    "tipo_de_combustible": ["gasolina", "diesel"],    "horarios_ocupados": {}  },  {    "id": 42,    "altura": 3.1,    "capacidad": 7800.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },  {    "id": 43,    "altura": 3.8,    "capacidad": 28500.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 44,    "altura": 2.7,    "capacidad": 4200.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 45,    "altura": 4.1,    "capacidad": 47000.0,    "tipo_de_combustible": ["gasolina", "diesel", "gas"],    "horarios_ocupados": {}  },  {    "id": 46,    "altura": 3.4,    "capacidad": 11500.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  },   {    "id": 47,    "altura": 3.5,    "capacidad": 19500.0,    "tipo_de_combustible": ["gasolina"],    "horarios_ocupados": {}  },  {    "id": 48,    "altura": 3.0,    "capacidad": 6300.0,    "tipo_de_combustible": ["gas"],    "horarios_ocupados": {}  },  {    "id": 49,    "altura": 3.8,    "capacidad": 32500.0,    "tipo_de_combustible": ["diesel", "gasolina"],    "horarios_ocupados": {}  },  {    "id": 50,    "altura": 3.2,    "capacidad": 8200.0,    "tipo_de_combustible": ["diesel"],    "horarios_ocupados": {}  }]'

new_vehicles = []
vehicles_data = json.loads(vehicles_json)
for vehicle_data in vehicles_data:
    vehicle = Vehicle(
        id=vehicle_data["id"],
        altura=vehicle_data["altura"],
        capacidad=vehicle_data["capacidad"],
        tipo_de_combustible=vehicle_data["tipo_de_combustible"],
    )
    new_vehicles.append(vehicle)

new_orders_str = '''Order ID: 1, RuteNode: Node ID: 103, Rute ID: 1, Distance: 60, Cantidad: 6000, TiempoLimite: 8
Order ID: 2, RuteNode: Node ID: 202, Rute ID: 2, Distance: 55, Cantidad: 10000, TiempoLimite: 22
Order ID: 3, RuteNode: Node ID: 301, Rute ID: 3, Distance: 70, Cantidad: 5000, TiempoLimite: 23
Order ID: 4, RuteNode: Node ID: 403, Rute ID: 4, Distance: 120, Cantidad: 7000, TiempoLimite: 19
Order ID: 5, RuteNode: Node ID: 502, Rute ID: 5, Distance: 50, Cantidad: 38000, TiempoLimite: 20
Order ID: 6, RuteNode: Node ID: 601, Rute ID: 6, Distance: 140, Cantidad: 6000, TiempoLimite: 13
Order ID: 7, RuteNode: Node ID: 703, Rute ID: 7, Distance: 70, Cantidad: 11000, TiempoLimite: 18
Order ID: 8, RuteNode: Node ID: 802, Rute ID: 8, Distance: 80, Cantidad: 15000, TiempoLimite: 16
Order ID: 9, RuteNode: Node ID: 901, Rute ID: 9, Distance: 65, Cantidad: 25000, TiempoLimite: 24
Order ID: 10, RuteNode: Node ID: 1003, Rute ID: 10, Distance: 40, Cantidad: 9000, TiempoLimite: 13
Order ID: 11, RuteNode: Node ID: 102, Rute ID: 1, Distance: 45, Cantidad: 10000, TiempoLimite: 10
Order ID: 12, RuteNode: Node ID: 201, Rute ID: 2, Distance: 60, Cantidad: 9000, TiempoLimite: 6
Order ID: 13, RuteNode: Node ID: 303, Rute ID: 3, Distance: 50, Cantidad: 21000, TiempoLimite: 18
Order ID: 14, RuteNode: Node ID: 402, Rute ID: 4, Distance: 90, Cantidad: 6000, TiempoLimite: 10
Order ID: 15, RuteNode: Node ID: 501, Rute ID: 5, Distance: 75, Cantidad: 24000, TiempoLimite: 22
Order ID: 16, RuteNode: Node ID: 603, Rute ID: 6, Distance: 120, Cantidad: 5000, TiempoLimite: 5
Order ID: 17, RuteNode: Node ID: 702, Rute ID: 7, Distance: 60, Cantidad: 20000, TiempoLimite: 9
Order ID: 18, RuteNode: Node ID: 801, Rute ID: 8, Distance: 50, Cantidad: 11000, TiempoLimite: 14
Order ID: 19, RuteNode: Node ID: 903, Rute ID: 9, Distance: 75, Cantidad: 20000, TiempoLimite: 10
Order ID: 20, RuteNode: Node ID: 1002, Rute ID: 10, Distance: 80, Cantidad: 9000, TiempoLimite: 16'''

new_orders = [
    OrderVar(id=1, rute_node=rutas[0].rute_nodes[1], cant=6000, t_lim=random.randint(5, 24)),
    OrderVar(id=2, rute_node=rutas[1].rute_nodes[0], cant=10000, t_lim=random.randint(5, 24)),
    OrderVar(id=3, rute_node=rutas[2].rute_nodes[2], cant=5000, t_lim=random.randint(5, 24)),
    OrderVar(id=4, rute_node=rutas[3].rute_nodes[1], cant=7000, t_lim=random.randint(5, 24)),
    OrderVar(id=5, rute_node=rutas[4].rute_nodes[0], cant=38000, t_lim=random.randint(5, 24)),
    OrderVar(id=6, rute_node=rutas[5].rute_nodes[2], cant=6000, t_lim=random.randint(5, 24)),
    OrderVar(id=7, rute_node=rutas[6].rute_nodes[1], cant=11000, t_lim=random.randint(5, 24)),
    OrderVar(id=8, rute_node=rutas[7].rute_nodes[0], cant=15000, t_lim=random.randint(5, 24)),
    OrderVar(id=9, rute_node=rutas[8].rute_nodes[2], cant=25000, t_lim=random.randint(5, 24)),
    OrderVar(id=10, rute_node=rutas[9].rute_nodes[1], cant=9000, t_lim=random.randint(5, 24)),
    OrderVar(id=11, rute_node=rutas[0].rute_nodes[0], cant=10000, t_lim=random.randint(5, 24)),
    OrderVar(id=12, rute_node=rutas[1].rute_nodes[2], cant=9000, t_lim=random.randint(5, 24)),
    OrderVar(id=13, rute_node=rutas[2].rute_nodes[1], cant=21000, t_lim=random.randint(5, 24)),
    OrderVar(id=14, rute_node=rutas[3].rute_nodes[0], cant=6000, t_lim=random.randint(5, 24)),
    OrderVar(id=15, rute_node=rutas[4].rute_nodes[2], cant=24000, t_lim=random.randint(5, 24)),
    OrderVar(id=16, rute_node=rutas[5].rute_nodes[1], cant=5000, t_lim=random.randint(5, 24)),
    OrderVar(id=17, rute_node=rutas[6].rute_nodes[0], cant=20000, t_lim=random.randint(5, 24)),
    OrderVar(id=18, rute_node=rutas[7].rute_nodes[2], cant=11000, t_lim=random.randint(5, 24)),
    OrderVar(id=19, rute_node=rutas[8].rute_nodes[1], cant=20000, t_lim=random.randint(5, 24)),
    OrderVar(id=20, rute_node=rutas[9].rute_nodes[0], cant=9000, t_lim=random.randint(5, 24))
]