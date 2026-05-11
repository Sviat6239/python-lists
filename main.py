'''
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
'''
'''
nums = [3, 7, 2, 8, 10, 13, 5]
odd_nums = []

for element in nums:
    if element % 2 == 0:
        added = odd_nums.append(element)

print(odd_nums)

nums = [3, 7, 2, 8, 10, 13, 5]
even_nums = []

for elemnt in nums:
    if elemnt % 2 == 1:
        added = even_nums.append(elemnt)
print(even_nums)        
'''

'''
# liked films
liked_films = ['film1', 'film2', 'film3', 'film4', 'film5']

print(liked_films[0])
print(liked_films[-1])
print(len(liked_films))
'''

'''
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(0, 5)
print(numbers)
'''

'''
owoca = ['owoc0', 'owoc1', 'owoc2', 'owoc3', 'owoc4']
owoca.pop()
owoca.remove('owoc1')
print(owoca)
'''

'''
miasta = ['Waszawa', 'Kraków', 'Gdynia', 'Gdansk', 'Wejherowo']
userMiasto = input('enter your city>>>')
for miasto in miasta:
    if miasto == userMiasto:
        print(miasta.index(userMiasto))
'''

'''
colors = ['red', 'green', 'blue']
colors.pop(1)
colors.insert(1, 'yellow')
colors.pop(2)
colors.insert(2, 'purple')
colors.append('grey')
print(colors)
'''

'''
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liczby[0:3])
print(liczby[-1])
'''

'''
names = ['Anna', 'Jan', 'Piotr', 'Maria']
for element in names:
    print(element, 'ma:', len(element), ' liter')
'''

'''
animals = ['cat', 'dog', 'horse', 'mous']
for element in animals:
    print(element, 'na pozycji', element.index(element))
'''    