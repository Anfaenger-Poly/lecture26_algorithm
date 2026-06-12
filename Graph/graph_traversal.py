from collections import deque

class Graph:
    def __init__(self):
        num_nodes, num_edges = map(int, input().split())
        self.directed = int(input('양방향 여부 (1: 양방향, 0: 단방향): '))
        self.graph = [[] for _ in range(num_nodes + 1)]
        for _ in range(num_edges):
            u, v = map(int, input().split())
            self.graph[u].append(v)
            if self.directed:
                self.graph[v].append(u)

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        print(node, end=' ')
        visited.add(node)
        for adj_node in self.graph[node]:
            if adj_node not in visited:
                self.dfs(adj_node, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        print(start, end=' ')  # 시작 노드에 대해 작업

        # 다음에 방문할 노드를 찾아서 처리
        # 방문했던 노드를 queue에서 가져와서 인접 노드 찾기
        while queue:
            node = queue.popleft()
            for node in self.graph[node]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
                    print(node, end=' ')

if __name__ == '__main__':
    g = Graph()
    start = int(input('시작 노드 번호: '))
    g.dfs(start)
    print()
    g.bfs(start)
    print()