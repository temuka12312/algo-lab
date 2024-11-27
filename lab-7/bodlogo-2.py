class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0
    for item in items:
        if capacity == 0:
            break
        
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            total_value += item.value * (capacity / item.weight)
            capacity = 0

    return total_value

items = [
    Item(10, 60),
    Item(20, 100),
    Item(30, 120)
]

capacity = 50

max_value = fractional_knapsack(capacity, items)
print(f"Total value: {max_value}")
