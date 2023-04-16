import networkx as nx

# Define the three graphs
g1 = nx.read_gml("G1Com.gml")
g2 = nx.read_gml("G2Com.gml")
g3 = nx.read_gml("G3Com.gml")

# Compute the major edges
major_edges = list(set(g1.edges()) & set(g2.edges())) + \
              list(set(g2.edges()) & set(g3.edges())) + \
              list(set(g1.edges()) & set(g3.edges()))

# Construct the new graph containing the major edges
new_graph = nx.DiGraph(major_edges)

nx.write_gml(new_graph, "majorGraph.gml")