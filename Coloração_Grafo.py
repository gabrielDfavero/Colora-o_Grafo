import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

def verifica_numero_cores(G, num_cores):
    maior_clique = len(max(nx.find_cliques(G), key=len))
    if(maior_clique <= num_cores):
      return True

def cor_vertice(G, num_cores):
    while True:
        cores = {}
        for no in G.nodes():
            cores_disponiveis = set(range(num_cores))
            for vizinho in G.neighbors(no):
                if vizinho in cores:
                    cores_disponiveis.discard(cores[vizinho])
            if cores_disponiveis:
                cores[no] = random.choice(list(cores_disponiveis))
            else:
                break
        else:
            return cores

def main():
    num_vertices = int(input("Digite o número de vértices: "))
    num_cores = int(input("Digite o número de cores: "))
    G = nx.gnp_random_graph(num_vertices, 0.4)

    if not verifica_numero_cores(G, num_cores):
        print("Número de cores insuficiente para colorir o grafo.")
    else:
      coresDict = cor_vertice(G, num_cores)
      cores = plt.cm.turbo(np.linspace(0, 1, num_cores))
      pos = nx.circular_layout(G)
      nx.draw(G, pos, with_labels=True, node_color=[cores[coresDict[node]] for node in G.nodes()])
      plt.title('Grafo Colorido')
      plt.show()
      print(coresDict)
main();