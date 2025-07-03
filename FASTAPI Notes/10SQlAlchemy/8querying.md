# Querying Data in SQLAlchemy

## Basic Queries
```python
# Get all users
users = session.query(User).all()

# Get a user by ID
user = session.query(User).filter_by(id=1).first()
```

## Filtering
```python
# Filter users by name
users = session.query(User).filter(User.name == 'Alice').all()
```

## Joining Tables
```python
# Join users and posts
results = session.query(User, Post).join(Post).filter(User.id == Post.user_id).all()
```

## Updating Data
```python
# Update a user's name
user = session.query(User).filter_by(id=1).first()
user.name = 'Bob'
session.commit()
```

## Deleting Data
```python
# Delete a user
user = session.query(User).filter_by(id=1).first()
session.delete(user)
session.commit()
``` 