# Installation

## 1. Setting Up a Virtual Environment
It is recommended to use a virtual environment for Python projects to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 2. Installing SQLAlchemy
Install SQLAlchemy using pip:

```bash
pip install SQLAlchemy
```

For working with a specific database (e.g., PostgreSQL, MySQL), install the appropriate driver:
- PostgreSQL: `pip install psycopg2-binary`
- MySQL: `pip install pymysql`
- SQLite: (built-in with Python)

## 3. Verifying Installation
Check the installation by importing SQLAlchemy in Python:

```python
import sqlalchemy
print(sqlalchemy.__version__)
```

If no errors occur and the version prints, SQLAlchemy is installed correctly. 