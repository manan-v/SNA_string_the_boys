import networkx as nx

graph = nx.read_gml("testNodeGraph.gml")

print(list(graph.nodes()))