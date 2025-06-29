# Integration Testing in Python

## What is Integration Testing?
- Integration testing checks how different parts (modules, components, or services) of your application work together.
- It goes beyond unit testing by verifying that combined units interact correctly.

---

## Why Integration Test?
- Catches bugs that occur when components interact.
- Ensures that your app works as a whole, not just in isolated pieces.
- Helps find issues with database access, API calls, or external services.

---

## Integration Testing in FastAPI
- Use `TestClient` from FastAPI (built on `requests`) to simulate real HTTP requests to your API.
- Can use a test database to avoid affecting real data.

---

## Example: FastAPI Integration Test
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

---

## Best Practices
- Use a separate test database or mock services.
- Clean up test data after each test.
- Test both success and failure scenarios.

> **Tip:** Integration tests are slower than unit tests but are essential for confidence that your app works end-to-end.
