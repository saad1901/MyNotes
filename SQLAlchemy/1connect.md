# 1. Connecting to a Database with SQLAlchemy

To use SQLAlchemy, you first need to connect to a database. SQLAlchemy supports many databases, such as SQLite, PostgreSQL, MySQL, and more.

## Installing SQLAlchemy
```bash
pip install sqlalchemy
```

## Creating an Engine
The `Engine` is the starting point for any SQLAlchemy application. It manages the connection to the database.

### Example: Connecting to SQLite
```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db')
```
- This creates a SQLite database file named `example.db` in your current directory.

### Example: Connecting to PostgreSQL
```python
engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
```

### Example: Connecting to MySQL
```python
engine = create_engine('mysql+pymysql://username:password@localhost:3306/mydatabase')
```

## Engine Arguments
- `echo=True`: Logs all SQL statements.
- `future=True`: Enables 2.0 style usage (recommended for new code).

```python
engine = create_engine('sqlite:///example.db', echo=True, future=True)
```

The `engine` object is used throughout your application to interact with the database. 