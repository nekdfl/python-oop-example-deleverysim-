# Генератор объектов класса address
# пример паттерна фабрика не путать с абстрактной файбрикой

import random
from address import Address


class AddressMaker:

    def __init__(self, city: list, street: list, buildnumlen=2 ):
        pass
        self.__city_list = city
        self.__street_list = street
        self.__buildnumlen = buildnumlen

    @property
    def get_buildnum(self):
        buildnum = random.randrange(1, self.__buildnumlen)
        return buildnum

    @property
    def get_city(self):
        city_index = random.randrange(0, len(self.__city_list))
        return self.__city_list[city_index]

    @property
    def get_street(self):
        street_index = random.randrange(0, len(self.__street_list))
        return self.__street_list[street_index]

    def make_address(self):
        pass
        city = self.get_city
        street = self.get_street
        buildnum = self.get_buildnum

        address = Address(city, street, buildnum)
        return address
