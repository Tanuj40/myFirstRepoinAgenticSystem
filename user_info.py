user_name = input("Enter your name: ")

age_input = input("Enter your age: ")
user_age = int(age_input)
active_input = input("Are you an active user? (True/False): ")
user_active = active_input.lower() == "true"

print(f"User {user_name} is {user_age} years old. Active status: {user_active}")