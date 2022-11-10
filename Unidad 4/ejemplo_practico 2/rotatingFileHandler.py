import logging
from logging.handlers import RotatingFileHandler

# Creamo el logger
logger = logging.getLogger("simple_logger")

# Establecemos el nivel de severidad
logger.setLevel(logging.DEBUG)

# Creamos un rotating file handler y seteamos el nivel de severidad en DEBUG
handler = RotatingFileHandler('./Logs/LogsEjercicio/my_log.log',
                              maxBytes=2000, backupCount=50)
handler.setLevel(logging.DEBUG)

# Creamos un objeto de formato
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Agregamos el objeto formato al rotating file handler
handler.setFormatter(formatter)

# Agregamos el handler al logger
logger.addHandler(handler)

# Generamos los logs
for i in range(10000):
    logger.debug(f"Debug message {i}")
    logger.info(f"Info message {i}")
    logger.warning(f"Warning message {i}")
    logger.error(f"Error message {i}")
    logger.critical(f"Critical message {i}")
