# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


class Contact:
    __first_name = ""
    __second_name = ""
    __third_name = ""
    __phone_num = ""

    def __init__(self, first, second, third, phone_num):
        self.__first_name = first
        self.__second_name = second
        self.__third_name = third
        self.__phone_num = phone_num

    @property
    def get_firstname(self):
        return self.__first_name

    @property
    def get_secondname(self):
        return self.__second_name

    @property
    def get_thirdname(self):
        return self.__third_name

    @property
    def get_phone_num(self):
        return self.__phone_num


def main():
    pass


if __name__ == "__main__":
    main()
