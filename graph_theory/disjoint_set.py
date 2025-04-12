from typing import List

class DisjointSet:
    
    def __init__(self, vertices: List[str]) -> None:
        self.parent = {vertex:vertex for vertex in vertices}
        self.rank = {vertex:0 for vertex in vertices}
        
    def find(self, vertex: str) -> str:
        # PATH COMPRESSION STEP
        # So that in future we can find parent of vertex in O(1) instead of O(logk)
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex] 
    
    def union(self, root_x: str, root_y: str) -> None:
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            