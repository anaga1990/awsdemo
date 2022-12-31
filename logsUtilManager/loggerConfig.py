import logging.config
import logging


class LoggerConfig():
    def testLog(self):
        logging.config.fileConfig("logging.conf")
        log = logging.getLogger(LoggerConfig.__name__)
        log.debug("debug logs")
        log.info("info logs")
        log.warning("warning logs")
        log.error("error logs")
        log.critical("critical logs")


logs = LoggerConfig()
logs.testLog()