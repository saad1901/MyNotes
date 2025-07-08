# 3. Defining Models in SQLAlchemy ORM

In SQLAlchemy ORM, models are Python classes that represent database tables. You define models by subclassing a base class created by `declarative_base()`.

## Setting Up the Base
```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

## Defining a Model
Each model class represents a table. Columns are defined as class attributes.

```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'  # Table name in the database

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
```

- `__tablename__`: Name of the table in the database.
- `id`, `name`, `email`: Columns in the table.
- `primary_key=True`: Marks the column as the primary key.
- `unique=True`: Ensures the column values are unique.

## Creating Tables
To create tables in the database based on your models:
```python
Base.metadata.create_all(engine)
```

This will create all tables defined by your models if they do not already exist. 