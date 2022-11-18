"""Module that creat a personalized logger to will be use into unidad5 module
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(
    "/usr/local/airflow/include/logs/custom_logs.log", "a")

format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(levelno)s - %(message)s')

c_handler.setFormatter(format)
f_handler.setFormatter(format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
