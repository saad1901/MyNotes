# ORM Basics

## What is ORM?
ORM stands for Object Relational Mapper. It allows you to interact with your database using Python classes and objects instead of writing raw SQL queries.

## Why Use ORM?
- Simplifies database operations
- Reduces boilerplate code
- Makes code more maintainable and readable

## Simple Example
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```
This class defines a table `users` with columns `id` and `name`. 