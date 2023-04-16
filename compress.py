import networkx as nx

# G1=nx.read_gml("Amazon0302.gml", destringizer=int)
G2=nx.read_gml("Amazon0312.gml", destringizer=int)
G3=nx.read_gml("Amazon0505.gml", destringizer=int)
G4=nx.read_gml("Amazon0601.gml", destringizer=int)


print("gmls read")


# find nodes to remove
# G1.remove_nodes_from([node for node in G1.nodes() if node > 100000])
# # remove nodes from the graph
# # G1.remove_nodes_from(nodes_to_remove)

# nx.write_gml(G1,"G1Com.gml")
# print("G1 done")

G2.remove_nodes_from([node for node in G2.nodes() if node > 100000])
# remove nodes from the graph
# G1.remove_nodes_from(nodes_to_remove)

nx.write_gml(G2,"G2Com.gml")
print("G2 done")



G3.remove_nodes_from([node for node in G3.nodes() if node > 100000])
# remove nodes from the graph
# G1.remove_nodes_from(nodes_to_remove)

nx.write_gml(G3,"G3Com.gml")
print("G3 done")





G4.remove_nodes_from([node for node in G4.nodes() if node > 100000])
# remove nodes from the graph
# G1.remove_nodes_from(nodes_to_remove)

nx.write_gml(G4,"G4Com.gml")
print("G4 done")