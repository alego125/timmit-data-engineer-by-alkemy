import pytest
import requests

# Create an example user to the test
xample = {
  "name": "Pablo",
  "age": 40,
  "email": "pablo.miranda@gmail.com",
  "adress": "calle falsa 1234",
  "zip_code": "4422"
}


# Test the extraction of registers name amd age end point
def test_fetchByname_endpoint():

    assert requests.get("http://127.0.0.1:8000/fetchUserByName").status_code == 200


# Test the extraction of all users
def test_fetchAllUsers_endpoint():

    assert requests.get("http://127.0.0.1:8000/fetchAllUsers").status_code == 200


# Test if data is save correctly
def test_saveData_endpoint():

    assert requests.put("http://127.0.0.1:8000/saveData", json=xample).status_code == 200


# Test the update of data that was enter in the above test function
def test_updateData_endpoint():

    assert requests.post("http://127.0.0.1:8000/updateCustomer?customerName=Pablo&adress=martos22").status_code == 200


# Test for the last the delete method to delete the register of the example
def test_deleteData_endpoint():

    assert requests.delete("http://127.0.0.1:8000/deleteCustomer?customerName=Pablo").status_code == 200
