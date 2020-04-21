import sys

class adjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    #Function to add an edge in undirected graph

    def add_edge(self, src, dest):

        #Adding node to source node

        node = adjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        #Adding  source node to desitination as
        #it is undirected graph

        node = adjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def isExplore(self, u,  visited):
        visited[u.vertex] = True
        tmp = self.graph[u.vertex]
        while tmp:
            if not visited[tmp.vertex]:
                self.isExplore(tmp, visited)
            tmp = tmp.next

    def explore(self, u, visited):
        return self.isExplore(u, visited)

    def DFS(self):
        visited = [False for v in self.graph]
        cc = 1
        for v in self.graph:
            if not v == None:
                if not visited[v.vertex]:
                    self.explore(v, visited)
                    cc += 1
        return cc


if __name__ == '__main__':
    v, e = map(int, input().split(" "))
    graph = Graph(v+1)
    for e in range(e):
        u, v = map(int, input().split(" "))
        graph.add_edge(u, v)
    print(graph.DFS())


