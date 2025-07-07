import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from map.create_nyc_map import create_nyc_map as create_map
from map.demo_nyc_map import find_shortest_path
import unittest
import pickle

class TestNYCMap(unittest.TestCase):
    def setUp(self):
        # Crear un mapa de ejemplo para las pruebas
        self.map = create_map(location='Manhattan, New York City, New York, USA', network_type='drive', save_fig=False, save_map=False)
    
    def test_map_creation(self):
        self.assertIsNotNone(self.map)
        self.assertGreater(len(self.map.nodes), 0)
        self.assertGreater(len(self.map.edges), 0)
    
    def test_node_adyacents(self):
        for node in self.map.nodes:
            self.assertIsInstance(node.adyacents, list)
            self.assertIsInstance(node.adyacents_distances, dict)
    
    def test_find_shortest_path(self):
        if len(self.map.nodes) < 2:
            self.skipTest("No hay suficientes nodos para encontrar una ruta")
        
        start_node_idx = 0
        end_node_idx = 1
        
        path, distance = find_shortest_path(self.map, start_node_idx, end_node_idx)
        
        self.assertIsInstance(path, list)
        self.assertGreaterEqual(distance, 0)  # La distancia no puede ser negativa
        self.assertGreater(len(path), 0)  # Debe haber al menos un nodo
        self.assertEqual(path[0].id, self.map.nodes[start_node_idx].id)
        self.assertEqual(path[-1].id, self.map.nodes[end_node_idx].id)
    def test_save_load_map(self):
        # Guardar el mapa en un archivo pickle
        pickle_path = 'test_nyc_map.pkl'
        with open(pickle_path, 'wb') as f:
            pickle.dump(self.map, f)
        
        # Cargar el mapa desde el archivo
        loaded_map = create_map(location='Manhattan, New York City, New York, USA', network_type='drive', save_fig=False, save_map=False)
        
        self.assertIsNotNone(loaded_map)
        self.assertEqual(len(loaded_map.nodes), len(self.map.nodes))
        self.assertEqual(len(loaded_map.edges), len(self.map.edges))
        
        # Limpiar el archivo creado
        os.remove(pickle_path)
    def tearDown(self):
        # Aquí podrías limpiar recursos si es necesario
        pass
if __name__ == '__main__':
    unittest.main()
#     # Ejecutar las pruebas
#     unittest.main()
#     # Si estás ejecutando este script directamente, puedes descomentar la línea anterior para ejecutar las pruebas.