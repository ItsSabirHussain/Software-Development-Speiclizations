import sys

class adjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        if self.graph[src]:
            self.graph[src].next = adjNode(dest)
        else:
            self.graph[src] = adjNode(src)
            self.graph[src].next = adjNode(dest)

    def isExplore(self, u,  visited, pre, post, clock):
        visited[u.vertex] = True
        pre[u.vertex] = clock
        clock += 1
        tmp = self.graph[u.vertex]
        while tmp:
            if not visited[tmp.vertex]:
                self.isExplore(tmp, visited, pre, post, clock)
            tmp = tmp.next
        post[u.vertex] = clock
        clock += 1

    def explore(self, u, visited):
        pre = [None for i in range(self.V + 1)]
        post = [None for i in range(self.V + 1)]
        return self.isExplore(u, visited, pre, post, 1)

    def DFS(self):
        visited = [False for v in self.graph]
        for v in self.graph:
            if not v == None:
                if not visited[v.vertex]:
                    self.explore(v, visited)
                else:
                    return 1
        return 0


if __name__ == '__main__':
    v, e = map(int, input().split(" "))
    graph = Graph(v+1)
    for e in range(e):
        u, v = map(int, input().split(" "))
        graph.add_edge(u, v)
    print(graph.DFS())


