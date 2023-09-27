import random

# Function to generate a random list of integers
def generate_random_list(length, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(length)]

# Function to perform Selection Sort
def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr

# Generate a random list of integers
my_list = generate_random_list(10, 1, 100)

# Print the unsorted list
print("Unsorted list:", my_list)

# Sort the list using Selection Sort
selection_sort(my_list)

# Print the sorted list
print("Sorted list:", my_list)