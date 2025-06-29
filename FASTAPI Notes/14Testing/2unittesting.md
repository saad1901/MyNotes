# Unit Testing in Python

## What is Unit Testing?
- Unit testing is the practice of testing individual units (functions, methods, or classes) of code in isolation.
- The goal is to ensure each part of your code works as expected on its own.

---

## Why Unit Test?
- Catches bugs early and locally.
- Makes code easier to refactor and maintain.
- Documents how functions/classes are supposed to behave.

---

## Common Python Unit Testing Tools
- **unittest** (built-in Python module)
- **pytest** (most popular, more features and easier syntax)

---

## Example: Using unittest
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

---

## Best Practices
- Test one thing per test function.
- Use descriptive test names.
- Run tests often!

> **Tip:** For modern Python projects, `pytest` is often preferred for its simplicity and power, but knowing `unittest` is useful for interviews and legacy code.
