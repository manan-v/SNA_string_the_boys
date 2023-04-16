import networkx as nx

G1=nx.read_gml("G1Com.gml")
G2=nx.read_gml("G2Com.gml")
G3=nx.read_gml("G3Com.gml")
G4=nx.read_gml("G4Com.gml")


u=nx.compose_all([G1,G2,G3])
print("union done")
G_resultant = nx.DiGraph()
G_resultant.add_nodes_from(G4.nodes)
G_resultant.add_edges_from(G4.edges - u.edges)

nx.write_gml(G_resultant,"Predcited.gml")
# print the nodes and edges of G_resultant
print("Nodes of G_resultant:", G_resultant.nodes)
print("Edges of G_resultant:", G_resultant.edges)