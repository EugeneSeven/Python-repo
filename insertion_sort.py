import random

# Function to generate a random list of integers
def generate_random_list(length, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(length)]

# Function to perform Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a random list of integers
my_list = generate_random_list(10, 1, 100)

# Print the unsorted list
print("Unsorted list:", my_list)

# Sort the list using Insertion Sort
insertion_sort(my_list)

# Print the sorted list
print("Sorted list:", my_list)
