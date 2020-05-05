# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

class Bill:

    def __init__(self, serialnum, src_addr, dst_addr, from_contact, to_contact, is_fragile, weight, size):
        self.__serialnum = serialnum
        self.__src_addr = src_addr
        self.__dst_addr = dst_addr
        self.__from_contact = from_contact
        self.__to_contact = to_contact
        self.__is_fragile = is_fragile
        self.__weight = weight
        self.__size = size

    @property
    def get_serialnum(self):
        return self.__serialnum

    @property
    def get_src_address(self):
        return self.__src_addr

    @property
    def get_dest_address(self):
        return self.__dst_addr

    @property
    def get_from_contact(self):
        return self.__from_contact

    @property
    def get_to_contact(self):
        return self.__to_contact

    @property
    def is_fragile(self):
        return self.__is_fragile

    @property
    def get_weight(self):
        return self.__weight

    @property
    def get_size(self):
        return self.__size

    def print_bill(self, mybill):
        short_from_c = f"{mybill.get_from_contact.get_firstname}" \
                       f" {mybill.get_from_contact.get_secondname.upper()[:1]}." \
                       f"{mybill.get_from_contact.get_thirdname.upper()[:1]}. "

        short_from_a = f"из г. {mybill.get_src_address.get_city} " \
                       f"ул. {mybill.get_src_address.get_street} ," \
                       f"Дом {mybill.get_src_address.get_build_num} "

        short_to_c = f"{mybill.get_to_contact.get_firstname} " \
                     f"{mybill.get_to_contact.get_secondname.upper():.1}." \
                     f"{mybill.get_to_contact.get_thirdname.upper():.1}. "

        short_to_a = f"из г. {mybill.get_dest_address.get_city} " \
                     f"ул. {mybill.get_dest_address.get_street} ," \
                     f"Дом {mybill.get_dest_address.get_build_num} "

        print(f"Заказ на посылку № {mybill.get_serialnum}\n"
              f"От {short_from_c}"
              f"{short_from_a}"
              f"т. {mybill.get_from_contact.get_phone_num},\n"
              f"Кому {short_to_c}"
              f"{short_to_a}"
              f"т. {mybill.get_to_contact.get_phone_num},\n"
              f"Хрупкое {mybill.is_fragile}, Масса кг: {mybill.get_weight:.2}, size {mybill.get_size:.2} m^3")


def main():
    pass
    from src.addressmaker import AddressMaker
    from src.contactmaker import ContactMaker
    amker = AddressMaker(["Москва", "Ростов"], ["Ленина", "Мира"], 99)
    src_addr = amker.make_address()
    dst_addr = amker.make_address()
    cmker = ContactMaker(["Иванов", "Сидоров"], ["Иван", "Петр"], ["Семенович", "Витальевич"])
    from_cont = cmker.make_contact()
    to_cont = cmker.make_contact()
    bill_range = range(10, 22)

    for snum in bill_range:
        mybill = Bill(snum, src_addr, dst_addr, from_cont, to_cont, True, 0.02, 0.22)
        mybill.print_bill(mybill)


if __name__ == "__main__":
    main()
