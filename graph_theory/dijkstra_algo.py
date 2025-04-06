# create infinite cost assigned to each node at start
import sys

from pprint import pprint
from heapq import heapify, heappop, heappush


def dijkstra(graph, source, destination):
    inf = sys.maxsize
   
    node_data = {}
    for k in graph.keys():
        node_data[k] = {'cost': inf, 'predecessor': []} 

    node_data[source]['cost'] = 0
    pprint(node_data) 
    
    visited = []
    temp = source
    
    for i in range(len(graph)-1):
        if temp not in visited:
            visited.append(temp)
            # min_heap = [] # list of tuples(cost, node-name). E.G.: [(2, 'B'), (4, 'C')] 
            min_cost_neighbour = {'cost': inf, 'neighbour': None}
            
            for j in graph[temp].keys():
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['predecessor'] = node_data[temp]['predecessor'] + [temp]
                    
                    # solving this without heap or library (greedy algorithm)
                    if node_data[j]['cost'] < min_cost_neighbour['cost']:
                        min_cost_neighbour['cost'] = node_data[j]['cost']
                        min_cost_neighbour['neighbour'] = j
                    
                    # heappush(min_heap, (node_data[j]['cost'], j))
                    # print(min_heap)
                    print(min_cost_neighbour)
                    
        # heapify(min_heap)
        # temp = min_heap[0][1]   
        temp = min_cost_neighbour['neighbour']
        
    print("Shortest Distance from source to destination is: {}".format(node_data[destination]['cost']))
    print("Shortest Path from source to destination is: {}".format(node_data[destination]['predecessor']+[destination])) 
         
    return 0

    
if __name__ == "__main__":
    # all nodes with its neighbours and distance to reach the listed nodes from given node
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8},
        'C': {'A': 4, 'B': 3, 'D': 2, 'E': 5},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1},
    }
    
    source = 'A'
    destination = 'F'
    dijkstra(graph, source, destination)