
def duplicate_elimination(value):
    return (sorted(set(value)))
    
colours = ["red", "green", "yellow", "red", "yellow", "white", "blue"]
numbers = [3, 4, 5, 8, 4, 9, 10]

print(duplicate_elimination(colours))
print(duplicate_elimination(numbers))


