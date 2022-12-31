import inspect
import logging


def customLogger(logLevel):
    loggerName = inspect.stack()[1][3]
    log = logging.getLogger(loggerName)

    log.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s: %(message)s', datefmt='%d-%m-%Y %H%M:%S')
    fileHandler.setFormatter(formatter)
    log.addHandler(fileHandler)

    return log
