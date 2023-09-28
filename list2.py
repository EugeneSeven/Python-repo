# Create an unnormalized list of mixed data
unnormalized_list = [9, "Yellow", 3, "$Bamboo", 25.4, 6, "Hello", 1, 2.3, 8, 2, "Car", 5,"4Hello", 7, 4]

# Sort the unnormalized list
def custom_sort(item):
    if isinstance(item, (int, float)):
        return (0, item)  # Sort integers first
    elif isinstance(item, str):
        return (2, item)  # Sort strings third
    else:
        return (3, item)  # Keep other types in their original order

sorted_list = sorted(unnormalized_list, key=custom_sort)

# Print the sorted list
print("Sorted List:", sorted_list)