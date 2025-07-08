# 5. Relationships in SQLAlchemy ORM

SQLAlchemy ORM allows you to define relationships between tables using foreign keys and relationship constructs. The most common relationships are one-to-many, many-to-one, and many-to-many.

## One-to-Many Relationship
Example: A user can have many posts.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', back_populates='author')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')
```

- `relationship()` creates a link between the two models.
- `ForeignKey` sets up the database-level relationship.
- `back_populates` allows bidirectional access.

## Many-to-Many Relationship
Example: Students and Courses.

```python
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

association_table = Table('association', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=association_table, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship('Student', secondary=association_table, back_populates='courses')
```

## Notes
- Always use `back_populates` or `backref` for bidirectional relationships.
- Relationships make it easy to navigate between related objects in your Python code. 