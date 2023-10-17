# Created Homework branch for the main file
# HomeWork Lesson_11
from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    CheckConstraint,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Relationship

connection = create_engine("sqlite:///Lesson11_Main.db")


class Base(DeclarativeBase):
    ...


class Statuses(Base):
    __tablename__ = "Statuses"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(100), nullable=False, unique=True)
    order = Relationship("Orders", backref="status")


class Orders(Base):
    __tablename__ = "Orders"
    __tableargs__ = CheckConstraint("user_id IS NOT NULL")
    id = Column(INT, primary_key=True)
    user_id = Column(INT, ForeignKey("Users.id"))
    status_id = Column(INT, ForeignKey("Statuses.id"))


class Users(Base):
    __tablename__ = "Users"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(32), nullable=False, unique=False)
    email = Column(VARCHAR(24), unique=True)
    user = Relationship("Orders", backref="id")


class Order_Items(Base):
    __tablename__ = "Order Items"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    order_id = Column(INT, ForeignKey("Orders.id"))
    product_id = Column(INT, ForeignKey("Products.id"))
    order = Relationship("Orders", backref="id")


class Categories(Base):
    __tablename__ = "Categories"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), unique=True)
    category = Relationship("Products", backref="id")


class Products(Base):
    __tablename__ = "Products"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(36))
    description = Column(VARCHAR(140))
    category_id = Column(INT, ForeignKey("Categories.id"))
    order_item = Relationship("Order_Items", backref="id")


Base.metadata.create_all(connection)
