# asyncio - Common Mistakes Using asyncio

- [Common Mistakes Using Python3 asyncio](https://xinhuang.github.io/posts/2017-07-31-common-mistakes-using-python3-asyncio.html)
- [YouTube - Python tricks: Demystifying async, await, and asyncio](https://www.youtube.com/watch?v=tSLDcRkgTsY)
- [Python tricks: Demystifying async, await, and asyncio](https://osf.io/w8u26/)
- [Morvan - 加速爬蟲: 異步加載 Asyncio](https://morvanzhou.github.io/tutorials/data-manipulation/scraping/4-02-asyncio/)

## TL;DR with asyncio

- The async and await keywords were introduced in Python 3.5.
- They are syntactic sugar on top of the `asyncio` module that was introduced in Python 3.4.
- But generator coroutines can do some of the same things.
- The interfaces of Python3 asyncio is verbose and difficult to use. And the document is somewhat difficult to understand.

### Example

Asynchronous code:

- Runs multiple functions seemingly in parallel
    - In a single process
    - Without threads
- Requires cooporative, well-behaving functions
    - Functions that regularly suspend by awaiting something
- Should not use blocking functions!
    - No time.sleep()
    - No socket.*
    - Etc.
    - asyncio provides non-blocking alternatives for many of these functions `asyncio.sleep(0.01)`

```py
import time
import asyncio


def is_prime(x):
    return not any(x//i == x/i for i in range(x-1, 1, -1))


async def highest_prime_below(x):
    
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('→ Highest prime below %d is %d' % (x, y))
            return y

        # the magic trick to make function really async:
        # hang over the processing time to the event loop
        await asyncio.sleep(0.01)
    return None


async def main():
    
    t0 = time.time()
    await asyncio.wait([
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
    ])
    t1 = time.time()
    print('Took %.2f ms' % (1000*(t1-t0)))

    
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except Exception as e:
    raise e
finally:
    loop.close()
```

### Mistake 1 - RuntimeWarning: coroutine foo was never awaited?

This runtime warning can happen in many scenarios, but the cause are same: A coroutine object is created by the invocation of an async function, but is never inserted into an EventLoop.

Consider following async function foo():

```py
async def foo():
    # a long async operation
    # no value is returned
```

If you want to call foo() as an asynchronous task, and doesn't care about the result:

```py
prepare_for_foo()
foo()                  # RuntimeWarning: coroutine foo was never awaited
remaining_work_not_depends_on_foo()
```

This is because invoking `foo()` doesn't actually runs the function `foo()`, but created a "coroutine object" instead. This "coroutine object" will be executed when current `EventLoop` gets a chance: `awaited/yield` from is called or all previous tasks are finished.

To execute an asynchronous task without await, use `loop.create_task()` with `loop.run_until_complete()`:

```py
prepare_for_foo()
task = loop.create_task(foo())
remaining_work_not_depends_on_foo()
loop.run_until_complete(task)
```

### Mistake 2 - Task was destroyed but it is pending!

The cause of this problem is that the `EventLoop` is closed right after canceling pending tasks. Because the [`Task.cancel()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel) "arranges for a `CancelledError` to be thrown into the wrapped coroutine on the next cycle through the event loop", and "_the coroutine then has a chance to clean up or even deny the request using try/except/finally._"

To correctly cancel all tasks and close `EventLoop`, the `EventLoop` should be given the last chance to run all the canceled, but unfinished tasks.

For example, this is the code to cancel all the tasks:

```py
def cancel_tasks():
    tasks = Task.all_tasks()              # get all task in current loop
    for t in tasks:
        t.cancel()

cancel_tasks()
loop.stop()
```

Below code correctly handle task canceling and clean up. It starts the `EventLoop` by calling `loop.run_forever()`, and cleans up tasks after receiving `loop.stop()`:

```py
try:
    loop.run_forever()                # run_forever() returns after calling loop.stop()
    tasks = Task.all_tasks()
    for t in [t for t in tasks if not (t.done() or t.cancelled())]:
        loop.run_until_complete(t)    # give canceled tasks the last chance to run
finally:
    loop.close()
```

### Mistake 3 - `Task`/`Future` is awaited in a different `EventLoop` than it is created

This error is especially surprising to people who are familiar with C# `async`/`await`. It is because most of `asyncio` is not thread-safe, nor is `asyncio.Future` or `asyncio.Task`. Also don't confuse `asyncio.Future` with `concurrent.futures.Future` because they are not compatible (at least until Python 3.6): the latter is thread-safe while the former is not.

In order to await an `asyncio.Future` in a different thread, `asyncio.Future` can be wrapped in a `concurrent.Future`:

```py
def wrap_future(asyncio_future):
    def done_callback(af, cf):
        try:
            cf.set_result(af.result())
        except Exception as e:
            cf.set_exception(e)

    concur_future = concurrent.Future()
    asyncio_future.add_done_callback(lambda f: done_callback(f, cf=concur_future))
    return concur_future
```

