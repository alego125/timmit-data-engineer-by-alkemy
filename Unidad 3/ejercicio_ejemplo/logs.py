import logging

# Creamos el logger personalizado
# logger = logging.getLogger(__name__)
logger = logging.getLogger("Este es mi logger")

# Ajustamos el nivel de severidad del logger
logger.setLevel(logging.DEBUG)

# Creamos los handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("../app.log")

# Ajustamos el nivel de severidad de los handlers
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Creamos el formato y se lo agregamos a cada uno de los handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Ahora agregamos los hadlers al logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Realizamos la prueba del logger personalizado
logger.warning("Esto es un mensaje de warning")
logger.error("Esto es un mensaje de error")
