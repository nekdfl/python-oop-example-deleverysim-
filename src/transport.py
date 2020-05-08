# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

from src.address import Address
from src.bill import Bill


class Transport:
    __status_dict = {0: "Свободен",
                1: 'Забираю посылку',
                2: 'Пью кофе на АЗС',
                3: 'Сломался',
                4: 'Встрял в пробку',
                5: 'Отдаю заказ'}

    def __init__(self, bill):
        self.__bill = bill
        self.__status = 0
        self.__name = ""
        self.__maxnumlength = 3

    def __gen_unique_name(self):
        pass
        return "Иницилизруй функцию в наследнике!"

    def __goto_src(self):
        pass

    def __goto_dest(self, serialnum):
        pass

    def __drink_coffe(self, serialnum):
        pass

    def __get_brake(self, serialnum):
        pass

    def do_trasport(self):
        self.__goto_src()
        self.__drink_coffe()
        self.__get_brake()
        self.__goto_dest()


class Taxi(Transport):
    __released_taxi = 0;

    # override
    def __gen_unique_name(self) -> str:
        pass
        name_prefix = "T"
        self.__released_taxi += 1
        snum = str(f"{self.__released_taxi:0>self.__maxnumlength}")
        unique_name = name_prefix + snum
        return unique_name

    def __init__(self, bill):
        super().__init__(bill)
        self.__name = self.__gen_unique_name()

    def __goto_src(self):
        pass
        self.__status = self.__status_dict[1]
        print(f"Борт {self.__name} меняет статус на {self.__status}")

    def __goto_dest(self, serialnum):
        pass

    def __drink_coffe(self, serialnum):
        pass

    def __get_brake(self, serialnum):
        pass


class Bike(Transport):
    __released_bike = 0;

    def __init__(self, bill):
        super().__init__(bill)
        self.__name = self.__gen_unique_name()

    # override
    def __gen_unique_name(self) -> str:
        pass
        name_prefix = "B"
        self.__released_taxi += 1
        snum = str(f"{self.__released_taxi:0>3}")
        unique_name = name_prefix + snum
        return unique_name


class Kamaz(Transport):
    __released_kamaz = 0;

    def __init__(self, bill):
        super().__init__(bill)
        self.__name = self.__gen_unique_name()

    # override
    def __gen_unique_name(self) -> str:
        pass
        name_prefix = "T"
        self.__released_taxi += 1
        snum = str(f"{self.__released_taxi:0>3}")
        unique_name = name_prefix + snum
        return unique_name


def main():
    pass


if __name__ == "__main__":
    main()
