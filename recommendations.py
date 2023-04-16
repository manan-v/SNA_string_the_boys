import networkx as nx
from apyori import apriori
import numpy as np
from scipy.sparse.linalg import svds
from sklearn.metrics.pairwise import cosine_similarity


node_id='0'

def get_recommendations_CN(node_id,graph):
    
    neighbors = set(graph.neighbors(node_id))
    common = set()
    for neighbor in neighbors:
        common |= set(graph.neighbors(neighbor))
    common = list(common - neighbors - set([node_id]))
    common_count = [(node, len(set(graph.neighbors(node)) & neighbors)) for node in common]
    common_count = sorted(common_count, key=lambda x: x[1], reverse=True)[:10]
    return [node for node, count in common_count]



def get_recommendations_Degree(node_id,graph):
    
    degree_centrality = nx.degree_centrality(graph)
    neighbors = list(graph.neighbors(node_id))
    
    
    neighbors_sorted = sorted(neighbors, key=lambda x: degree_centrality[x], reverse=True)
    
    
    print("Degree done for " + node_id)
    return neighbors_sorted[:10]



def get_recommendations_Diversity(node_id,graph):
    input_node = node_id

   
    jaccard_similarity = {}
    for node in graph.nodes():
        if node != input_node:
            input_successors = set(graph.successors(input_node))
            node_successors = set(graph.successors(node))
            deno=len(input_successors.union(node_successors))
            if deno==0:
                jaccard_similarity[node]=0
                continue
            jaccard_similarity[node] = len(input_successors.intersection(node_successors)) / len(input_successors.union(node_successors))

    
    average_distance = {}
    for node in graph.nodes():
        if node != input_node:
            try:
                average_distance[node] = nx.shortest_path_length(graph, source=input_node, target=node)
            except:
                average_distance[node] = 0

    
    diversity_score = {}
    for node in graph.nodes():
        if node != input_node:
            diversity_score[node] = (1 - jaccard_similarity[node]) * average_distance[node]

   
    sorted_nodes = sorted(diversity_score.items(), key=lambda x: x[1], reverse=False)

    
    top_n = 10
    print("diversity done for " + node_id)
    recommended_products_Diversity = [node[0] for node in sorted_nodes[:top_n]]
    return recommended_products_Diversity


def get_recommendations_EigenVectorCentrality(node_id,graph):

    input_node = node_id

    
    eigenvector_centrality = nx.eigenvector_centrality(graph)


    input_node_eigenvector_centrality = eigenvector_centrality.get(input_node, 0)

    
    recommended_products = [node for node, score in eigenvector_centrality.items() if score > input_node_eigenvector_centrality]

   
    print("eigen done for " + node_id)
    return recommended_products[:10]



# ground_truth = nx.read_edgelist('graph4.txt', create_using=nx.DiGraph())
def get_recommendations_Jaccard(node_id,graph):

    input_node = node_id

    
    jaccard_similarity = {}
    for node in graph.nodes():
        if node != input_node:
            deno=len(set(graph.successors(input_node)).union(set(graph.successors(node))))
            if deno==0:
                jaccard_similarity[node] =0
                continue
            jaccard_similarity[node] = len(set(graph.successors(input_node)).intersection(set(graph.successors(node)))) / deno

    
    sorted_nodes = sorted(jaccard_similarity.items(), key=lambda x: x[1], reverse=True)

    
    top_n = 10
    print("jaccard done for " + node_id)
    recommended_products_Jaccard = [node[0] for node in sorted_nodes[:top_n]]
    return recommended_products_Jaccard




def get_recommendations_PR(node_id,graph):
    page_rank = nx.pagerank(graph)
    
    neighbors = list(graph.neighbors(node_id))
    
    
    neighbors_sorted = sorted(neighbors, key=lambda x: page_rank[x], reverse=True)
    
    
    print("PR done for " + node_id)
    return neighbors_sorted[:10]


def predictedList(input_node,nodesList):
    ans=[]
    for i in nodesList:
        temp=[]
        temp.append((input_node,i))
        ans.append(temp)
    return ans
    
def actualList(input_node):
    graph = nx.read_gml("Predcited.gml")
    connected_nodes=list(graph.successors(input_node))
    return connected_nodes

def actual_list(node_id):
    G=nx.read_gml('Predcited.gml')
    neighbors = list(G.successors(node_id))
    return neighbors


def evaluate_recommendations(actual,predicted):
   
    #  precision
    if(len(predicted)==0 and len(actual)==0):
        f1_score=1
        return f1_score
    relevant_recommendations = set(predicted) & set(actual)
    
    if(len(predicted)==0):
        return 0
    precision = len(relevant_recommendations) / len(predicted)

    #  recall
    if(len(actual)==0):
        return 0
    recall = len(relevant_recommendations) / len(actual)

    # return (precision, recall)

    # precision, recall = evaluate_recommendations(actual, predicted)
    if(precision==0 and recall == 0):
        f1_score=0
    else:    
        f1_score = 2 * (precision * recall) / (precision + recall)

    return f1_score

def callAllFunc(node_id,graph):
    temp =[]
    temp1=get_recommendations_CN(node_id,graph)
    temp2=get_recommendations_Degree(node_id,graph)
    temp3=get_recommendations_Diversity(node_id,graph)
    temp4=get_recommendations_EigenVectorCentrality(node_id,graph)
    temp5=get_recommendations_Jaccard(node_id,graph)
    temp6=get_recommendations_PR(node_id,graph)
    temp.append(temp1)
    temp.append(temp2)
    temp.append(temp3)
    temp.append(temp4)
    temp.append(temp5)
    temp.append(temp6)

    return temp
# actual=actual_list(node_id)
# predicted=get_recommendations_CN(node_id);
# predicted=get_recommendations_Degree(node_id);




