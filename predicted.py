import networkx as nx

# Read the two directed graphs from GML files
G4 = nx.read_gml("Amazon0601.gml")
union = nx.read_gml('3Union.gml')

G_diff = nx.difference(G4, union)


print("Nodes in difference graph:", list(G_diff.nodes()))
print("Edges in difference graph:", list(G_diff.edges()))

# Writing the difference graph to a GML file
nx.write_gml(G_diff, "g4_union.gml")
