# Speed Up Your Python Program With Concurrency: Code Examples

Corresponding code to the Real Python tutorial, "[Speed up your Python Program with Concurrency](https://realpython.com/python-concurrency/)."

To run the code here, use:

```bash
pipenv install -r requirements.txt
```

This will ensure you have the required packages.

## What Is Parallelism?

| Concurrency Type                     | Switching Decision                                                    | Number of Processors |
|--------------------------------------|-----------------------------------------------------------------------|----------------------|
| Pre-emptive multitasking (threading) | The operating system decides when to switch tasks external to Python. | 1                    |
| Cooperative multitasking (asyncio)   | The tasks decide when to give up control.                             | 1                    |
| Multiprocessing (multiprocessing)    | The processes all run at the same time on different processors.       | Many                 |

## When Is Concurrency Useful?

**IO bound**

![io bound](.)

**CPU bound**
