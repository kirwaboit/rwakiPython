import logging

# This emptys out the log file so that we can start with a clean fresh one
with open(file=r'logging/example3.log', mode='w+') as f:
    f.truncate(0)

# configures a fresh new log file
logging.basicConfig(filename=r'logging/example3.log', format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S'   ,level=logging.DEBUG)
# Here we demonstrate how to put variables into the log file output
james = 3+3
logging.debug('This message should go to the log file %s',james)
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

