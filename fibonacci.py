# Set the number of Fibonacci numbers to generate
n = 10
# Initialize the first two numbers in the sequence
a, b = 0, 1
# Print the first two numbers
print(a, b, end=" ")
# Generate the remaining Fibonacci numbers
for _ in range(2, n):
    next_number = a + b
    print(next_number, end=" ")
    # Update the values for the next iteration
    a, b = b, next_number