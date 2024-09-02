def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    # Apply the decorator to the input function
    return decorator_func(func)


def sample_function():
    print("Original function is called.")

# Apply the decorator to the sample function
decorated_function = apply_decorator(sample_function)

# Call the decorated function
decorated_function()
