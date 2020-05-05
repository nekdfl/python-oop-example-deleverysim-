# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import random
from bill import Bill
from addressmaker import AddressMaker
from contactmaker import ContactMaker


class BillMaker:
    __releasedbill_count = 1  # !STATIC CLASS MEMBER !!!

    def __init__(self, min: int, max: int, contactmaker, addressmaker):
        pass
        self.__mingenbill = min
        self.__maxgenbill = max
        self.__contactmaker = contactmaker
        self.__addressmaker = addressmaker

    def __get_gencount(self):
        count = random.randrange(self.__mingenbill, self.__maxgenbill)
        return count

    def __gen_size(self):
        size = random.uniform(0.01, 1)
        return size

    def __gen_weight(self, size):
        density_k = random.uniform(0.01, 1.01)
        weight = size * density_k
        return weight

    def __gen_fragile(self):
        fragile = bool(random.uniform(0.01, 1.00))
        return fragile

    def gen_bill_list(self):
        count = range(1, self.__get_gencount())
        bill_list = []
        for i in count:
            src_addr = self.__addressmaker.make_address()
            src_cont = self.__contactmaker.make_contact()
            dst_addr = self.__addressmaker.make_address()
            dst_cont = self.__contactmaker.make_contact()
            is_fragile = self.__gen_fragile()
            size = self.__gen_size()
            weight = self.__gen_weight(size)
            newbill = Bill(self.__releasedbill_count, src_addr, dst_addr, src_cont, dst_cont, is_fragile, weight, size)
            bill_list.append(newbill)
            self.__releasedbill_count += 1

        return bill_list


########################
def main():
    pass
    amker = AddressMaker(["Москва", "Ростов"], ["Ленина", "Мира"], 99)
    cmker = ContactMaker(["Иванов", "Сидоров"], ["Иван", "Петр"], ["Семенович", "Витальевич"])
    billmker = BillMaker(9, 12, cmker, amker)

    billlist = billmker.gen_bill_list()
    for bill in billlist:
        bill.print_bill(bill)
        print("=" * 60)
    print("*" * 60)
    print("*" * 60)


if __name__ == "__main__":
    main()
