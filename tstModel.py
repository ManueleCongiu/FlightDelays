from datetime import datetime

import networkx as nx

from model.model import Model

myModel = Model()
myModel.buildGraph(5)
myModel.printGraphDetails()

v0 = myModel.getAllNodes()[0]

connessa = list(nx.node_connected_component(myModel._grafo, v0))
v1 = connessa[10]

pathD = myModel.trovaCamminoD(v0, v1)
pathBFS = myModel.trovaCamminoBFS(v0, v1)
pathDFS = myModel.trovaCamminoDFS(v0, v1)

print("\n\nMetodo di Dijkstra:")
print("-------------------------------------------------")
print(*pathD, sep='\n')
print("-------------------------------------------------\n")
print("Metodo albero Breadth first:")
print("-------------------------------------------------")
print(*pathBFS, sep='\n')
print("-------------------------------------------------\n")
print("Metodo albero Depth first:")
print("-------------------------------------------------")
print(*pathDFS, sep='\n')
print("-------------------------------------------------\n")


tic = datetime.now()
bestPath, bestScore = myModel.getCamminoOttimo(v0, v1, 4)
print(f"\nCammino ottimo tra {v0} e {v1} ha peso {bestScore}. \nTrovato in: {datetime.now() - tic} secondi")
print("-------------------------------------------------")
print(*bestPath, sep='\n')
print("-------------------------------------------------\n")

