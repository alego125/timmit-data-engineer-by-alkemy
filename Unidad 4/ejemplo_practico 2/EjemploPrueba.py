import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')
rf_handler = RotatingFileHandler('./Logs/LogsEjemplo/my_log.log',
                                 maxBytes=30, backupCount=5)

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.ERROR)
rf_handler.setLevel(logging.DEBUG)


rf_formater = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(lineno)s - %(message)s')
rf_handler.setFormatter(rf_formater)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.addHandler(rf_handler)

logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
logger.debug('Esto es un Debug')
