import sys

class adjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        self.pre = {i: -1 for i in range(self.V + 1)}
        self.post = {i: -1 for i in range(self.V + 1)}
    def add_edge(self, src, dest):
        node = adjNode(dest)
        if self.graph[src]:
            self.graph[src].next = node
        else:
            self.graph[src] = adjNode(src)
            self.graph[src].next = node

        if not self.graph[dest]:
            self.graph[dest] = node


    def isExplore(self, u,  visited, clock):
        visited[u.vertex] = True
        self.pre[u.vertex] = clock
        clock += 1
        tmp = self.graph[u.vertex]
        while tmp:
            if not visited[tmp.vertex]:
                self.isExplore(tmp, visited, clock)
            tmp = tmp.next
        self.post[u.vertex] = clock
        clock += 1

    def explore(self, u, visited):
        self.isExplore(u, visited, 0)

    def DFS(self):
        visited = [False for v in self.graph]
        for v in self.graph:
            if not v == None:
                if not visited[v.vertex]:
                    self.explore(v, visited)


    def topologicalSort(self):
        self.DFS()
        res = []
        tmp = (sorted(self.post.items(), key=lambda kv: kv[1]))
        for i in range(len(tmp)):
            res.append(tmp[i][0])
        return res


if __name__ == '__main__':
    v, e = map(int, input().split(" "))
    graph = Graph(v+1)
    for e in range(e):
        u, v = map(int, input().split(" "))
        graph.add_edge(u, v)
    print(graph.topologicalSort())


