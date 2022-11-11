import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("./Unidad 16/Practico/logs/database.log","a")
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(f_format)
f_handler.setFormatter(f_format)

logger.addHandler(f_handler)
logger.addHandler(c_handler)
