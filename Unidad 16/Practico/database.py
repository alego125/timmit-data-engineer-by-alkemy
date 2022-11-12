"""
.. module:: database
   :platform: Windows
   :synopsis: Module with class database to make connection and action in database.

.. moduleauthor:: Alejandro Gomez

"""

import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.orm import Session
from model import Customer, Base
from logsHandlers import logger
from decouple import config

# Set environment variables into global variables to be use into Database class
database = config('DATABASE_NAME')
user = config('USER_NAME')
password = config('PASSWORD')
server = config('SERVER_NAME')
port = config('PORT')


class Database:
    """Class Database that create connection to database and make some actions.
    """

    try:
        # Replace user, password, hostname and
        # database according to your configuration
        engine = db.create_engine(
            f'postgresql://{user}:{password}@{server}:{port}/{database}')

        Base.metadata.create_all(bind=engine)
    except Exception:
        logger.error(f"Error {Exception}")

    def __init__(self) -> None:
        self.connection = self.engine.connect()
        print("DB instance created")

    def fetchQuery(self, query: str) -> None:
        """Function that recieve query to excecute into excecute function
        and then print database registers
        """
        fetchQuery = self.connection.execute(query)

        # Go throw database registers and print them
        # With data in position 2,3 and 4 we need to
        # use strip with a white space
        # becouse in database register have a lot of white
        # space at the start and the end
        for data in fetchQuery.fetchall():
            print(f"""
                Register: {data[0]}
                Name: {data[1]}
                Age: {data[2]}
                Email: {data[3].strip(" ")}
                Adress: {data[4].strip(" ")}
                Zip-Code: {data[5].strip(" ")}
            """)

    # def saveData(self, customer: Customer):
    #     """Mehtod that save complete data into database with a query sentence
    #     """
    #     self.connection.execute(f"""
    #         INSERT INTO customer(name, age, email, adress, zip_code)
    #         VALUES(
    #             '{customer.name}',
    #             '{customer.age}',
    #             '{customer.email}',
    #             '{customer.address}',
    #             '{customer.zip_code}'
    #         )""")

    # Create MetaData objet, then create Table with customer information, meta
    # object and Columns that we requiere, After that excecute a select into customer
    # table and finally go throw the table data with for loop to show information in tuples
    def fetchUserByName(self) -> None:
        """Method that show customer name and age in database with print

        :classmethod:
        """
        meta = MetaData()
        customer = Table('customer', meta, Column('name'), Column('age'))
        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)

    def fetchAllUsers(self) -> None:
        """Method that Bind an individual Session to the Connectio

        :classmethod:
        """
        self.session = Session(bind=self.connection)
        customers = self.session.query(Customer).all()        
        for cust in customers:
            print(cust)

    def saveData(self, customer) -> None:
        """Create register of customer into database

        :classmethod:
        """
        try:
            session = Session(bind=self.connection)
            session.add(customer)
            session.commit()
            logger.info("Info saved successfuly")
        except Exception:
            logger.error(f"Error {Exception}")

    def updateCustomer(self, customerName, address) -> None:
        """Update customer in the database

        :param customerName
        :param address
        :type string
        :classmethod:
        """
        session = Session(bind=self.connection)
        dataToUpdate = {Customer.adress: address}
        try:
            # Line that create the query sentence to make the update filtering by name
            customerData = session.query(Customer).filter(Customer.name==customerName)
            customerData.update(dataToUpdate)
            session.commit()
            logger.info(f"Element updated succesfully")
        except Exception:
            logger.error("Register not exist")

    def deleteCustomer(self, customerName: str) -> None:
        """Method that delete customer regiter by customer name.

        :param: customerName
        :classmethod:
        """
        session = Session(bind=self.connection)
        try:
            customerData = session.query(Customer).filter(Customer.name==customerName).first()
            session.delete(customerData)
            logger.info(f"Customer {customerData} deleted")
        except Exception:
            logger.error("Register not exist")
        session.commit()


if __name__ == '__main__':

    dbinfo = Database()
    while True:
        print("""
            Menu
            1) Create Register
            2) Fetch user by Name
            3) Fetch All Users
            4) Update Customer
            5) Delete Customer
            6) Exit
        """)
        option = int(input("Insert your option: "))
        match option:
            case 1:
                try:
                    name: str = input("Insert name: ")
                    age: int = int(input("Insert age: "))
                    email: str = input("Insert email: ")
                    address = input("Insert address: ")
                    zip_code: str = input("Insert zip_code: ")
                    customer = Customer(name, age, email, address, zip_code)
                    dbinfo.saveData(customer)
                except TypeError:
                    logger.error(TypeError)
            case 2:
                dbinfo.fetchUserByName()

            case 3:
                dbinfo.fetchAllUsers()

            case 4:
                try:
                    name = input("Insert name to update: ")
                    address = input(f"Insert address to be replaced into register with name {name}: ")
                    dbinfo.updateCustomer(name, address)
                except TypeError:
                    logger.error(TypeError)

            case 5:
                try:
                    name = input("Insert customer name to be deleted: ")
                    dbinfo.deleteCustomer(name)
                except TypeError:
                    logger.error(TypeError)

            case 6:
                break

    # Manual tests
    # customer = Customer('Paul', 23,'paul@gmail.com', 'address from paul', '2321LL')
    # customer = Customer('Felipe',32,'felipegarcia@gmail.com','address from felipe','3413MS')
    # customer = Customer('Teddy',90,'teddy@gmail.com','address from teddy','3423PO')
    # customer = Customer('Mark',17,'mark@gmail.com','address from mark','9423MA')
    # customer = Customer('David',35,'david@gmail.com','address from david','2341DA')
    # customer = Customer('Allen',56,'allen@gmail.com','address from allen','3423PO')
    # customer = Customer('James',56,'james@gmail.com','address from james','3423PO')    
    # dbinfo.saveData(customer)

    # dbinfo.fetchQuery("SELECT * FROM customer")
