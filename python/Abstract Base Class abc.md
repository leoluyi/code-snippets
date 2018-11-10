# Python - Abstract Base Class abc.md

- https://dbader.org/blog/abstract-base-classes-in-python
- https://blog.louie.lu/2017/07/28/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-03-abc/

## TL;DR

- the goal was to define a simple class hierarchy for a service backend in the most programmer-friendly and maintainable way.
- instantiating the base class is impossible; and
- forgetting to implement interface methods in one of the subclasses raises an error as early as possible.

```py
from abc import ABCMeta, abstractmethod

class AbstractFoo(metaclass=ABCMeta):

    # Reruired attr or property
    @property
    @abstractmethod
    def required_attr(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Foo(AbstractFoo):

    required_attr = 999  # must implement class attribute here for abc in base class

    def __init__(self, value=None):
        if value:
            '''replace default when value provided'''
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


