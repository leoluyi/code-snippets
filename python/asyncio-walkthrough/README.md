# RealPython - Async IO in Python: A Complete Walkthrough

https://realpython.com/async-io-python/

## Setting Up Your Environment

You'll need Python 3.7 or above to follow this article in its entirety, as well as the `aiohttp` and `aiofiles` packages:

```bash
$ pipenv --python 3.7
$ pipenv shell
$ pip install --upgrade pip aiohttp aiofiles  # Optional: aiodns
```

## Generators vs Coroutines

- Both can be startd, paused, and restarted.
- Generators produce values, Coroutines consume values.
