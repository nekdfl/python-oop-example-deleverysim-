# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import random


class BillMaker:

    def __init__(self, min: int, max: int, contactmaker, addressmaker):
        pass
        self.__mingenbill = min
        self.__maxgenbill = max
        self.__contactmaker = contactmaker
        self__addressmaker = addressmaker

    def __get_gencount(self):
        count = random.randrange(min, max)
        return count

    def gen_bill_list(self):
        pass



def main():
    pass


if __name__ == "__main__":
    main()
