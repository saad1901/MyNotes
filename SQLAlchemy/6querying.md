# 6. Querying Data in SQLAlchemy ORM

SQLAlchemy ORM provides a powerful and flexible way to query data from your database using Python code.

## Basic Query
```python
users = session.query(User).all()  # Get all users
```

## Filtering
```python
# Get users with a specific name
users = session.query(User).filter(User.name == "Alice").all()

# Multiple conditions
users = session.query(User).filter(User.name == "Alice", User.email.like("%@example.com")).all()
```

## Ordering
```python
users = session.query(User).order_by(User.name).all()
```

## Limiting Results
```python
users = session.query(User).limit(5).all()  # Get first 5 users
```

## Joining Tables
Assume you have a `User` and `Post` model with a relationship.
```python
from sqlalchemy.orm import joinedload

# Get users and their posts
users = session.query(User).options(joinedload(User.posts)).all()

# Join and filter
posts = session.query(Post).join(User).filter(User.name == "Alice").all()
```

## Counting
```python
count = session.query(User).count()
```

SQLAlchemy's query API is very expressive and allows you to build complex queries using Python syntax. 