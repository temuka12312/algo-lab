def fibonacci(n):
    cache = [0] * (n + 1)
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    
    return cache[n]

n = 10  
result = fibonacci(n)
print(f"F({n}) = {result}")
