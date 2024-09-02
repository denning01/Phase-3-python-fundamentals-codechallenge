#function that adds 2 numbers

#defines 2 empty variables that will store the numbers
num1 = ()
num2 =()

#delares a function
def add_numbers(num1, num2):
    #asks the user to enter the number that he/she wants
    num1= input("Enter the first number: ")
    num2= input("Enter the second number: ")
    #converts the number to a float so as to accept numbers with decimal points
    num1= float(num1) 
    num2 = float(num2) 
    result = (num1 +num2)
    print(result)
#calls the function
add_numbers(num1,num2)
    
    