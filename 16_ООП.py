# Создание класса и объекта
class Dog:
    name = None
    age = None
    isHappy = None

dog1 = Dog()
dog1.name = 'Принц'
dog1.age = 17
dog1.isHappy = False


dog2 = Dog()
dog2.name = 'Графинья'
dog2.age = 13
dog2.isHappy = True

print(dog1.name)
print(dog2.isHappy)

#Зд_2 Работа с методами
class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name=None, age=None, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

        self.set_data(name, age, isHappy)
        self.get_data()


    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, 'age:', self.age, '. Happy', self.isHappy)

cat1 = Cat('Барсик', 3, True)

cat2 = Cat('Жопен', 2, False)

