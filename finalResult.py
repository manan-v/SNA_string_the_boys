import networkx as nx
from recommendations import *

G=nx.read_gml("intersection_graph.gml")
Hop=nx.read_gml("final.gml")
nodeList=[]
count =0
for node in G.nodes:
    if count == 10:
        break
    if Hop.has_node(node):
        nodeList.append(node)
        count+=1

print(nodeList)

rec=[]
count =0
for i in nodeList:
    print(i)
    rec.append(callAllFunc(i,Hop))
    print(rec[count])
    count+=1

print(rec)
    
