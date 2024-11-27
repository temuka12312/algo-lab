def potential_function(D0, Di):
    if D0 != 0 and Di >= D0:
        return True
    return False

D0 = 0  
Di = 10  
result = potential_function(D0, Di)
print(f"Potential function holds: {result}")
