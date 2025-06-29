# pytest: Python Testing Framework

## What is pytest?
- **pytest** is a powerful and easy-to-use testing framework for Python.
- It is the most popular tool for writing and running tests in modern Python projects.
- Supports unit, integration, and functional testing.

---

## Key Features
- Simple, readable test syntax (no need for classes or lots of boilerplate).
- Auto-discovers test files and functions (by default, files named `test_*.py` and functions named `test_*`).
- Rich set of built-in assertions and helpful error messages.
- Supports fixtures for setup/teardown and sharing test data.
- Plugins available for coverage, mocking, parallel runs, and more.

---

## Basic Example
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```
- Save as `test_example.py` and run with `pytest` in the terminal.

### What does `assert` do?
- The `assert` statement checks if a condition is `True`.
- If the condition is `False`, the test fails and pytest reports an error.
- In the example above, `assert add(2, 3) == 5` checks that the `add` function returns `5` when given `2` and `3`.
- `assert` is the main way to verify expected outcomes in pytest tests.

---

## Using pytest with FastAPI
- Use `TestClient` to test FastAPI endpoints.
- Example:
  ```python
  from fastapi.testclient import TestClient
  from main import app

  client = TestClient(app)

  def test_home():
      response = client.get("/")
      assert response.status_code == 200
  ```

---

## Common Commands
- `pytest` — Run all tests in the current directory.
- `pytest test_file.py` — Run tests in a specific file.
- `pytest -k "keyword"` — Run tests matching a keyword.
- `pytest --maxfail=1 --disable-warnings -q` — Stop after 1 failure, quiet output.

---

## Best Practices
- Name test files and functions clearly (`test_*.py`, `test_*`).
- Use fixtures for reusable setup/teardown logic.
- Keep tests isolated and independent.
- Run tests often!

---

## Useful Links
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [FastAPI Testing Docs](https://fastapi.tiangolo.com/tutorial/testing/)

> **Tip:** pytest is the standard for Python testing—learn it well for both interviews and real-world projects!
