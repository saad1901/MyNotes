# 2. SQLAlchemy Session

A **Session** in SQLAlchemy is the main interface for interacting with the database in ORM mode. It manages the context for database operations, including object persistence, transactions, and queries.

## Why Use a Session?
- Handles transactions automatically.
- Tracks changes to objects and synchronizes them with the database.
- Provides a workspace for all the objects you load or associate with the database.

## Creating a Session
You need to create a `Session` object, usually using a `sessionmaker` factory.

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
```
- `engine` is the Engine object you created earlier.

## Basic Usage
### Adding and Committing Objects
```python
# Assuming you have a User model
user = User(name="Alice")
session.add(user)
session.commit()  # Writes changes to the database
```

### Querying
```python
users = session.query(User).all()
```

### Closing the Session
```python
session.close()
```

## Best Practices
- Use a new session for each logical unit of work (e.g., a web request).
- Always close the session when done.
- Use context managers for automatic cleanup (SQLAlchemy 1.4+):

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    # work with session
    ...
```

The session is a powerful tool for managing your database interactions in a safe and efficient way. 