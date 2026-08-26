# def greet():
#     print("Hello! Welcome to our program.")

# greet()


"""function should be descriptive
separate function name with underscores
"""
# def check_weather():
#     temperature = 30
#     if temperature > 25:
#         print("It's a hot day")
#     else:
#         print("It's a cold day")


# check_weather()

# def greet(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")

# greet("Alice", "Smith")

# greet(first_name="Bob", last_name="Johnson" )

def sim_fun():
    numbers = [1, 2, 3, 4, 5]
    first = numbers[0]
    last = numbers[-1]
    return first, last

first_number, last_number = sim_fun()
print(f"First number: {first_number}, Last number: {last_number}")
