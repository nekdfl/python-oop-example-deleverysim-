# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

class Bill:

    def __init__(self, src_addr, dst_addr, contact, is_fragile, weight, size):
        self.__src_addr = src_addr
        self.__dst_addr = dst_addr
        self.__contact = contact
        self.__is_fragile = is_fragile
        self.__weight = weight
        self.__size = size

    @property
    def get_src_address(self):
        return self.__src_addr

    @property
    def get_dest_address(self):
        return self.__dst_addr

    @property
    def get_contact(self):
        return self.__contact

    @property
    def is_fragile(self):
        return self.__is_fragile

    @property
    def get_weight(self):
        return self.__weight

    @property
    def get_size(self):
        return self.__size


def main():
    pass
    mybill = Bill("src", "dst", "cont", True, 10, 0.22)
    print(f"from: {mybill.get_src_address}; to: {mybill.get_dest_address}, call {mybill.get_contact},"
          f" care it {mybill.is_fragile}, weight kg: {mybill.get_weight}, size {mybill.get_size} m^3")


if __name__ == "__main__":
    main()
