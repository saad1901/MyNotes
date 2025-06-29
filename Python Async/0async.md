Async and Await in Python
=========================

Python's `async` and `await` keywords are used to write asynchronous, non-blocking code. They are most commonly used with I/O-bound operations, such as network requests, file I/O, or database queries, where waiting for a response would otherwise block the program.

## Why Use Async/Await?
- **Concurrency**: Run multiple tasks seemingly at the same time.
- **Efficiency**: Free up the program to do other work while waiting for I/O.
- **Simplicity**: Write asynchronous code that looks like synchronous code.

## Key Concepts
- **Coroutine**: A special function defined with `async def` that can be paused and resumed.
- **Event Loop**: The core of every async application. It runs asynchronous tasks and callbacks.
- **Awaitable**: An object that can be awaited using `await` (usually a coroutine or an object with `__await__`).

## Basic Syntax

```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```

- `async def main()`: Defines a coroutine.
- `await asyncio.sleep(1)`: Pauses the coroutine for 1 second without blocking the event loop.
- `asyncio.run(main())`: Runs the coroutine.

## Example: Running Multiple Tasks Concurrently

```python
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    await task1
    await task2

asyncio.run(main())
```

**Output:**
```
hello
world
```

## Example: Gathering Results

```python
import asyncio

async def fetch_data(x):
    await asyncio.sleep(1)
    return x * 2

async def main():
    results = await asyncio.gather(fetch_data(1), fetch_data(2), fetch_data(3))
    print(results)

asyncio.run(main())
```

**Output:**
```
[2, 4, 6]
```

## Notes
- Use `await` only inside `async def` functions.
- Blocking operations (like time.sleep) should be replaced with their async equivalents (like asyncio.sleep).
- Exceptions in coroutines can be caught with try/except as usual.

## When to Use Async/Await
- Network requests (HTTP, database, etc.)
- File I/O
- High-concurrency applications (web servers, bots)

## When Not to Use
- CPU-bound tasks (use multiprocessing or threading instead)
- Simple scripts with no I/O

---
**References:**
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python: Async IO in Python](https://realpython.com/async-io-python/)

