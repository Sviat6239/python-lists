shopping_list = []

shopping_list.append("product1")
shopping_list.append("product2")
shopping_list.append("product3")

shopping_list.extend("anotherproduct1")
shopping_list.extend("anotherproduct2")
shopping_list.extend("anotherproduct3")

print(shopping_list)

user_nums = []

num = int(input("Enter your number #1: "))
user_nums.append(num)
num2 = int(input("Enter your number #2: "))
user_nums.append(num2)
num3 = int(input("Enter your number #3: "))
user_nums.append(num3)
num4 = int(input("Enter your number #4: "))
user_nums.append(num4)
num5 = int(input("Enter your number #5: "))
user_nums.append(num5)

print(user_nums)

print("max user num is: ", max(user_nums))
print("min user num is: ", min(user_nums))

events = ["first event", "second event", "third event"]

events.reverse()
print(events)
events.reverse()
print(events)


day_todos = ["one", "two", "three", "four", "five"]

print(day_todos)

day_todos.insert(1, "six")
print(day_todos)

day_todos.insert(-1, "seven")
print(day_todos)

users = ["user", "admin", "guest"]

print(users)

name = input("enter your name:\n>>>")
users.append(name)

