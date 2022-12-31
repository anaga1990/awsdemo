"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
Logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
import logging
import logging as log

log.basicConfig(filename="test11.log", level=log.INFO, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')
log.debug("debug logs")
log.info("info logs")
log.warning("warning logs")
log.error("error logs")
log.critical("critical logs")

# datefmt='%d-%m-%Y %I:%M:%S %p get