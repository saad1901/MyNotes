# Awaitables

> **Awaitables** are objects that can be used in an `await` expression. Many `asyncio` APIs are designed to accept awaitables.

---

## Types of Awaitable Objects
- **Coroutines**
- **Tasks**
- **Futures**

---

## Coroutines

Python coroutines are awaitables and can be awaited from other coroutines:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()  # will raise a "RuntimeWarning".

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```

> **Note:**
> - A **coroutine function** is an `async def` function.
> - A **coroutine object** is what you get when you call a coroutine function.

---

## Tasks

Tasks are used to schedule coroutines concurrently. When a coroutine is wrapped into a Task with functions like `asyncio.create_task()`, the coroutine is automatically scheduled to run soon:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
```

---

## Futures

A **Future** is a special low-level awaitable object that represents an eventual result of an asynchronous operation.

When a Future object is awaited, the coroutine will wait until the Future is resolved elsewhere. Future objects in `asyncio` are needed to allow callback-based code to be used with `async/await`.

> **Tip:** Normally, there is no need to create Future objects at the application level.

Future objects, sometimes exposed by libraries and some asyncio APIs, can be awaited:

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

A good example of a low-level function that returns a Future object is `loop.run_in_executor()`.