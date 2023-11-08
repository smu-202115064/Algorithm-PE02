import collections
import sys


def solve(n_vertices: int, graph: dict[int, list[int]]) -> str:
    # 각 노드의 부모를 기억하기 위한 공간 할당
    # 1번 노드부터 세기 위해 0번 노드로 None을 추가
    parents = [None] + [-1] * n_vertices
    visited = [None] + [False] * n_vertices

    def dfs(node: int):
        visited[node] = True
        for child in graph[node]:
            if not visited[child]:
                parents[child] = node
                dfs(child)

    # DFS 탐색을 통해 부모-자식 관계 확인
    dfs(1)
    return '\n'.join(map(str, parents[2:]))


if __name__ == "__main__":
    MAX_N = 100000
    sys.setrecursionlimit(MAX_N*2)
    # 표준 입력으로 들어온 데이터 가공
    N = int(sys.stdin.readline())
    graph = collections.defaultdict(list)
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    # 테스트 케이스 수행
    print(solve(N, graph))
