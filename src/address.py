# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

class Address:
    __city = ""
    __street = ""
    __buildnum = ""

    def __init__(self, city, street, buildnum):
        self.__city = city
        self.__street = street
        self.__buildnum = buildnum

    @property
    def get_full_address(self):
        full_addr = f"из г. {self.__city} " \
                     f"ул. {self.__street}, " \
                     f"Дом {self.__buildnum} "
        return full_addr

    @property
    def get_city(self):
        return self.__city

    @property
    def get_street(self):
        return self.__street

    @property
    def get_build_num(self):
        return self.__buildnum


def main():
    pass


if __name__ == "__main__":
    main()
