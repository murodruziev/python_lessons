class Building:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def set_data(self):
        print('Year:', self.year, 'City:', self.city)

class School(Building):
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def set_data(self):
       super().set_data()
       print('Pupils:', self.pupils)



class Shop(Building):
    pass

class House(Building):
    pass


school_36 = School(450, 1998, 'Bukhara')
school_36.year = 5
school_36.set_data()
shop = Building(2012, 'Bukhara')
house = Building(2019, 'Bukhara')
house.set_data()