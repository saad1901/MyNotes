# Advanced Features

## 1. Migrations with Alembic
Alembic is a lightweight database migration tool for SQLAlchemy.

- Install Alembic:
  ```bash
  pip install alembic
  ```
- Initialize Alembic:
  ```bash
  alembic init alembic
  ```
- Create a migration:
  ```bash
  alembic revision --autogenerate -m "message"
  alembic upgrade head
  ```

## 2. Connection Pooling
SQLAlchemy manages a pool of database connections for efficiency.

```python
engine = create_engine('sqlite:///example.db', pool_size=10, max_overflow=20)
```

## 3. Custom Types
You can define custom column types by subclassing `TypeDecorator`.

```python
from sqlalchemy.types import TypeDecorator, VARCHAR

class LowerCaseString(TypeDecorator):
    impl = VARCHAR
    def process_bind_param(self, value, dialect):
        return value.lower() if value else value
``` 