# Program: 15
# Description: This program takes an integer input from the user,
# finds all numbers that divide it evenly, and stores them in a list.

# Get input from the user
n = int(input("Add number:\n"))

# Initialize an empty list to store divisors
divisors = []

# Loop through all numbers from 1 to n
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)  # Add divisor to the list

# Print the list of divisors
print("Divisors:", divisors)
