import random
from variable import Rute,RuteNode,Vehicle,OrderVar



rutas = [
    Rute(
        id=1,
        ancho_m=2.55,
        altura_m=3.40,
        peso_m=15000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=102, rute_id=1, distance=15),
            RuteNode(node_id=103, rute_id=1, distance=30),
            RuteNode(node_id=101, rute_id=1, distance=40),
        ]
    ),
    Rute(
        id=2,
        ancho_m=2.45,
        altura_m=3.30,
        peso_m=10000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="rural",
        rute_nodes=[
            RuteNode(node_id=202, rute_id=2, distance=8),
            RuteNode(node_id=203, rute_id=2, distance=18),
            RuteNode(node_id=201, rute_id=2, distance=50),
        ]
    ),
    Rute(
        id=3,
        ancho_m=2.70,
        altura_m=3.70,
        peso_m=30000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=302, rute_id=3, distance=25),
            RuteNode(node_id=303, rute_id=3, distance=50),
            RuteNode(node_id=301, rute_id=3, distance=80),
        ]
    ),
    Rute(
        id=4,
        ancho_m=2.50,
        altura_m=3.25,
        peso_m=8000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="urbana",
        rute_nodes=[
            RuteNode(node_id=402, rute_id=4, distance=5),
            RuteNode(node_id=403, rute_id=4, distance=12),
            RuteNode(node_id=401, rute_id=4, distance=20),
        ]
    ),  
    Rute(
        id=5,
        ancho_m=2.85,
        altura_m=4.00,
        peso_m=45000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=502, rute_id=5, distance=30),
            RuteNode(node_id=503, rute_id=5, distance=65),
            RuteNode(node_id=501, rute_id=5, distance=75),
        ]
    ),
    Rute(
        id=6,
        ancho_m=2.40,
        altura_m=3.20,
        peso_m=6000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="urbana",
        rute_nodes=[
            RuteNode(node_id=602, rute_id=6, distance=3),
            RuteNode(node_id=603, rute_id=6, distance=7),
            RuteNode(node_id=601, rute_id=6, distance=15),
        ]
    ),
    Rute(
        id=7,
        ancho_m=2.60,
        altura_m=3.60,
        peso_m=25000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="mixta",
        rute_nodes=[
            RuteNode(node_id=702, rute_id=7, distance=20),
            RuteNode(node_id=703, rute_id=7, distance=45),
            RuteNode(node_id=701, rute_id=7, distance=70),
        ]
    ),
    Rute(
        id=8,
        ancho_m=2.55,
        altura_m=3.45,
        peso_m=18000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="rural",
        rute_nodes=[
            RuteNode(node_id=802, rute_id=8, distance=12),
            RuteNode(node_id=803, rute_id=8, distance=28),
            RuteNode(node_id=801, rute_id=8, distance=40),
        ]
    ),
    Rute(
        id=9,
        ancho_m=2.75,
        altura_m=3.90,
        peso_m=35000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="autopista",
        rute_nodes=[
            RuteNode(node_id=902, rute_id=9, distance=40),
            RuteNode(node_id=903, rute_id=9, distance=85),
            RuteNode(node_id=901, rute_id=9, distance=95),
        ]
    ),
    Rute(
        id=10,
        ancho_m=2.48,
        altura_m=3.35,
        peso_m=11000,
        tipo_de_combustible=["diesel", "gasolina", "hidrogeno", "gas"],
        tipo_de_zona="mixta",
        rute_nodes=[
            RuteNode(node_id=1002, rute_id=10, distance=7),
            RuteNode(node_id=1003, rute_id=10, distance=16),
            RuteNode(node_id=1001, rute_id=10, distance=25),
        ]
    )
]

vehicles = [
    Vehicle(id=1, ancho=2.45, altura=3.30, capacidad=8000, tipo_de_combustible= ["diesel", "gasolina"]),   # Estrecho, estándar, baja
    Vehicle(id=2, ancho=2.55, altura=3.60, capacidad=20000, tipo_de_combustible=["diesel", "gasolina"]),  # Estándar, alto, media
    Vehicle(id=3, ancho=2.65, altura=4.00, capacidad=50000, tipo_de_combustible=["diesel", "gasolina"]), # Muy ancho, muy alto, muy alta
    Vehicle(id=4, ancho=2.48, altura=3.40, capacidad=10000, tipo_de_combustible=["diesel", "gasolina"]), # Estrecho, estándar, baja
    Vehicle(id=5, ancho=2.58, altura=3.70, capacidad=30000, tipo_de_combustible=["diesel", "gasolina"]), # Estándar, alto, alta
    Vehicle(id=6, ancho=2.70, altura=3.25, capacidad=35000, tipo_de_combustible=["diesel", "gasolina"]), # Muy ancho, estándar, alta
    Vehicle(id=7, ancho=2.52, altura=4.10, capacidad=55000, tipo_de_combustible=["diesel", "gasolina"]), # Estándar, muy alto, muy alta
    Vehicle(id=8, ancho=2.62, altura=3.45, capacidad=18000, tipo_de_combustible=["diesel", "gasolina"])  # Muy ancho, estándar, media
]

rangos_cantidad = {
    "baja": (5000, 11000),
    "media": (8000, 10000),
    "alta": (6000, 8000),
    "muy alta": (5000, 6000)
}

# Función para obtener una cantidad aleatoria según la categoría
def get_cantidad_aleatoria():
    categoria = random.choice(list(rangos_cantidad.keys()))
    min_val, max_val = rangos_cantidad[categoria]
    return random.randint(min_val, max_val)

orders = [
    OrderVar(id=1, rute_node=rutas[0].rute_nodes[1], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=2, rute_node=rutas[1].rute_nodes[0], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=3, rute_node=rutas[2].rute_nodes[2], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=4, rute_node=rutas[3].rute_nodes[1], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=5, rute_node=rutas[4].rute_nodes[0], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=6, rute_node=rutas[5].rute_nodes[2], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=7, rute_node=rutas[6].rute_nodes[1], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=8, rute_node=rutas[7].rute_nodes[0], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=9, rute_node=rutas[8].rute_nodes[2], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=10, rute_node=rutas[9].rute_nodes[1], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=11, rute_node=rutas[0].rute_nodes[0], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=12, rute_node=rutas[1].rute_nodes[2], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=13, rute_node=rutas[2].rute_nodes[1], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=14, rute_node=rutas[3].rute_nodes[0], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=15, rute_node=rutas[4].rute_nodes[2], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=16, rute_node=rutas[5].rute_nodes[1], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=17, rute_node=rutas[6].rute_nodes[0], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=18, rute_node=rutas[7].rute_nodes[2], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=19, rute_node=rutas[8].rute_nodes[1], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24)),
    OrderVar(id=20, rute_node=rutas[9].rute_nodes[0], cant=get_cantidad_aleatoria(), t_lim=random.randint(5, 24))
]