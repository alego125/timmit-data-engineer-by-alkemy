import logging

# Creo el objeto logger
logger = logging.getLogger(__name__)

# Seteo el nivel de severidad del objeto logger
logger.setLevel(logging.DEBUG)

# Creo el handler en este caso el file handler
f_handler = logging.FileHandler("results.log")

# Seteo el nivel de severidad del filehandler, 
f_handler.setLevel(logging.INFO)

# Creo el formater con el formato que quiero que tenga el log
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Seteo este formato en el handler
f_handler.setFormatter(f_format)

# Agrego el handler al objeto logger
logger.addHandler(f_handler)
