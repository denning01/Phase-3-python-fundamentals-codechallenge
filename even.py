#checks if number is even
number=()
def is_even(number):
    number =int(input("enter a number of your choice: "))


    result = (number % 2)
    if result == 0:
        print("True")
    else:
        print("False")
    
    
is_even(number)