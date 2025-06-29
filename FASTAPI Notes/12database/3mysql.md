# MySQL Quick Notes

## What is MySQL?
- MySQL is a popular open-source relational database management system (RDBMS).
- Widely used for web applications, especially with PHP (LAMP stack), but also works well with Python, Java, and more.

## Key Features
- Open source and free (with commercial options via Oracle).
- ACID compliant (with InnoDB engine).
- Supports SQL, transactions, indexing, and replication.
- Good performance and scalability for most use cases.

## Common Use Cases
- Web applications (WordPress, e-commerce, etc.)
- Data warehousing
- Logging and analytics

## Connecting FastAPI to MySQL
1. Install dependencies:
   ```bash
   pip install sqlalchemy pymysql
   ```
2. Example connection string:
   ```python
   SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@host:port/dbname"
   ```
3. Use SQLAlchemy's `create_engine` to connect.

## Best Practices
- Use environment variables or a `.env` file for credentials.
- Use migrations (like Alembic) for schema changes.
- Regularly back up your database.

## Useful Links
- [MySQL Official Site](https://www.mysql.com/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [FastAPI SQL Databases Tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases/)

> Tip: MySQL is a solid choice for many web apps due to its speed, reliability, and large community support.
