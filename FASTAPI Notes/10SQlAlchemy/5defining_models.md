# Defining Models

## Creating Tables with Python Classes
SQLAlchemy uses Python classes to define database tables.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
```

## Column Types
- `Integer`, `String`, `Float`, `Boolean`, `DateTime`, etc.

## Primary Keys and Constraints
- Use `primary_key=True` to define a primary key.
- Use `nullable=False` to make a column required.
- You can add unique constraints, default values, and more. 