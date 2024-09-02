class Car:


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Print out the car's information
        print(f"Car Information: {self.year} {self.model} {self.make} ")

# Example usage
car1 = Car("Toyota,", "LC 200,", 2023)
car1.display_info()  
