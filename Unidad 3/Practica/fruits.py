import logs

# Other way to make loging config is with logging basicConfig
# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='results.log',
#     format='%(asctime)s - %(name)s - %(message)s'
# )


fruits = ['Frutilla', 'Melón', 'PERA', 99.6, 'NaranJA', 'mORa', 'NisPERo', 99]

for pos, fruit in enumerate(fruits):
    """Indicate two ways to solve this topic the firstone 
    use if block to solve it and the secondone use try 
    catch. In the two ways we use logs 

    :param: fruits: list of fruits names
    """

    # if type(fruit) == str:
    #     fruits[pos]=fruit.lower()
    #     logging.info(f"Conversion exitosa: {fruit} -> {fruits[pos]}")
    # else:
    #     logging.error(f"Conversión Fallida: {fruit}")

    try:
        fruta = fruit.lower()
        fruits[pos] = fruta
        logs.logger.info(f"Conversion exitosa: {fruit} -> {fruta}")
    except Exception:
        logs.logger.error(f"Conversión Fallida: {fruit}")
