class Graph:
    def __init__(self,vno):
        self.vertax_count=vno
        self.adj_list={v:[] for v in range(vno)}

    def add_edge(self,u,v,weight=1):
        if 0<= u <self.vertax_count and 0<= v <self.vertax_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("Invalid inputs!")

    def remove_edge(self,u,v):
        if 0<= u <self.vertax_count and 0<= v <self.vertax_count:
            self.adj_list[u]=[(vertax,weight) for vertax,weight in self.adj_list[u] if vertax != v]
            self.adj_list[v]=[(vertax,weight) for vertax,weight in self.adj_list[v] if vertax != u]
        else:
            print("Invalid inputs!")
    
    def has_edge(self,u,v):
        if 0<= u <self.vertax_count and 0<= v <self.vertax_count:
            return any(vertax == v for vertax,x in self.adj_list[u])
        else:
            print("Invalid inputs!")
            return False

    def printing(self):
        for vertax,neighbor in self.adj_list.items():
            print("V",vertax,":",neighbor)


g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(1,4)
g.printing()
g.remove_edge(1,4)
print("\n")
print("After Removing the Edge.\n")
g.has_edge(1,4)
g.printing()