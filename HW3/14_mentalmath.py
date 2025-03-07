numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

# Create a list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Bonus: Create a list of odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
