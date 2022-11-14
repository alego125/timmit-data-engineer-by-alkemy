import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler("Logs/logs.log","w")
c_handler = logging.StreamHandler()

formater = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)s - %(message)s')

f_handler.setFormatter(formater)
c_handler.setFormatter(formater)

logger.addHandler(f_handler)
logger.addHandler(c_handler)

