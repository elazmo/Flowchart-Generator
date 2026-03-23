weight = {"pencil": 10, "pen": 20, "paper": 4, "eraser": 80}
available = {"pen": 3, "pencil": 5, "eraser": 2, "paper": 10}

overall_weight = 0

for item, count in available.items():
    overall_weight += weight[item] * count

print("Overall weight:", overall_weight)
