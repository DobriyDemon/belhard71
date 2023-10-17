# Created Homework branch for the main file
# HomeWork Lesson_11
from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
    CheckConstraint,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Relationship


class Base(DeclarativeBase):
    ...


class Statuses(Base):
    __tablename__ = "statuses"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, ForeignKey("id"))
    name = Column(VARCHAR(100), nullable=False, unique=True)


class Orders(Base):
    __tablename__ = "Orders"
    __tableargs__ = CheckConstraint("user_id IS NOT NULL")
    id = Column(INT, primary_key=True)
    user_id = Column(INT, ForeignKey("user_id"))
    status_id = Relationship("Statuses", back_populates="id")


Base.metadata.create_all()


class Users(Base):
    __tablename__ = "Users"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(32), nullable=False, unique=False)
    email = Column(VARCHAR(24), unique=True)


class Order_Items(Base):
    __tablename__ = "Order Items"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    order_id = Column(INT, ForeignKey("order_id"))
    product = Column(INT, ForeignKey("order_id"))


class Categories(Base):
    __tablename__ = "Categories"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), unique=True)


class Products(Base):
    __tablename__ = "Products"
    __tableargs__ = CheckConstraint("name IS NOT NULL")
    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(36))
    description = Column(VARCHAR(140))
    category_id = Column(INT, ForeignKey("category_id"))
