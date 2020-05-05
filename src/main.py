# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8
# links:
#   python singleton

import signal
from src.deleverysim import DeleverySim


# MainApp = singleton с отложенным созданием экземпляра
#
class MainApp:
    __instance = None

    def __init__(self):
        self.__dsym = DeleverySim()

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = MainApp()
        return cls.__instance

    def request_params(self):
        self.__dsym.user_input()

    def loop(self):
        while True:
            # Do nothing and hog CPU forever until SIGINT received.
            pass
            self.__dsym.do_simulate_cycle()


def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


def init():
    pass
    # init logger
    # init config
    # update logger config


def main():
    mainapp = MainApp()
    mainapp.get_instance()
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    # mainapp.request_params()
    print('Running. Press CTRL-C to exit.')
    mainapp.loop()


if __name__ == "__main__":
    main()
