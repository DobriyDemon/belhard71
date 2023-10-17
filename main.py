# Created Homework branch for the main file
#HomeWork Lesson_11
from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, CheckConstraint, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Relationship


class Base(DeclarativeBase):
    ...

