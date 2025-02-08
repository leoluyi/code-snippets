import sys

print(f"module2 sys.path[0]: {sys.path[0]}")
print(__package__)


def func_2():
    print("func2 runs here ---------------")
