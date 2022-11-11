"""Calculator module that simulate functionality of a simple calculator
"""


class Calculadora:
    """Class that simulate calculator functions addition, subtraction,
    multiplication and division
    """

    def add(self, num1: float, num2: float) -> float:
        """Method that make addition operation

        :param num1: first value of operation
        :type: float
        :param num2: second value of operation
        :type: float
        :return: addition between num1 and num2
        :rtype: float
        """
        return num1 + num2

    def subtract(self, num1: float, num2: float) -> float:
        """Method that make subtraction operation

        :param num1: first value of operation
        :type: float
        :param num2: second value of operation
        :type: float
        :return: subtraction between num1 and num2
        :rtype: float
        """
        return num1 - num2

    def multiply(self, num1: float, num2: float) -> float:
        """Method that make multiplication operation

        :param num1: first value of operation
        :type: float
        :param num2: second value of operation
        :type: float
        :return: multiplication between num1 and num2
        :rtype: float
        """
        return num1 * num2

    def divide(self, num1: float, num2: float) -> float:
        """Method that make division operation

        :param num1: first value of operation
        :type: float
        :param num2: second value of operation
        :type: float
        :return: division between num1 and num2
        :rtype: float
        """
        return num1 / num2
