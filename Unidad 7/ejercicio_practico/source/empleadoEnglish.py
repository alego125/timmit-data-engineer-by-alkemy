from datetime import datetime
from dateutil.relativedelta import relativedelta


class Employee:
    """Class that conains employee information and return it

        :param nombre: employee name,
        :param apellido: employee last name,
        :param fecha_nacimiento: employee date of birth,
        :param nro_dni: employee dni number
        :type: string
    """

    def __init__(self, name: str,
                 last_name: str,
                 date_of_birth: str,
                 dni_number: str):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.dni_number = dni_number

    def get_age(self) -> str:
        """Obtain employee age with date of birth

            :returns: employee age
            :rtype: int
        """

        return relativedelta(datetime.now(),
                             datetime.strptime(self.date_of_birth,
                                               '%d/%m/%Y')).years

    def present_yourself(self) -> str:
        """Employee presentation

            :returns: texto con infromacion del empleado
            :rtype: str
        """

        return f"""Hi, I'm {self.name} {self.last_name}.
                 I born on {self.date_of_birth}
                 and my DNI is {self.dni_number}"""

    def __str__(self) -> str:
        return f'''
                   Name : {self.name}
                   Last Name : {self.last_name}
                   Date of Birth : {self.date_of_birth}
                   DNI number : {self.dni_number}
                '''


if __name__ == "__main__":

    employee = Employee("Alejandro", "Gomez", "20/11/1990", "35627087")

    print(employee.present_yourself())
    print(employee)
    print(employee.get_age())
