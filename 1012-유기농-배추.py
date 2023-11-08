import sys


def solve(width: int, height: int, cabbages: list[tuple[int, int]]) -> int:
    visitable = [[ False ] * width for _ in range(height)]

    def is_visitable(x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < width and y < height and visitable[y][x]

    def dfs(x: int, y: int):
        if is_visitable(x, y):
            visitable[y][x] = False
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

    # 배추가 심어진 곳은 방문 가능한 곳으로 표시
    for x, y in cabbages:
        visitable[y][x] = True

    # DFS로 방문 가능한 곳들로 이루어진 연결 성분들을 소거해나감.
    sys.setrecursionlimit(width * height * 2)

    connected_components = 0
    for x, y in cabbages:
        if is_visitable(x, y):
            connected_components += 1
            dfs(x, y)

    # 연결 성분의 개수가 문제의 정답에 해당함.
    return connected_components


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        # 표준 입력으로 들어온 데이터 가공
        M, N, K = map(int, sys.stdin.readline().split())
        items = []
        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            items.append((X, Y))
        # 테스트 케이스 수행
        print(solve(M, N, items))