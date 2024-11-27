def calculate_cost(n):
    total_cost = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:  
            total_cost += i
        else:
            total_cost += 1
    return total_cost

n = 10  
cost = calculate_cost(n)
print(f"The total cost for {n} operations is: {cost}")
