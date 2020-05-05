# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


class LogisticCenter:
    def __init__(self, maxtaxi_count, maxbike_count, maxkamaz_count):
        self.__maxtaxi = maxtaxi_count
        self.__maxbike = maxbike_count
        self.__maxkamaz = maxkamaz_count
        self.__usedtaxi = 0
        self.__userbike = 0
        self.__usedkamaz = 0
        self.__busytransport_list = []


    def sendTaxi(self, serialnum):
        pass

    def sendBike(self, serialnum):
        pass

    def sendKamaz(self, serialnum):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
