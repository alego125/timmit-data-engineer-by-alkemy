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

    def fetchQuery(self, query: str) -> list:
        """Function that recieve query to excecute into excecute function
        and then return list of database registers in dictionary form
        """
        fetchQuery = self.connection.execute(query)
        listCustomers = []
        # Go throw database registers and save into a list to be return
        # With data in position 3,4 and 5 we need to
        # use strip with a white space
        # becouse in database register have a lot of white
        # space at the start and the end
        for data in fetchQuery.fetchall():            
            listCustomers.append({
                "Register": data[0],
                "Name": data[1],
                "Age": data[2],
                "Email": data[3].strip(" "),
                "Adress": data[4].strip(" "),
                "Zip-Code": data[5].strip(" ")
            })
  
            return {
                "Register": data[0],
                "Name": data[1],
                "Age": data[2],
                "Email": data[3].strip(" "),
                "Adress": data[4].strip(" "),
                "Zip-Code": data[5].strip(" ")
            }      
        # return listCustomers

    # Create MetaData objet, then create Table with customer information, meta
    # object and Columns that we requiere, After that excecute a select into customer
    # table and finally go throw the table data with for loop to store information in a list
    # of dictionary to be return
    def fetchUserByName(self) -> list:
        """Method that return customer name and age in database in dictionary form
        """

        meta = MetaData()
        customer = Table('customer', meta, Column('name'), Column('age'))
        data = self.connection.execute(customer.select())
        customerList = []
        for cust in data:
            customerList.append({
                "Name": cust[0],
                "Age": cust[1]
            })
        return customerList

    def fetchAllUsers(self) -> list:
        """Method that Bind an individual Session to the Connectio

        :classmethod:
        """
        self.session = Session(bind=self.connection)
        customers = self.session.query(Customer).all()        
        customerList = []
        # Go throw customers objects in form of dictionaries and append them into a list
        # to be return
        for cust in customers:
            customerList.append(cust)
        return customerList

    def saveData(self, customer: Customer) -> dict:
        """Create register of customer into database

        :classmethod:
        """
        try:
            session = Session(bind=self.connection)
            session.add(customer)
            session.commit()
            logger.info("Info saved successfuly")
            return {"message": "Info saved successfuly"}
        except Exception:
            logger.error(f"Error {Exception}")
            return {"message": f"Error {Exception}"}

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
            logger.info("Element updated succesfully")
            return {"message":"Element updated succesfully"}
        except Exception:
            logger.error("Register not exist")
            return {"message": "Register not exist"}

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
            session.commit()
            return {"message": f"Customer {customerData} deleted"}
        except Exception:
            logger.error("Register not exist")
            return {"message": "Register not exist"}





