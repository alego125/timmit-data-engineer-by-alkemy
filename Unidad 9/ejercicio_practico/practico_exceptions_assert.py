# def write_text(lista):
#     """Function that take a list and assert with an input index number

#        :param: lista: list of words
#     """
#     index = int(input("Write index word in list: "))
#     assert index < len(lista)-1 and index > 0
#     print(f"In the postion {index} was found {lista[index]}")


# try:
#     write_text(['auto', 'avión', 'barco', 'bicicleta', 'ómnibus'])

# except Exception as index:
#     print(f"Index not found {type(index)}")
#     write_text(['auto', 'avión', 'barco', 'bicicleta', 'ómnibus'])


# def write_text(lista):
#     index = int(input("Write an index of list to search: "))
#     assert (index < len(lista)-1 and index > 0), funcion(index)

# def funcion(index):
#     print("Index error")
#     del index
#     write_text(['auto', 'avión', 'barco', 'bicicleta', 'ómnibus'])

# if __name__ == '__main__':
#     write_text(['auto', 'avión', 'barco', 'bicicleta', 'ómnibus'])


def assert_search_method(lista):
    index = int(input("Ingrese valor indice: "))
    try:
        assert (index < len(lista)-1 and index > 0)
        return f"En la posicion {index} se encontro el valor {lista[index]}"

    except AssertionError:
        return assert_search_method(
            ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus'])


if __name__ == '__main__':
    print(assert_search_method(
        ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']))
