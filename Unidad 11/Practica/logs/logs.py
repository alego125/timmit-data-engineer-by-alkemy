import logging
from pathlib import Path

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
# Obtain the path root with Path module and then indicate the file name
f_handler = logging.FileHandler(f"{Path(__file__).parent}/logs.log", "w")

formater = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)s - %(message)s')

c_handler.setFormatter(formater)
f_handler.setFormatter(formater)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
