

class Bank:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_details(self):
        print(f'name = {self.name} year = {self.year}')

    def get_brand(self):
        print('This is the central bank')

class Wema(Bank):

    def get_brand(self):
        print("Our brand logo is purple with over 5 million customer base")

class UBA(Bank):

    def get_brand(self):
        print("Our brand color is Red with over 10million customer base")

class Titan(Bank):
    def __init__(self,name, year,customer_base):
        super().__init__(name,year)
        self.customer_base = customer_base

    def get_details(self):
        print(f'name = {self.name} year = {self.year} total number of customers = {self.customer_base}')


w = Wema('wema',1986)
w.get_details()
w.get_brand()

u = UBA('UBA',1992)
u.get_details()
u.get_brand()

t = Titan('Titan',2010,4000000)
t.get_details()
t.get_brand()