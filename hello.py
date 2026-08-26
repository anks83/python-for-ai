person = {
    "name": "Ankit",
    "age": 25,
    "city": "New York"
}

person["age"] = 26

print(person)

if person["age"] > 25:
    print("You are older than 25.")
elif person["age"] == 25:
    print("You are 25 years old.")
else:
    print("You are younger than 25.")
