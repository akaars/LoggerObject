#!/usr/bin/python
"""Logger wrapper
"""

__author__ = "Ilya Brik"

import logging
import time
from termcolor import cprint
from singleton_decorator import singleton


@singleton
class LoggerObject():
    """Creates a LoggerObject object useful for logging"""
    def __init__(self, file_name=""):
        self.__loggers = self._init_loggers(file_name)
        self.info_logger = self.__loggers[0]
        self.debug_logger = self.__loggers[1]


    def _init_loggers(self, file_name):
        from os import environ
        cur_date = time.strftime("%d_%b_%Y-%H_%M")
        if not file_name:
            try:
                if environ['logfile']:
                    file_name = environ['logfile'] + '_' + cur_date
            except KeyError:
                print("No logfile entry found in environment")
                file_name = "/tmp/" + cur_date
        else:
            file_name = file_name + '_' + cur_date
            print("using default filename for logging: %s" % file_name)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        def setup_logger(name, log_file, level=logging.INFO):
            """Common logger setup"""

            handler = logging.FileHandler(filename=log_file, mode='w')
            handler.setFormatter(formatter)

            logger = logging.getLogger(name)
            logger.setLevel(level)
            logger.addHandler(handler)
            return logger

        file_name = file_name + ".log"
        print("Create logging file %s" % file_name)
        info_logger = setup_logger('INFO', file_name, logging.INFO)
        debug_logger = setup_logger('DEBUG', file_name + '.debug', logging.DEBUG)
        return info_logger, debug_logger

    def Info(self, msg_txt, color="blue"):
        time_str = time.strftime("%c") + " INFO "
        cprint(time_str + msg_txt, color)
        self.info_logger.info(msg_txt)

    def Warn(self, msg_txt, color="magenta"):
        time_str = time.strftime("%c") + " WARN  "
        cprint(time_str + msg_txt, color, attrs=['bold'])
        self.info_logger.warn(msg_txt)
        self.debug_logger.warn(msg_txt)

    def Debug(self, msg_txt, color="red", print_screen=False):
        if print_screen:
            time_str = time.strftime("%c") + " DEBUG "
            cprint(time_str + msg_txt, color, attrs=['bold'])
        self.debug_logger.debug(msg_txt)

    def Err(self, msg_txt, color="magenta"):
        time_str = time.strftime("%c") + " ERROR "
        cprint(str(time_str) + str(msg_txt), color, attrs=['bold'])
        self.info_logger.error(msg_txt)
        self.debug_logger.error(msg_txt)


