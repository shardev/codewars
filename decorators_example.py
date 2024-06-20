# Define the decorator function
def my_decorator(func):
    # Define the inner wrapper function
    def wrapper(*args, **kwargs):
        kwargs['name'] += ' [BEFORE]' 
        print(kwargs['name'])
        
        result = func(*args, **kwargs)  # Call the original function
        
        kwargs['name'] += ' [AFTER]' 
        print(kwargs['name'])
        return result
    # Return the inner wrapper function
    return wrapper

# Apply the decorator to a function using the @ syntax
@my_decorator
def greet(name):
    return f"Hello, {name}!"

# Call the decorated function
print(greet(name = "Alice"))
