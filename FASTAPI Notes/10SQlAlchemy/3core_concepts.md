# Core Concepts

## 1. Engine
The Engine is the starting point for any SQLAlchemy application. It manages the connection to the database.

```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db')
```

## 2. MetaData
MetaData is a container object that keeps together many different features of a database (tables, schemas, etc.).

```python
from sqlalchemy import MetaData
metadata = MetaData()
```

## 3. Session
The Session is the ORM's handle to the database. It manages object persistence and transactions.

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

## How They Work Together
- The Engine connects to the database.
- MetaData describes the structure of the database.
- The Session is used to interact with the database using ORM. 