import networkx as nx

G1=nx.read_gml("G1Hopped.gml")
G2=nx.read_gml("G2Hopped.gml")
G3=nx.read_gml("G3Hopped.gml")
G4=nx.read_gml("majorGraph.gml")
three = nx.compose_all([G1,G2,G3])

intersection = nx.intersection_all([three,G4])

# Create a new graph for the intersection and add its nodes and edges
intersection_graph = nx.DiGraph()
intersection_graph.add_nodes_from(intersection.nodes)
intersection_graph.add_edges_from(intersection.edges)

# Write the intersection graph to a GML file
nx.write_gml(intersection_graph, "final.gml")
