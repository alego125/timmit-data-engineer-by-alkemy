from fastapi import FastAPI
from database import Database
from model import Customer
from baseModels import Customers

app = FastAPI()


@app.get("/fetchItems/")
async def fetItems(query: str = None):
    """EndPoint that Use query to make resquest to database

    :param query: query of sql, defaults to None
    :type query: str, optional
    :return: response of query
    :rtype: dict
    """
    return Database().fetchQuery(query)


@app.put("/saveData/")
async def saveData(customer: Customers):
    """EndPoint that Create new register in database

    :param customer: Model of customer information
    :type customer: Customers
    """
    register = Customer(customer.name, customer.age, customer.email, customer.adress, customer.zip_code)
    # Use method saveData in database class to send register and save it in database
    Database().saveData(register)


@app.get("/fetchUserByName/")
async def fetchUserByName():
    """EndPoint that Return list of information json with coustomer name and age

    :return: list of customers name and age
    :rtype: list
    """
    return Database().fetchUserByName()


@app.get("/fetchAllUsers/")
async def fetchAllUsers():
    """EndPoint that Return list of dictionaries with customer information

    :return: list customers
    :rtype: list
    """
    return Database().fetchAllUsers()


@app.post("/updateCustomer/")
async def updateCustomer(customerName: str = None, adress: str = None):
    """EndPoint that take name of a customer to serch in 
    database and an address to be update

    :param customerName: name to serch, defaults to None
    :type customerName: str, optional
    :param adress: to be update, defaults to None
    :type adress: str, optional
    :return: message
    :rtype: str
    """
    return Database().updateCustomer(customerName, adress)


@app.delete("/deleteCustomer/")
async def deleteCustomer(customerName: str = None):
    """EndPoint that delete register that match with the param name

    :param customerName: to serch in database, defaults to None
    :type customerName: str, optional
    :return: message
    :rtype: str
    """
    return Database().deleteCustomer(customerName)