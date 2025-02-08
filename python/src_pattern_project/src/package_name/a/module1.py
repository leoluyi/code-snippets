import sys

from src.package_name.b.module2 import func_2

print(f"module1 sys.path[0]: {sys.path[0]}")
print(f"__package__: {__package__}")


if __name__ == "__main__":
    func_2()
