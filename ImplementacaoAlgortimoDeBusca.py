"""
Planejamento de rotas com trânsito usando o algoritmo A* (NetworkX)
Autores: Ana Clara Araujo, Thalita Amorim, Caua Veloso Oliveira
Disciplina: Inteligência Artificial 

Descrição:
    - Cidades modeladas como nós de um grafo.
    - Estradas entre cidades possuem pesos (tempo de viagem).
    - Penalidades de trânsito simulam congestionamentos.
    - O algoritmo A* encontra o caminho mais rápido.
"""

import networkx as nx
import math
import matplotlib.pyplot as plt

# 1. Heurística (distância em linha reta)
def heuristica(u, v, G):
    x1, y1 = G.nodes[u]['coord']
    x2, y2 = G.nodes[v]['coord']
    return math.hypot(x1 - x2, y1 - y2)

# 2. Criação do grafo com MAIS ARESTAS
def criar_grafo(traffic=None):
    G = nx.Graph()

    # Nós (coordenadas fictícias)
    coords = {
        'A': (0, 0),
        'B': (4, 1),
        'C': (8, 0),
        'D': (4, -3),
        'E': (12, 3),
        'F': (16, 0),
        'G': (10, -4),
        'H': (14, -3)
    }

    # Arestas: (cidade1, cidade2, tempo_base)
    estradas = [
        ('A', 'B', 10),
        ('A', 'D', 12),
        ('B', 'C', 9),
        ('B', 'D', 5),
        ('B', 'E', 14),     # nova
        ('C', 'D', 8),
        ('C', 'E', 11),
        ('C', 'F', 25),
        ('C', 'G', 12),     # nova
        ('D', 'G', 10),     # nova
        ('E', 'F', 10),
        ('E', 'H', 9),      # nova
        ('G', 'H', 7),      # nova
        ('H', 'F', 8)       # nova
    ]

    # Adiciona nós
    for cidade, coord in coords.items():
        G.add_node(cidade, coord=coord)

    # Penalidades
    traffic = traffic or {}

    # Adiciona arestas com penalidades
    for u, v, tempo in estradas:
        penalidade = traffic.get((u, v), 0) or traffic.get((v, u), 0)
        total = tempo + penalidade
        G.add_edge(u, v, time=total, base=tempo, penalty=penalidade)

    return G

# 3. Execução do A*
def executar_a_star(G, inicio, destino):
    caminho = nx.astar_path(
        G, inicio, destino,
        heuristic=lambda u, v: heuristica(u, v, G),
        weight='time'
    )
    custo = nx.astar_path_length(
        G, inicio, destino,
        heuristic=lambda u, v: heuristica(u, v, G),
        weight='time'
    )
    return caminho, custo

# 4. Visualização
def mostrar_grafo(G, caminho, titulo):
    pos = nx.get_node_attributes(G, 'coord')
    rotulos = {(u, v): f"{d['time']} min" for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=900, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=rotulos, font_color='red')

    edges = list(zip(caminho, caminho[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=4, edge_color='green')

    plt.title(titulo)
    plt.axis('off')
    plt.show()

# 5. Programa principal
def main():
    print("=== PLANEJAMENTO DE ROTAS COM A* ===")
    print("1 - Executar sem trânsito")
    print("2 - Executar com trânsito (simulado)")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\n[SEM TRÂNSITO]")
        G = criar_grafo()
        caminho, custo = executar_a_star(G, 'A', 'F')
        print("Melhor caminho:", caminho)
        print("Tempo total:", custo, "min")
        mostrar_grafo(G, caminho, "Rota Sem Trânsito")

    elif opcao == '2':
        print("\n[COM TRÂNSITO]")
        trafego = {
            ('B', 'C'): 8,
            ('C', 'E'): 10,
            ('G', 'H'): 7,
            ('H', 'F'): 12
        }
        G = criar_grafo(trafego)
        caminho, custo = executar_a_star(G, 'A', 'F')
        print("Melhor caminho:", caminho)
        print("Tempo total:", custo, "min")
        mostrar_grafo(G, caminho, "Rota Com Trânsito")

    else:
        print("Opção inválida!")

# EXECUÇÃO
if __name__ == "__main__":
    main()

