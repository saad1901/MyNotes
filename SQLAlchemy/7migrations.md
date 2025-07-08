# 7. Database Migrations with Alembic

Database migrations are changes to your database schema (tables, columns, etc.) over time. Alembic is the recommended tool for managing migrations in SQLAlchemy projects.

## Why Migrations?
- Keep your database schema in sync with your models.
- Apply changes incrementally (add/remove columns, tables, etc.).
- Version control for your database structure.

## Installing Alembic
```bash
pip install alembic
```

## Setting Up Alembic
1. Initialize Alembic in your project:
   ```bash
   alembic init alembic
   ```
2. Edit `alembic.ini` and `alembic/env.py` to set your database URL and import your models.

## Creating a Migration
- Generate a migration script based on model changes:
  ```bash
  alembic revision --autogenerate -m "create user table"
  ```
- Review and edit the generated script if needed.

## Applying Migrations
- Apply migrations to the database:
  ```bash
  alembic upgrade head
  ```

## Downgrading
- Revert to a previous migration:
  ```bash
  alembic downgrade -1
  ```

Alembic helps you manage your database schema safely and efficiently as your application evolves. 