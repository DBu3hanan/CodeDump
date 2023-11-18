import random

"""
This Python code generates a sequence with 4 random numbers at the front
followed by 2 random letters (in uppercase) at the back.
"""

# Function to generate a random sequence
def generate_sequence():
    # Generate 4 random numbers
    numbers = [random.randint(0, 9) for _ in range(4)]

    # Generate 2 random letters in uppercase
    letters = [chr(random.randint(65, 90)) for _ in range(2)]

    # Combine the numbers and letters to form the sequence
    sequence = numbers + letters

    return sequence

# Generate and print the sequence without spaces between characters
result_sequence = generate_sequence()
print("Generated Sequence:", ''.join(map(str, result_sequence)))
