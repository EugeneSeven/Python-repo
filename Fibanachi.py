def generate_fibonacci(length):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Example usage:
desired_length = 10
result = generate_fibonacci(desired_length)
print(result)
