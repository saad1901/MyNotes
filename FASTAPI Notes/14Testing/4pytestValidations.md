# pytest: Common Validations and Assertions

When writing tests with pytest, you often need to validate different types of data and behaviors. Here are common types of validations and how to perform them:

---

## 1. Integer and Numeric Validations
- Check if a value is equal to an expected integer:
  ```python
  assert result == 42
  ```
- Check if a value is greater/less than:
  ```python
  assert value > 0
  assert value <= 100
  ```
- Check if a value is within a range:
  ```python
  assert 10 <= value <= 20
  ```

---

## 2. Boolean Validations
- Check if a value is True or False:
  ```python
  assert is_active is True
  assert is_deleted is False
  ```

---

## 3. Type Validations
- Check if a value is of a certain type:
  ```python
  assert isinstance(result, int)
  assert isinstance(name, str)
  assert isinstance(data, list)
  ```

---

## 4. String Validations
- Check string equality:
  ```python
  assert username == "admin"
  ```
- Check substring:
  ```python
  assert "error" in message
  ```
- Check string starts/ends with:
  ```python
  assert email.startswith("user@")
  assert filename.endswith(".txt")
  ```

---

## 5. List/Collection Validations
- Check length:
  ```python
  assert len(items) == 3
  ```
- Check membership:
  ```python
  assert 5 in numbers
  assert "apple" not in fruits
  ```
- Check all elements meet a condition:
  ```python
  assert all(isinstance(i, int) for i in numbers)
  ```

---

## 6. Dictionary Validations
- Check key/value presence:
  ```python
  assert "id" in user
  assert user["name"] == "Alice"
  ```

---

## 7. Exception Validations
- Check if a function raises an exception:
  ```python
  import pytest

  with pytest.raises(ValueError):
      func_that_should_fail()
  ```

---

## 8. None/Null Validations
- Check if a value is None or not:
  ```python
  assert result is None
  assert value is not None
  ```

---

## 9. Custom Validations
- You can use any Python expression with `assert` to validate custom logic:
  ```python
  assert user["age"] > 18 and user["is_active"]
  ```

---

> **Tip:** pytest's assert statements are very flexible—use them to check any condition you expect in your code or API responses!
