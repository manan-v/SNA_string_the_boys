import networkx as nx
import matplotlib.pyplot as plt

# load the GML file as a directed graph
G = nx.read_gml('G3Com.gml', destringizer=int)

# drop nodes with id > 100000
def remove_hops(G):
    nodes_to_remove = []
    for node in G.nodes:
        hops = nx.single_source_shortest_path_length(G, node)
        for h in hops.values():
            if h > 2:
                nodes_to_remove.append(node)
                break
    G.remove_nodes_from(nodes_to_remove)
    return G

G2=remove_hops(G)
nx.write_gml(G2,"G3Hopped.gml")