# 4. CRUD Operations in SQLAlchemy ORM

CRUD stands for Create, Read, Update, and Delete—the four basic operations for managing data in a database. SQLAlchemy ORM makes these operations easy using model classes and sessions.

Assume you have a `User` model as defined previously.

## 1. Create (Insert)
```python
user = User(name="Alice", email="alice@example.com")
session.add(user)
session.commit()
```

## 2. Read (Query)
- Get all users:
  ```python
  users = session.query(User).all()
  ```
- Get a user by ID:
  ```python
  user = session.query(User).filter_by(id=1).first()
  ```

## 3. Update
```python
user = session.query(User).filter_by(id=1).first()
user.name = "Bob"
session.commit()
```

## 4. Delete
```python
user = session.query(User).filter_by(id=1).first()
session.delete(user)
session.commit()
```

## Notes
- Always commit after making changes (create, update, delete) to persist them in the database.
- Use `session.rollback()` to undo uncommitted changes if needed.

These basic operations allow you to manage your data efficiently using SQLAlchemy ORM. 