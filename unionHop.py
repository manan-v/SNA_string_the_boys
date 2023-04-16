import networkx as nx

G1 = nx.read_gml("G1Com.gml")
G2 = nx.read_gml("G2Com.gml")
G3=nx.read_gml("G3Com.gml")

# Load graph from GML file
# G = nx.read_gml('graph_file.gml')

# Create empty graph for the union of all ego graphs
union_graph_1 = nx.DiGraph()

# Loop over all nodes and compute union of 1-hop and 2-hop neighbors
print("GMLs read done")

for n in G1.nodes():
    # Get the set of predecessors and successors of the current node
    neighbors = set(G1.predecessors(n)) | set(G1.successors(n)) | {n}
    
    # Create an ego graph for the current node using the set of neighbors
    hop1 = G1.subgraph(neighbors)
    
    # Create the 2-hop ego graph by taking the union of the ego graphs of the neighbors
    hop2 = nx.DiGraph()
    for node in neighbors:
        ego = G1.subgraph(set(G1.predecessors(node)) | set(G1.successors(node)) | {node})
        hop2 = nx.compose(hop2,ego)
        
    # Take the union of the 1-hop and 2-hop ego graphs and add it to the union graph
    union = nx.compose(hop1,hop2)
    union_graph_1 = nx.compose(union_graph_1,union)

print("g1 done")

union_graph_2=nx.DiGraph()
for n in G2.nodes():
    # Get the set of predecessors and successors of the current node
    neighbors = set(G2.predecessors(n)) | set(G2.successors(n)) | {n}
    
    # Create an ego graph for the current node using the set of neighbors
    hop1 = G2.subgraph(neighbors)
    
    # Create the 2-hop ego graph by taking the union of the ego graphs of the neighbors
    hop2 = nx.DiGraph()
    for node in neighbors:
        ego = G2.subgraph(set(G2.predecessors(node)) | set(G2.successors(node)) | {node})
        hop2 = nx.compose(hop2,ego)
        
    # Take the union of the 1-hop and 2-hop ego graphs and add it to the union graph
    union = nx.compose(hop1,hop2)
    union_graph_2 = nx.compose(union_graph_2,union)
print("g2 done")

union_graph_3=nx.DiGraph()
for n in G3.nodes():
    # Get the set of predecessors and successors of the current node
    neighbors = set(G3.predecessors(n)) | set(G3.successors(n)) | {n}
    
    # Create an ego graph for the current node using the set of neighbors
    hop1 = G3.subgraph(neighbors)
    
    # Create the 2-hop ego graph by taking the union of the ego graphs of the neighbors
    hop2 = nx.DiGraph()
    for node in neighbors:
        ego = G3.subgraph(set(G3.predecessors(node)) | set(G3.successors(node)) | {node})
        hop2 = nx.compose(hop2,ego)
        
    # Take the union of the 1-hop and 2-hop ego graphs and add it to the union graph
    union = nx.compose(hop1,hop2)
    union_graph_3 = nx.compose(union_graph_3,union)
print("g3 done")



union_graph=nx.DiGraph()
print("making final shrinked graph")
union_graph=nx.compose_all(union_graph_1,union_graph_2,union_graph_3)
nx.write_gml(union_graph,"Hopped.gml")