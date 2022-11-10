

def string_to_number(string_list: list) -> list:
    # Extract number of character of each element
    # in string_list and return it as a comprehension list
    return [len(string) for string in string_list]


if __name__ == '__main__':
    print(string_to_number(['Alejandro', 'perro', 'gato', 'australopitecus']))
