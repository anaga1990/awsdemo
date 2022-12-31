import logging

import logsUtilManager.custom_logger as logger


class LoggingApplicationTest():
    log = logger.customLogger(logging.DEBUG)

    def loginWithValidData(self):
        self.log.debug('debug logs')
        self.log.info('info logs')
        self.log.warning('warning logs')
        self.log.error('error logs')
        self.log.critical('critical logs')

    def loginWithInValidData(self):
        log = logger.customLogger(logging.INFO)
        log.debug('debug logs')
        log.info('info logs')
        log.warning('warning logs')
        log.error('error logs')
        log.critical('critical logs')

    def verifyLoginWithInValidData(self):
        log = logger.customLogger(logging.INFO)
        log.debug('debug logs')
        log.info('info logs')
        log.warning('warning logs')
        log.error('error logs')
        log.critical('critical logs')


logtest = LoggingApplicationTest()
logtest.loginWithValidData()
logtest.loginWithInValidData()
logtest.verifyLoginWithInValidData()
