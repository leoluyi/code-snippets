# Speed Up Your Python Program With Concurrency: Code Examples

Corresponding code to the Real Python tutorial, "[Speed up your Python Program with Concurrency](https://realpython.com/python-concurrency/)."

To run the code here, use:

```bash
pipenv install -r requirements.txt
```

This will ensure you have the required packages.

## What Is Concurrency?

- Only multiprocessing actually runs these trains of thought at literally the
  same time.
- Threading and asyncio both run on a single processor and therefore only run
  one at a time. They just cleverly find ways to take turns to speed up the
  overall process.

## What Is Parallelism?

| Concurrency Type                     | Switching Decision                                                    | Number of Processors |
|--------------------------------------|-----------------------------------------------------------------------|----------------------|
| Pre-emptive multitasking (threading) | The operating system decides when to switch tasks external to Python. | 1                    |
| Cooperative multitasking (asyncio)   | The tasks decide when to give up control.                             | 1                    |
| Multiprocessing (multiprocessing)    | The processes all run at the same time on different processors.       | Many                 |

## When Is Concurrency Useful?

| I/O-Bound Process                                                                                                     | CPU-Bound Process                                                                        |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer. | You program spends most of its time doing CPU operations.                                |
| Speeding it up involves overlapping the times spent waiting for these devices.                                        | Speeding it up involves finding ways to do more computations in the same amount of time. |

**IO bound**

![io bound](./img/IOBound.4810a888b457.png)

**CPU bound**

![cpu bound](./img/CPUBound.d2d32cb2626c.png)
