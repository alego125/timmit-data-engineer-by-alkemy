import logging
import logging.config

logging.config.fileConfig(fname='custom.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug("Este es un mensaje de debug")
