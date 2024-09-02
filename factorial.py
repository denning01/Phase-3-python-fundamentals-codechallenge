def calculate_factorial(n):
    # Check if n is a non-negative integer
    if n < 0:
        return "Invalid input! Please enter a non-negative integer."
    # Base case: the factorial of 0 is 1
    if n == 0:
        return 1
    
    # Initialize the result to 1
    result = 1
    
    # Calculate the factorial using a loop
    for i in range(1, n + 1):
        result *= i
    
    return result

# Allow user input
try:
    user_input = int(input("Enter a non-negative integer to calculate its factorial: "))
    print(f"The factorial of {user_input} is: {calculate_factorial(user_input)}")
except ValueError:
    print("Invalid input! Please enter a valid non-negative integer.")
