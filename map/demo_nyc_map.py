"""
Script para demostrar el uso del mapa de New York creado con OSMNX
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from map.create_nyc_map import create_nyc_map, load_map

def find_shortest_path(map_obj, start_node_idx, end_node_idx):
    """
    Implementación simple del algoritmo de Dijkstra para encontrar
    la ruta más corta entre dos nodos.
    
    Args:
        map_obj: Objeto Map con el grafo de la ciudad
        start_node_idx: Índice del nodo de inicio en la lista map_obj.nodes
        end_node_idx: Índice del nodo de destino en la lista map_obj.nodes
    
    Returns:
        Una tupla (ruta, distancia_total) donde ruta es una lista de nodos
    """
    import heapq
    
    # Obtener los nodos de inicio y fin
    start_node = map_obj.nodes[start_node_idx]
    end_node = map_obj.nodes[end_node_idx]
    
    print(f"Buscando ruta más corta del nodo {start_node.id} al nodo {end_node.id}")
    
    # Inicializar variables para Dijkstra
    distances = {node: float('infinity') for node in map_obj.nodes}
    distances[start_node] = 0
    previous_nodes = {node: None for node in map_obj.nodes}
    priority_queue = [(0, start_node)]
    visited = set()
    
    # Algoritmo de Dijkstra
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == end_node:
            break
        
        for adjacent_node in current_node.adyacents:
            distance = current_distance + current_node.adyacents_distances[adjacent_node]
            
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                previous_nodes[adjacent_node] = current_node
                heapq.heappush(priority_queue, (distance, adjacent_node))
    
    # Reconstruir la ruta
    path = []
    current = end_node
    
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    
    path.reverse()
    
    if path[0] != start_node:
        print("No se encontró una ruta entre los nodos especificados")
        return [], 0
    
    return path, distances[end_node]

def main():
    # Verificar si ya existe un archivo del mapa
    map_file = "nyc_drive_map.pkl"
    
    if os.path.exists(map_file):
        print(f"Cargando mapa existente desde {map_file}...")
        nyc_map = load_map(map_file)
    else:
        print("Creando nuevo mapa de New York (puede tardar varios minutos)...")
        nyc_map = create_nyc_map(
            # Para un mapa más pequeño y rápido, podemos usar un área más específica
            location='Greenwich Village, Manhattan, New York City, USA',
            network_type='drive',
            save_fig=True,
            save_map=True
        )
    
    # Mostrar información del mapa
    print("\nInformación del mapa:")
    print(f"ID: {nyc_map.id}")
    print(f"Nodos: {len(nyc_map.nodes)}")
    print(f"Aristas: {len(nyc_map.edges)}")
    
    # Seleccionar dos nodos aleatorios para encontrar una ruta
    import random
    
    if len(nyc_map.nodes) > 10:  # Asegurarse de que haya suficientes nodos
        start_idx = random.randint(0, len(nyc_map.nodes) - 1)
        end_idx = random.randint(0, len(nyc_map.nodes) - 1)
        
        # Asegurarse de que son diferentes
        while end_idx == start_idx:
            end_idx = random.randint(0, len(nyc_map.nodes) - 1)
        
        # Encontrar la ruta más corta
        path, total_distance = find_shortest_path(nyc_map, start_idx, end_idx)
        
        if path:
            print(f"\nRuta encontrada con {len(path)} nodos y distancia total de {total_distance:.2f} metros")
            print("Nodos en la ruta:")
            for i, node in enumerate(path[:5]):  # Mostrar solo los primeros 5 nodos
                print(f"  {i+1}. ID: {node.id}")
            
            if len(path) > 5:
                print(f"  ... y {len(path) - 5} nodos más.")
    else:
        print("No hay suficientes nodos para calcular una ruta.")

if __name__ == "__main__":
    main()
