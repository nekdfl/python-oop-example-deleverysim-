import time

from billmaker import BillMaker
from contactmaker import ContactMaker
from addressmaker import AddressMaker


class DeleverySim:

    def __init_user_params(self):
        self.__min_bill_count = 10
        self.__max_bill_count = 1000
        self.__taxi_count = 300
        self.__bike_count = 200
        self.__kamaz_count = 100

    def __init_contact_maker_data(self):
        self.__contactmakerdata_firstname = ["Смирнов", "Иванов", "Кузнецов", "Попов", "Лебедев", "Козлов", "Новиков",
                                             "Морозов", "Петров", "Волков", "Соловьёв", "Васильев", "Зайцев", "Павлов",
                                             "Семёнов", "Голубев", "Виноградов", "Богданов",
                                             "Воробьёв", "Фёдоров", "Михайлов", "Беляев"]

        self.__contactmakerdata_secondname = ["Бажен", "Бенедикт", "Богдан", "Боеслав", "Болеслав", "Боримир", "Борис",
                                              "Борислав", "Боян", "Бронислав", "Будимир", "Булат"]

        self.__contactmakerdata_thirdname = ["Александрович", "Алексеевич", "Анатольевич", "Андреевич", "Антонович",
                                             "Аркадьевич", "Арсеньевич", "Артемович", "Афанасьевич"]

        self.__phone_length = 6

    def __init_address_maker_data(self):
        pass
        self.__address_maker_data_city = [
            "Арзгир", "Артезианский", "Архангельское", "Архиповское", "Ачикулак", "Базовый", "Баклановская",
            "Балахоновское", "Балковский", "Балтийский", "Барсуковская"]

        self.__address_maker_data_street = ["Далекий", "Далибанда", "Далидовича", "Далинина", "Далматовская",
                                            "Далматская",
                                            "Дальзаводская", "Дальная", "Дальневосточная",
                                            "Дальневосточная(Михайловка)",
                                            "Дальневосточная 1 - я", "Дальневосточная 2 - я", "Дальневосточная 3 - я",
                                            "Дальневосточная 4 - я", "Дальневосточная 5 - я", "Дальневосточный",
                                            "Дальнегорная", "Дальнегорская", "Дальнее", "Дальнее поле",
                                            "Дальне - Кабанная", "Дальне - Ключевская"]

        self.__address_maker_data_buildnumlen = 2

    def __init_objects(self):
        self.__contactmaker = ContactMaker(self.__contactmakerdata_firstname, self.__contactmakerdata_secondname,
                                           self.__contactmakerdata_thirdname, self.__phone_length)

        self.__addressmaker = AddressMaker(self.__address_maker_data_city,
                                           self.__address_maker_data_street,
                                           self.__address_maker_data_buildnumlen)

        self.__billmaker = BillMaker(self.__min_bill_count,
                                     self.__max_bill_count,
                                     self.__contactmaker,
                                     self.__addressmaker)

    def __init__(self):
        self.__init_user_params()
        self.__init_contact_maker_data()
        self.__init_address_maker_data()
        self.__init_objects()

    def user_input(self):
        self.__min_bill_count = input("Мин число заказов: ")
        self.__max_bill_count = input("Макс число заказов: ")
        self.__taxi_count = input("Число такси: ")
        self.__bike_count = input("Числов велокурьеров: ")
        self.__kamaz_count = input("Число грузовых: ")

    def __print_bills(self, bills):

        for bill in bills:
            bill.print_bill(bill)
            print("=" * 40)

    def do_djob(self):
        pass
        time.sleep(0.1)
        bill_list = self.__billmaker.gen_bill_list()
        self.__print_bills(bill_list)

        # self.__contactmaker.make_contact()


def main():
    dsim = DeleverySim()
    dsim.do_djob()


if __name__ == "__main__":
    main()
