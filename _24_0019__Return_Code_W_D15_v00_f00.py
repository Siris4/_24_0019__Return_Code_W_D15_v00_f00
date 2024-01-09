def my_add_function(n1, n2):
	total = n1 + n2
	return total

my_add_function(4,5)


##########################

def outer_function():
	# Outer function code

    def inner_function():
        # Inner function code

    # More outer function code

    	return inner_function

##########################

def greet(name):
    def get_message():
        return "Hello, "

    result = get_message() + name
    return result

print(greet("Alice"))  # Output: Hello, Alice

###########################

def outer_function():
    def inner_function():
        return "Hello from inner function!"

    return inner_function

my_func = outer_function()
result = my_func()
print(result)


###########################

order_ingredients = ["pepper", "salt", "milkshake"]
resources = {"pepper": 5, "salt": 10, "milkshake": 2}

def is_resource_sufficient(order_ingredients):
    # Returns True when order can be made or False if the ingredients are insufficient.
    for item in order_ingredients:
        if item not in resources or resources[item] < 1:  # Check if item is available and quantity is sufficient
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
