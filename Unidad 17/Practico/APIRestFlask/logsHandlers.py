import logging
from pathlib import Path

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(f"{Path(__file__).parent}/logs/database.log","a")
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(f_format)
f_handler.setFormatter(f_format)

logger.addHandler(f_handler)
logger.addHandler(c_handler)
