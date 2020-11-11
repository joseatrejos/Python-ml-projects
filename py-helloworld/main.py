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
    p = "Persona: " + p
    print(p)

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

        def sayHello():
            print(f'Hola! \nMi nombre es: {name}\nMi edad es: {age}\nMi correo es:{email}')
        
        super().__init__()

user1 = User("Pancheiser", "23", "pancheiser@reina.com")
print(user1.age)
print.sayHello('')