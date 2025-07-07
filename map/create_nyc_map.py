"""
Este script crea un grafo de la ciudad de New York usando OSMNX
y lo adapta a las clases Node y Map definidas en mapa_test.py
"""

import osmnx as ox
import networkx as nx
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mapa_test import Node, Map

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib no está instalado. Las visualizaciones no estarán disponibles.")
import pickle
import os

def create_nyc_map(location='Manhattan, New York City, New York, USA', 
                   network_type='drive', 
                   save_fig=True, 
                   save_map=True):
    """
    Crea un grafo de New York City usando OSMNX y lo adapta a las clases Node y Map.
    
    Args:
        location: Nombre del lugar (por defecto Manhattan)
        network_type: Tipo de red ('drive', 'walk', 'bike', etc.)
        save_fig: Si se debe guardar una imagen del grafo
        save_map: Si se debe guardar el mapa como un archivo pickle
        
    Returns:
        Un objeto Map con el grafo de la ciudad
    """
    print(f"Descargando mapa de {location}...")
    
    # Extraer grafo de OpenStreetMap
    G = ox.graph_from_place(location, network_type=network_type)
    
    # Proyectar el grafo para cálculos de distancia más precisos
    G_proj = ox.project_graph(G)
    
    # Convertir el grafo a un formato más manejable
    nodes, edges = ox.graph_to_gdfs(G_proj)
    
    print(f"Grafo descargado: {len(G.nodes)} nodos y {len(G.edges)} aristas")
    
    # Crear un objeto Map vacío
    nyc_map = Map(id=f"nyc_{network_type}", nodes=[], edges={})
    
    # Diccionario para rastrear nodos creados
    created_nodes = {}
    
    print("Creando nodos...")
    # Crear nodos
    for node_id, data in G.nodes(data=True):
        new_node = Node(id=node_id, map=nyc_map)
        created_nodes[node_id] = new_node
        nyc_map.nodes.append(new_node)
    
    print("Creando aristas y estableciendo adyacencias...")
    # Crear aristas y conectar nodos
    for u, v, data in G.edges(data=True):
        # Obtener la distancia en metros (si existe, de lo contrario usar 0)
        distance = data.get('length', 0)
        
        # Agregar adyacencia solo en el sentido de la arista (grafo dirigido)
        try:
            created_nodes[u].add_adyacent(distance, created_nodes[v])
        except Exception as e:
            print(f"Error al añadir adyacencia de {u} a {v}: {e}")
            # printear la arista
            # print(f"Arista: {u} -> {v}, distancia: {distance}")
            # #comprobar si el nodo v existe en created_nodes
            # if v not in created_nodes:
            #     print(f"El nodo {v} no existe en created_nodes, creando nuevo nodo.")
            #     new_node = Node(id=v, map=nyc_map)
            #     created_nodes[v] = new_node
            #     nyc_map.nodes.append(new_node)
            # #comprobar si el nodo u existe en created_nodes
            # if u not in created_nodes:
            #     print(f"El nodo {u} no existe en created_nodes, creando nuevo nodo.")
            #     new_node = Node(id=u, map=nyc_map)
            #     created_nodes[u] = new_node
            #     nyc_map.nodes.append(new_node)
        
        # No agregar la arista en sentido contrario, aunque el grafo sea dirigido
        # Actualizar el diccionario de aristas en el mapa
        nyc_map.edges[(u, v)] = distance
    
    print(f"Mapa creado: {nyc_map}")
    
    # Guardar una imagen del grafo si se solicita
    if save_fig:
        print("Generando visualización del mapa...")
        fig, ax = ox.plot_graph(G, node_size=10, edge_linewidth=0.5, 
                                show=False, close=False)
        plt.title(f"Mapa de {location} - {network_type}")
        plt.tight_layout()
        fig_path = f"nyc_{network_type}_map.png"
        plt.savefig(fig_path, dpi=300)
        plt.close()
        print(f"Visualización guardada en {fig_path}")
    
    # Guardar el mapa como un archivo pickle si se solicita
    if save_map:
        print("Guardando objeto Map...")
        pickle_path = f"nyc_{network_type}_map.pkl"
        with open(pickle_path, 'wb') as f:
            pickle.dump(nyc_map, f)
        print(f"Mapa guardado en {pickle_path}")
    
    return nyc_map

def load_map(file_path):
    """
    Carga un mapa desde un archivo pickle
    
    Args:
        file_path: Ruta del archivo pickle
        
    Returns:
        Un objeto Map con el grafo cargado
    """
    with open(file_path, 'rb') as f:
        return pickle.load(f)

if __name__ == "__main__":
    # Crear mapa de Manhattan (por defecto)
    print("Iniciando creación del mapa de New York City...")
    
    try:
        # Puedes cambiar estos parámetros según necesites
        nyc_map = create_nyc_map(
            location='Manhattan, New York City, New York, USA',
            network_type='drive',
            save_fig=True,
            save_map=True
        )
        
        print("\nResumen del mapa:")
        print(f"ID del mapa: {nyc_map.id}")
        print(f"Número de nodos: {len(nyc_map.nodes)}")
        print(f"Número de aristas: {len(nyc_map.edges)}")
        
        # Mostrar algunos nodos de ejemplo con sus adyacentes
        print("\nEjemplo de nodos y sus adyacencias:")
        for i, node in enumerate(nyc_map.nodes[:3]):  # Mostrar solo los primeros 3 nodos
            print(f"Nodo {i+1}: ID {node.id}")
            print(f"  Número de adyacentes: {len(node.adyacents)}")
            if node.adyacents:
                print(f"  Ejemplo de distancia al primer adyacente: {node.adyacents_distances[node.adyacents[0]]:.2f} metros")
            print()
        
    except Exception as e:
        print(f"Error al crear el mapa: {e}")
