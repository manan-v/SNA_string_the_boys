import networkx as nx

# Create four example directed graphs
G1 = nx.read_gml("G1Com.gml")
# G1.add_edges_from([(1,2), (2,3), (3,1)])

G2 = nx.read_gml("G2Com.gml")
# G2.add_edges_from([(2,3), (3,4), (4,2)])

G3 = nx.read_gml("G3Com.gml")
# G3.add_edges_from([(3,4), (4,5), (5,3)])

G4 = nx.read_gml("G4Com.gml")
# G4.add_edges_from([(4,5), (5,6), (6,4)])

# Find the intersection of the four graphs
intersection = nx.intersection_all([G1, G2, G3, G4])

# Create a new graph for the intersection and add its nodes and edges
intersection_graph = nx.DiGraph()
intersection_graph.add_nodes_from(intersection.nodes)
intersection_graph.add_edges_from(intersection.edges)

# Write the intersection graph to a GML file
nx.write_gml(intersection_graph, "intersection_graph.gml")
