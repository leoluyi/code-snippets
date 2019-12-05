# Python - Abstract Base Class abc.md

- https://docs.python.org/3/library/abc.html
- [dbader - abstract-base-classes-in-python](https://dbader.org/blog/abstract-base-classes-in-python)
- [你所不知道的-python-標準函式庫用法-03-abc](https://blog.louie.lu/2017/07/28/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-03-abc/)

## TL;DR

Goals:

- To enforce that a derived class implements a number of methods from the base class.
- To define a simple class hierarchy for a service backend in the most programmer-friendly and maintainable way.
- Forgetting to implement interface methods in one of the subclasses raises an error as early as possible.

Python idiom - raises `NotImplementedError` **after** methods are called:

```
class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'
```

Use ABC - raises an error as early as possible

```py
from abc import ABCMeta, ABC, abstractmethod


class MyABC(metaclass=ABCMeta):
    pass


# More convenient way:
class AbstractFoo(ABC):

    # Reruired attr or property
    @property
    @abstractmethod
    def required_attr(self):
        pass

    # Required method
    @abstractmethod
    def bar(self):
        pass


class Foo(AbstractFoo):

    required_attr = 999  # must implement attribute or property here

    def __init__(self, value=None):
        if value:
            '''replace default required_attr when value provided'''
            self.required_attr = value

    def bar():
        pass


class FooNobar(AbstractFoo):
    # We forget to declare bar()
    pass


def main():
    foo = Foo()
    foofoo = Foo(7777)
    print(foo.required_attr)
    print(foofoo.required_attr)

    try:
        foo_no_bar = FooNobar()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
```

Different types of methods:

```python
from abc import ABC

class C(ABC):
    @abstractmethod
    def my_abstract_method(self, ...):
        ...
    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls, ...):
        ...
    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(...):
        ...

    @property
    @abstractmethod
    def my_abstract_property(self):
        ...
    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):
        ...
```
