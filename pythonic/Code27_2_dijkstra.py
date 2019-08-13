#File name: dijkstraalgorithm.py
#Author: Luis Carlos <luiscarlos.sf@outlook.com>

import time
import networkx as nx
from filaprioritaria import PriorityQueue #Fila de Prioridade
import sys #Fornece o "Infinito"

"""Determines the distance between the fonte vertex to all other vertices of the digrafo

        Parameters
        ----------
        digrafo : digraph
            A network digraph

        fonte: node
            A node can be any hashable Python object except None.
        
        Returns
        --------
        caminho_minimo[::-1]: minimum path and weight
            A list with the minimum path nodes and a dictionary 
            with the weight of the path. 
        
        Examples
        --------
        >>> G = nx.DiGraph()
        >>> e = [(1, 2, {'weight': 10}), (2, 3, {'weight':11}), (3, 4, {'weight':8})] # list of edges
        >>> G = nx.DiGraph(e)
        >>> minimum_path = dijkstra(G, 1, 4)
        
        Notes
        -----
        A hashable object is one that can be used as a key in a Python
        dictionary. This includes strings, numbers, tuples of strings
        and numbers, etc.

        On many platforms hashable items also include mutables such as
        NetworkX Graphs, though one should be careful that the hash
        doesn't change on mutables.
        """

def dijkstra(digrafo, fonte, destino):
    #Passo 1
    r_dist = list()
    for node in digrafo:
        digrafo.nodes[node]['distance'] = sys.maxsize
        digrafo.nodes[node]['rotulado'] = False #Indica se o grafo foi rotulado ou não
    digrafo.nodes[fonte]['distance']= 0

    #Inicio
    nr = PriorityQueue() #Fila de prioriadade vazia dos nós não rotulados.
    for node in list(digrafo):
        nr.insert((digrafo.nodes[node]['distance'], node)) #Inserir tuplas (distancia, node)
    #Passo 2
    while nr.getTamanho()!=0:
        #Passo 2.1
        u = nr.remove_min() #Retorna (distancia, nó)
        k = u[1]
        #Passo 2.2
        digrafo.nodes[k]['rotulado']=True
        r_dist.append(u)
        #Passo 2.3
        for j in list(digrafo.successors(k)):
            if not digrafo.nodes[j]['rotulado']:
                novo_custo = digrafo.nodes[k]['distance'] + digrafo.edges[k, j]['weight']
                if novo_custo < digrafo.nodes[j]['distance']:
                    digrafo.nodes[j]['distance'] = novo_custo
                    digrafo.nodes[j]['precedente'] = k
                    nr.increase_key(j, novo_custo)
    #Determinando Caminho Mínimo
    z = digrafo.nodes[destino]['distance']
    i = destino
    caminho_minimo = [{'peso':z}]
    while True:
        try:
            caminho_minimo.append(i)
            i = digrafo.nodes[i]['precedente']
        except:
            break

    return caminho_minimo[::-1]

def teste():
    digrafo = nx.DiGraph()
    digrafo.add_nodes_from(range(1, 10))
    digrafo.add_edges_from([(1,2,{'weight':11}),(1,3,{'weight':9}),(2,4,{'weight':4}),\
                        (2,5,{'weight':8}), (3,4,{'weight':8}), (3,5,{'weight':6}), \
                        (4,6,{'weight':6}),(4,7,{'weight':5}), (5,7,{'weight':6}),\
                        (5,8,{'weight':4}), (6,9,{'weight':6}),(7,9,{'weight':4}), (8,9,{'weight':6})])

    print("Nodes\n", digrafo.nodes())
    print("Edges\n", digrafo.edges(data=True))
    #nx.draw(digrafo)
    fonte = input("Digite o vértice fonte: ")
    try:
        fonte = int(fonte)
    except():
        pass

    destino = input("Digite o vértice destino: ")
    try:
        destino = int(destino)
    except():
        pass

    if fonte in digrafo:
        if destino in digrafo:
            start= time.time()
            caminho_minimo=dijkstra(digrafo, fonte, destino)
            tempo = time.time()-start
            print("Algoritmo dijkstra executado em ", tempo,"segundos.")
            print("Caminho Minimo: ", caminho_minimo)

        else:
            print("O vértice destino não está no grafo")
    else:
        print("O vértice fonte não está no grafo")

if __name__=="__main__":
    teste()