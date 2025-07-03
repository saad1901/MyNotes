# Relationships in SQLAlchemy

Relationships define how tables are linked to each other in a database.

## One-to-Many Relationship
Example: One user has many posts.
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')
```

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
    courses = relationship('Course', secondary=association_table, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    students = relationship('Student', secondary=association_table, back_populates='courses')
```

## Tips
- Use `back_populates` to set up bidirectional relationships.
- Use `secondary` for many-to-many relationships. 