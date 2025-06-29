# Alembic: Upgrade and Downgrade

## What is Upgrade?
- **Upgrade** means applying new migrations to your database to bring its schema up to date with your latest models/code.
- This can include adding tables, columns, indexes, or changing data types.
- Upgrading is how you move your database "forward" in time.

### How to Upgrade
- To apply all pending migrations:
  ```bash
  alembic upgrade head
  ```
- To upgrade to a specific revision:
  ```bash
  alembic upgrade <revision_id>
  ```
- `head` means the latest migration. You can also use revision hashes (shown in migration filenames).

---

## What is Downgrade?
- **Downgrade** means reverting (undoing) migrations, moving your database schema "backward" to a previous state.
- Useful if a migration introduced a bug or you need to roll back a feature.

### How to Downgrade
- To revert the last migration:
  ```bash
  alembic downgrade -1
  ```
- To downgrade to a specific revision:
  ```bash
  alembic downgrade <revision_id>
  ```
- You can chain downgrades to go back multiple steps.

---

## Best Practices
- Always back up your database before downgrading, as data loss is possible.
- Review migration scripts to ensure downgrades are safe and reversible.
- Test upgrades and downgrades on a staging environment before production.

---

## Common Commands
| Command                        | Description                                 |
|------------------------------- |---------------------------------------------|
| `alembic upgrade head`         | Upgrade to the latest migration             |
| `alembic upgrade <rev>`        | Upgrade to a specific revision              |
| `alembic downgrade -1`         | Revert the last migration                   |
| `alembic downgrade <rev>`      | Downgrade to a specific revision            |

---

## How to Write Upgrade and Downgrade Code in Alembic

- Each Alembic migration file has two functions: `upgrade()` and `downgrade()`.
- These functions define the exact changes to apply (upgrade) or revert (downgrade) in your database schema.

### Example Migration File Structure
```python
"""add email column to users table"""
revision = 'abc123'
down_revision = 'xyz789'
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))

def downgrade():
    op.drop_column('users', 'email')
```

### Writing Upgrade Code
- Use Alembic's `op` object to make schema changes:
  - `op.add_column()`: Add a new column
  - `op.create_table()`: Create a new table
  - `op.create_index()`: Add an index
- Example: Add a column
  ```python
  def upgrade():
      op.add_column('users', sa.Column('email', sa.String(), nullable=True))
  ```

### Writing Downgrade Code
- Write the **reverse** of your upgrade logic:
  - `op.drop_column()`: Remove a column
  - `op.drop_table()`: Remove a table
  - `op.drop_index()`: Remove an index
- Example: Remove the column you added above
  ```python
  def downgrade():
      op.drop_column('users', 'email')
  ```

### Tips
- Always make sure your downgrade undoes the upgrade safely.
- For complex changes (like data migrations), write custom SQL using `op.execute()`.
- Test both upgrade and downgrade on a test database before production.

---

> **Summary:**
> - `upgrade()` = apply schema changes
> - `downgrade()` = revert those changes
> - Use Alembic's `op` object for all schema operations

---

> **Tip:** Upgrades are routine, but downgrades should be used with caution—always check for possible data loss!
