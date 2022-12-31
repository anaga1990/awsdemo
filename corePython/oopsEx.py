class Car(object):
    def __init__(self):
        print("car object creation done")

    def model_of_year(self, year_of_the_year='2022'):
        print('Year of the car model is ' + year_of_the_year)

    def car_company(self, car_company_name):
        print('car company name ' + car_company_name)


class Tata(Car):
    def __init__(self):
        Car.__init__(self)
        print('tata car object Created')

    def model_of_year(self, year_of_the_year):
        return year_of_the_year

    def car_model_name(self, model_name):
        print(model_name)


t = Tata()
t.model_of_year('2020')
t.car_model_name("NEXON")
t.car_company('tata')
