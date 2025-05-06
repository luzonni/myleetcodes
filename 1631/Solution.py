import heapq

def minimumEffortPath(heights):
    rows, cols = len(heights), len(heights[0])
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    heap = [(0, 0, 0)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        effort, x, y = heapq.heappop(heap)
        if (x, y) == (rows - 1, cols - 1):
            return effort
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                if new_effort < efforts[nx][ny]:
                    efforts[nx][ny] = new_effort
                    heapq.heappush(heap, (new_effort, nx, ny))

# Exemplo de uso:
heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]

print(minimumEffortPath(heights))  # Saída esperada: 2
