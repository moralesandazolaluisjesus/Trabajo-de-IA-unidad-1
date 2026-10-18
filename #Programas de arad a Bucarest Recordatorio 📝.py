# Tabla de heurística hacia Bucharest
heuristica = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 178,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 98,
    "Rimnicu Vilcea": 193, 
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

# Conexiones del mapa con sus costos reales
mapa = {
    "Arad": {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    "Zerind": {'Arad': 75, 'Oradea': 71},
    "Oradea": {'Zerind': 71, 'Sibiu': 151},
    "Timisoara": {'Arad': 118, 'Lugoj': 111},
    "Lugoj": {'Timisoara': 111, 'Mehadia': 70},
    "Mehadia": {'Lugoj': 70, 'Drobeta': 75},
    "Drobeta": {'Mehadia': 75, 'Craiova': 120},
    "Craiova": {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    "Sibiu": {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    "Rimnicu Vilcea": {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    "Fagaras": {'Sibiu': 99, 'Bucharest': 211},
    "Pitesti": {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    "Bucharest": {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    "Giurgiu": {'Bucharest': 90},
    "Urziceni": {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    "Hirsova": {'Urziceni': 98, 'Eforie': 86},
    "Eforie": {'Hirsova': 86},
    "Vaslui": {'Urziceni': 142, 'Iasi': 92},
    "Iasi": {'Vaslui': 92, 'Neamt': 87},
    "Neamt": {'Iasi': 87}
}

def a_estrella(inicio, meta):
    # Lista de pendientes: [f, g, ciudad actual, ruta recorrida]
    abiertos = [[heuristica[inicio], 0, inicio, [inicio]]]
    visitados = set()

    while abiertos:
        # buscamos manualmente el índice del nodo con menor f
        indice_mejor = 0
        for i in range(1, len(abiertos)):
            if abiertos[i][0] < abiertos[indice_mejor][0]:
                indice_mejor = i
        
        # Sacamos el mejor nodo de la lista usando su posición
        f_actual, g_actual, actual, ruta = abiertos.pop(indice_mejor)

        # ¿Llegamos a la meta?
        if actual == meta:
            return ruta, g_actual

        if actual in visitados:
            continue
        visitados.add(actual)

        # Revisar vecinos
        for vecino, costo_arista in mapa.get(actual, {}).items():
            if vecino in visitados:
                continue
            
            # Calcular g, h y f para el vecino
            g_vecino = g_actual + costo_arista
            h_vecino = heuristica.get(vecino, 0)
            f_vecino = g_vecino + h_vecino
            
            nueva_ruta = ruta + [vecino]
            abiertos.append([f_vecino, g_vecino, vecino, nueva_ruta])

    return None, 0


ruta_optima, costo_total = a_estrella('Arad', 'Bucharest')
print("Ruta óptima:", ruta_optima)
print("Costo total:", costo_total)