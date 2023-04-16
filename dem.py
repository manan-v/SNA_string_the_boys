from recommendations import *
import networkx as nx

graph=nx.read_gml("Predcited.gml")

nodelist=['86664', '75404', '88957', '55382', '32109', '7224', '54582', '78175', '83113', '95325']


for currNode in nodelist:
    currNode=nodelist[0]
    actual=actualList(currNode)
    print("Actual pridction: ",actual)
    print()
    print()

    predicted=get_recommendations_EigenVectorCentrality(currNode,graph)
    print(evaluate_recommendations(actual,predicted))
    print("Node predicted using eigen vector :",predicted)

    predicted=get_recommendations_Jaccard(currNode,graph)
    print("Node predicted using jaccard : ",predicted)

    predicted=get_recommendations_CN(currNode,graph)
    print("Node predicted using CN : ",predicted)

    predicted=get_recommendations_Degree(currNode,graph)
    print("Node predicted using degree : ",predicted)

    predicted=get_recommendations_Diversity(currNode,graph)
    print("Node predicted using diversity : ",predicted)

    predicted=get_recommendations_PR(currNode,graph)
    print("Node predicted using pr : ",predicted)