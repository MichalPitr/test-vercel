# Import Logtail client library and deault logging library
import logging
import time

# Create handler
# Create logger
logger = logging.getLogger(__name__)
logger.handlers = []
logger.setLevel(logging.DEBUG) # Set minimal log level

# LOGGING EXAMPLE
# Following code shocases logger usage

# Send debug log using the debug() method

logger.warning('Log structured data', extra={
    'item': {
        'url': "https://fictional-store.com/item-123",
        'price': 100.00,
        'ridiculouslyLongFieldNameThatShouldBeIllegalButWhoKeepsTabsOnWhatDiagnosticsPeopleDo': "hello"
    }
})

while True:
    logger.debug('Log with "quotes" is fun.')
    logger.debug('Log with ""doublequotes"" is bad')
    logger.debug('Why even ////')
    logger.debug("outter double quotes ////")
    logger.debug("Why """"""")
    logger.debug("Terror ''''''")
    logger.debug("Terror ''''''")
    logger.debug("backslash n \\n cuz why not")

    time.sleep(30)

print('All done! You can check your logs now.')