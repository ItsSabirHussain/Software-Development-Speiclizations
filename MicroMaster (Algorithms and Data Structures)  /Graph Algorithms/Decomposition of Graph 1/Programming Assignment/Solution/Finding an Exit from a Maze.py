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

    def isPathHelper(self, u, v,  visited):
        if u == v:
            return 1
        visited[u] = True
        tmp = self.graph[u]
        while tmp:
            if not visited[tmp.vertex]:
                return self.isPathHelper(tmp.vertex,v, visited)
            tmp = tmp.next
        return 0

    def isPath(self, u, v):
        return self.isPathHelper(u,v, [False for i in range(self.V)])



if __name__ == '__main__':
    V = set()
    arr = []
    n, m = map(int, input().split(" "))
    graph = Graph(n+1)
    for i in range(m):
        u, v = map(int, input().split(" "))
        graph.add_edge(u, v)

    src, dest = map(int, input().split(" "))

    print(graph.isPath(src, dest))

