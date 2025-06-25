import random
from variable import Rute,RuteNode,Vehicle,OrderVar



rutas = [
    Rute(
        id=1,
        altura_m=3.40,
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
        altura_m=3.30,
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
        altura_m=3.70,
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
        altura_m=3.25,
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
        altura_m=3.20,
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
        altura_m=3.60,
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
        altura_m=3.45,
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
        altura_m=3.35,
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

