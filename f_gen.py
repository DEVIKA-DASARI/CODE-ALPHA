def fibonacci_generator(num_terms):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Generate Fibonacci sequence up to num_terms terms
    for _ in range(num_terms):
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update Fibonacci numbers: next = current + previous


# Get input for the number of Fibonacci numbers to generate
try:
    num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))
    if num_terms <= 0:
        raise ValueError("Number of terms must be a positive integer.")
except ValueError as e:
    print(f"Error: {e}")
else:
    # Create a Fibonacci generator object
    fib_gen = fibonacci_generator(num_terms)

    # Generate and print the Fibonacci sequence
    print(f"Fibonacci sequence with {num_terms} terms:")
    for fib_number in fib_gen:
        print(fib_number)
