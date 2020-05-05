# Генератор объектов класса контакт
# пример паттерна фабрика не путать с абстрактной файбрикой

import random
from contact import Contact


class ContactMaker:

    def __init__(self, firstname: list, secondname: list, thirdname: list, phone_length=6):
        pass
        self.__firstname_list = firstname
        self.__secondname_list = secondname
        self.__thirdname_list = thirdname
        self.__phone_digit_count = phone_length

    @property
    def get_phone(self):
        need_append = int(self.__phone_digit_count) - 1
        append_text = "0" * need_append
        firstdigit_text = "1"

        startrange = int(firstdigit_text + append_text)  # 100000
        endrange = int("1" * self.__phone_digit_count) * 9  # 999999
        phone = random.randrange(startrange, endrange)
        return phone

    @property
    def get_firstname(self):
        firstname_index = random.randrange(0, len(self.__firstname_list))
        return self.__firstname_list[firstname_index]

    @property
    def get_secondname(self):
        secondname_index = random.randrange(0, len(self.__secondname_list))
        return self.__secondname_list[secondname_index]

    @property
    def get_thirdname(self):
        thirdname_index = random.randrange(0, len(self.__thirdname_list))
        return self.__thirdname_list[thirdname_index]

    def make_contact(self):
        pass
        firstname = self.get_firstname
        secondname = self.get_secondname
        thirdname = self.get_thirdname
        phone = self.get_phone

        # print(
        #     f"hello {firstname} {secondname} {thirdname}, call to: {phone}")
        contact = Contact(firstname, secondname, thirdname, phone)
        return contact


######## BAD PROGRAM STYLE EXAMPLE
# @property
# def __phone(self):
#     phone = random.randrange(100000, 999999)
#     return phone
#
# def make_contact(self):
#     pass
#     firstname_index = random.randrange(o, len(self.__firstname_list))
#     secondname_index = random.randrange(0, len(self.__secondname_list))
#     thirdname_index = random.randrange(0, len(self.__thirdname_list))
#     phone = self.__phone
#
#     print(
#         f"hello {self.__firstname_list[firstname_index]} "
#         f"{self.__secondname_list[secondname_index]} "
#         f"{self.__thirdname_list[thirdname_index]} "
#         f"call to: {phone}")
#
#     contact = Contact(self.__firstname_list[firstname_index], self.__secondname_list[secondname_index],
#                       self.__thirdname_list[thirdname_index], phone)
#
#     return contact


def main():
    print(
        "Тестируем, просто чтобы убедиться в получении ожидаемых резульатов. "
        "Это не юнит тест, а просто пример работы")

    contactmakerdata_firstname = ["Смирнов", "Иванов", "Кузнецов", "Попов", "Лебедев", "Козлов", "Новиков",
                                  "Морозов",
                                  "Петров", "Волков", "Соловьёв", "Васильев", "Зайцев", "Павлов", "Семёнов",
                                  "Голубев", "Виноградов", "Богданов",
                                  "Воробьёв", "Фёдоров", "Михайлов", "Беляев"]

    contactmakerdata_secondname = ["Бажен", "Бенедикт", "Богдан", "Боеслав", "Болеслав", "Боримир", "Борис",
                                   "Борислав",
                                   "Боян", "Бронислав", "Будимир", "Булат"]

    contactmakerdata_thirdname = ["Александрович", "Алексеевич", "Анатольевич", "Андреевич", "Антонович",
                                  "Аркадьевич",
                                  "Арсеньевич", "Артемович", "Афанасьевич"]

    phone_length = 6

    make_list_size = 5

    contactmaker = ContactMaker(contactmakerdata_firstname, contactmakerdata_secondname, contactmakerdata_thirdname,
                                phone_length)

    print("Contact maker example")

    for i in range(make_list_size):
        contact = contactmaker.make_contact()
        print(f"{i + 1}. К Вам заходил {contact.get_firstname} {contact.get_secondname} {contact.get_thirdname},"
              f" просил позвонить по номеру {contact.get_phone_num:>6}")


if __name__ == "__main__":
    main()
