def optimal_search_cost(k, f):
    n = len(k)
    c = [[0] * n for _ in range(n)]
    cost = [[0] * n for _ in range(n)]
    
    for i in range(n):
        c[i][i] = f[i]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            c[i][j] = sum(f[i:j+1])
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + c[i][j]
                if total_cost < cost[i][j]:
                    cost[i][j] = total_cost
    
    return cost[0][n - 1]

k = [5, 6]
f = [17, 25]

result = optimal_search_cost(k, f)
print(f"Нийт хайлтын хамгийн бага өртөг: {result}")
