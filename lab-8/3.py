def assign_bicycles(students, bicycles):
    result = []
    assigned_bikes = set()

    for student in students:
        closest_bike = -1
        min_distance = float('inf')
        
        for i, bike in enumerate(bicycles):
            if i not in assigned_bikes:
                distance = abs(student[0] - bike[0]) + abs(student[1] - bike[1])
                if distance < min_distance:
                    min_distance = distance
                    closest_bike = i
        
        result.append(closest_bike)
        assigned_bikes.add(closest_bike)
    
    return result

students = [(0, 0), (1, 1)]
bicycles = [(0, 1), (4, 3), (2, 1)]

result = assign_bicycles(students, bicycles)
print(f"Assign: {result}")
