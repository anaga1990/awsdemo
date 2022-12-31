"""
Logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
import logging
import logging as log

log.basicConfig(filename="test.log", level=logging.DEBUG)
log.debug("debug logs")
log.info("info logs")
log.warning("warning logs")
log.error("error logs")
log.critical("critical logs")

