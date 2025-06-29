 # Alembic vs SQLAlchemy: Purpose and Usage

## SQLAlchemy
- **SQLAlchemy** is an Object Relational Mapper (ORM) for Python.
- It lets you define your database schema as Python classes (models).
- You can use SQLAlchemy to:
  - Define tables and columns in Python code.
  - Interact with the database using Python objects (CRUD operations).
  - Create tables in the database (if they don't exist) using:
    ```python
    Base.metadata.create_all(bind=engine)
    ```
- **Limitation:** If you change your models (e.g., add/remove a column), SQLAlchemy does NOT automatically update the existing database schema. It only creates missing tables.

---

## Alembic
- **Alembic** is a database migration tool for SQLAlchemy.
- It tracks changes to your models and generates migration scripts to update your database schema over time.
- You use Alembic to:
  - Generate migration files when your models change.
  - Apply migrations to upgrade or downgrade your database schema.
  - Keep your database schema in sync with your models, even as your app evolves.
- **Key advantage:** Handles schema changes safely and versioned, so you don't lose data or have to manually write SQL for every change.

---

## When to Use Each
- **Use SQLAlchemy's `create_all()`**:
  - For initial development, prototyping, or when you don't care about existing data.
  - Not recommended for production, as it doesn't handle schema changes after the first creation.
- **Use Alembic**:
  - For any project where your database schema will change over time.
  - Essential for production apps to manage migrations, upgrades, and downgrades.

---

## Summary Table
| Feature                | SQLAlchemy                | Alembic                        |
|------------------------|--------------------------|-------------------------------|
| Define models/schema   | Yes                      | No                            |
| Create tables          | Yes (`create_all()`)     | No                            |
| Handle schema changes  | No                       | Yes (migrations)              |
| Version control        | No                       | Yes                           |
| Data safety            | No (can lose data)       | Yes (safe migrations)         |

---

> **Tip:** Use SQLAlchemy for defining and interacting with your data, and Alembic for managing schema changes and migrations in any real-world project.