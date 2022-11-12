"""Module that evaluete a list index if exist or not in diferents ways
"""


class Lists:
    """Class that serch index lists into lists in diferents ways.

        :param: list: lists of things
        :type: list
    """

    def __init__(self, list) -> None:
        self.list = list

    # FORM N°1 - USING WHILE LOOP
    def request_index_loop(self) -> str:
        """Method that take an index and show if it
        is posible to get value in a list transports,
        if not posible make a request index again.

        :return: String
        :type: String
        """

        # ask for index until the program doesn't give any more errors
        while True:
            try:
                index = int(input("Give an index number: "))
                self.list[index]
                break
            except Exception as error:
                print(f'Error - {type(error)}')

        return f"Value {self.list[index]} was found in position {index}"

    # FORM N°2 - USING RECURTION PROGRAMING
    def request_index_recursive(self) -> str:
        """This Method take the list as a param. Then make
        request for an index and show if it
        is posible to get value in a list of transports.

        :return: String
        :type: String
        """

        try:
            index = int(input("Give an index number: "))
            return f"Value {self.list[index]} in position {index}"
        except Exception as error:
            print(f'Error - {type(error)}')
            return self.request_index_recursive()

    # FORM N°3 - USING ASSERT
    def assert_search_method(self) -> str:
        """Method with recoursion that use assert to verify index in a list

        :return: String
        :type: String
        """
        index = int(input("Insert inde value: "))
        try:
            assert (index < len(self.list)-1 and index > 0)
            return f"""In the position {index} we
                       found the value {self.list[index]}
                       """

        except AssertionError:
            return self.assert_search_method(self.list)

    def main():
        """
        """
        print("""
                 Options menu:
                 1- List items
                 2- Verify if index exist with loop try except
                 3- Verify if index exist with recursive try except
                 4- Verify if index exist with assert and try except
                 5- Exit
                """)
        option = int(input("Insert your menu option: "))
        if option is 1:
            print([item for item in self.list])


if __name__ == "__main__":
    object_class = Lists(['auto', 'avión', 'barco', 'bicicleta', 'ómnibus'])
    print(object_class.request_index_loop())
    # print(object_class.request_index_recursive())
