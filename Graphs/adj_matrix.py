class Graph:
    def __init__(self,Vno):
        self.vertax_count=Vno
        self.adj_matrix=[[0]*Vno for e in range(Vno)]

    def add_edge(self,u,v,weight=1):
        if 0 <= u < self.vertax_count and 0 <= v < self.vertax_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid Vertax.")

    def remove_edge(self,u,v):
        if 0 <= u < self.vertax_count and 0 <= v < self.vertax_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid Vertax.")

    def has_edge(self,u,v):
        if 0 <= u < self.vertax_count and 0 <= v < self.vertax_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertax.")

    def printing(self):
        for row_list in self.adj_matrix:
            print("  ".join(map(str,row_list)))

g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.printing()