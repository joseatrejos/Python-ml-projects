class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    # Los métodos necesitan recibir el argumento self obligatoriamente
    def sayHello(self):
        print(f'\nHola! \nMi nombre es: {self.name}\nMi edad es: {self.age}\nMi correo es:{self.email}\n')

class Trejus:
    def __init__(self, something):
        self.something = something
