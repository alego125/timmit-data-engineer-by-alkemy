from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    adress = Column(String)
    zip_code = Column(String)

    def __init__(self, name: str, age: int, email: str, adress: str, zip_code:str) -> None:
        # self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.adress = adress
        self.zip_code = zip_code


    def __repr__(self) -> str:
        return f"<Customer(name={self.name},age={self.age},email={self.email}, address={self.adress}, Zip Code={self.zip_code})>"
