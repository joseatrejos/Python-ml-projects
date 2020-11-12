from User import User
from User import Trejus

import matplotlib.pyplot as plt
import csv

print("hello world\n")

name = "Cesar\n"
print(name)

num = 1
print(num)

#variable2 = variable1 + num

if 1 < 2:
    print("It's less\n")
else:
    print("It's more\n")

vectorExample = ["Chompy", "Joel", "Ana", "Cesar"]

print(vectorExample)

print(vectorExample[0])

for p in vectorExample:
    p = "Persona: " + p + "\n"
    print(p)

# Las funciones no necesitan self como argumento
def showName():
    print('Jose')


user1 = User("Pancheiser", "23", "pancheiser@reina.com")
user2 = User("Chompy", "20", "chompy@gmail.com")
print(user2.age)

# Call the object's function sayHello
user2.sayHello()

showName()

trejus1 = Trejus("Chompylandia")

print(trejus1.something)
