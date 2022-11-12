import logs


fruits = ['Frutilla', 'Melón', 'PERA', 99.6, 'NaranJA', 'mORa', 'NisPERo', 99]

for pos, fruit in enumerate(fruits):
    """Indicate two ways to solve this topic the firstone 
    use if block to solve it and the secondone use try 
    catch. In the two ways we use logs 

    :param: fruits: list of fruits names
    """
    # FORMA 1
    # if type(fruit) == str:
    #     fruits[pos]=fruit.lower()
    #     logging.info(f"Conversion exitosa: {fruit} -> {fruits[pos]}")
    # else:
    #     logging.error(f"Conversión Fallida: {fruit}")

    #FORMA 2
    try:
        fruta = fruit.lower()
        fruits[pos] = fruta
        logs.logger.info(f"Conversion exitosa: {fruit} -> {fruta}")
    except Exception:
        logs.logger.error(f"Conversión Fallida: {fruit}")
