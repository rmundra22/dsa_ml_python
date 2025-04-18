class Graph:
    """
    A graph is a pictorial representation of a set of objects where 
    some pairs of objects are connected by links. The interconnected 
    objects are represented by points termed as vertices, and the 
    links that connect the vertices are called edges.
    """
    def __init__(self, graph_as_dict = {}):
        self.graph = graph_as_dict
    
    def display_vertices(self):
        return list(self.graph.keys())
    
    def display_edges(self):
        edges = []
        for key, value in self.graph.items():
            for neighbour in value:
                new_edge = str(key + neighbour)
                if new_edge not in edges:
                    edges += [new_edge]
        return edges
    
    def add_vertices(self, vertices_with_neighbours):
        for vertex, neighbours in vertices_with_neighbours.items():
            self.graph[vertex] = neighbours
            for node in neighbours:
                self.graph[node].append(vertex)
    

def create_graph(graph_as_dict):
    graph = Graph(graph_as_dict)
    return graph

if __name__ == "__main__":
    # Create the dictionary with graph elements
    graph_as_dict = { 
        "a" : ["b", "c", "c"],
        "b" : ["a", "d"],
        "c" : ["a", "d"],
        "d" : ["e"],
        "e" : ["d"]
    }
    
    graph = create_graph(graph_as_dict)
    # Print the graph 		 
    print(graph.graph)
    print(graph.display_vertices())
    print(graph.display_edges())
    
    additional_nodes = {
        "f": ["a", "c"],
        "g": ["f"]
    }
    graph.add_vertices(additional_nodes)
    print(graph.graph)