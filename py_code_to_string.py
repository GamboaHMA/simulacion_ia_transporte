vehicle_class = '''
    class Vehicle():  
        def __init__(self, id:int, altura:float, capacidad:float, tipo_de_combustible: list[str]):
            self.id: int = id
            self.altura: float = altura 
            self.capacidad: float = capacidad 
            self.tipo_de_combustible: list[str] = tipo_de_combustible
            self.horarios_ocupados:dict[OrderVar, tuple[float,float]] = {}
'''

vehicle_order = '''
Generame
'''

tipos_de_combustible = '''
    tipos_de_combustible = {
        "gasolina",
        "diesel",
        "hidrogeno",
        "gas"
    }
'''