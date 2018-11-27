__author__ = "Ilya Brik"

from logger_object import LoggerObject

def test_loggerobj_is_singleton():
    logger_obj1 = LoggerObject("/tmp/test_file")
    logger_obj2 = LoggerObject()
    logger_obj3 = LoggerObject("/tmp/test_file2")
    assert logger_obj1 == logger_obj2 == logger_obj3


def default_log_file_is_created():
    del LoggerObject
    logger_obj1 = LoggerObject("/tmp/__test_file")
