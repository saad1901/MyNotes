# Reflecting Existing Databases

## What is Reflection?
Reflection is the process of loading table definitions from an existing database into SQLAlchemy.

## Why Use Reflection?
- Useful when working with legacy databases
- No need to manually define models for existing tables

## Example: Reflecting Tables
```python
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///example.db')
metadata = MetaData()

# Reflect all tables
metadata.reflect(bind=engine)

# Access a specific table
user_table = metadata.tables['users']
```

## Generating ORM Classes from Existing Tables
You can use tools like `sqlacodegen` to auto-generate ORM classes:
```bash
pip install sqlacodegen
sqlacodegen sqlite:///example.db > models.py
``` 