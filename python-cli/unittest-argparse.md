# How do you write tests for the argparse portion of a python module?

You should refactor your code and move the parsing to a function:

```python
def parse_args(args):
    parser = argparse.ArgumentParser(...)
    parser.add_argument...
    # ...Create your parser as you like...
    return parser.parse_args(args)
```

Then in your main function you should just call it with:

```python
parser = parse_args(sys.argv[1:])
```

(where the first element of `sys.argv` that represents the script name is removed to not send it as an additional switch during CLI operation.)

In your tests, you can then call the parser function with whatever list of arguments you want to test it with:

```python
def test_parser(self):
    parser = parse_args(['-l', '-m'])
    self.assertTrue(parser.long)
    # ...and so on.
```

This way you'll never have to execute the code of your application just to test the parser.

If you need to change and/or add options to your parser later in your application, then create a factory method:

```python
def create_parser():
    parser = argparse.ArgumentParser(...)
    parser.add_argument...
    # ...Create your parser as you like...
    return parser
```

You can later manipulate it if you want, and a test could look like:

```python
class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_something(self):
        parsed = self.parser.parse_args(['--something', 'test'])
        self.assertEqual(parsed.something, 'test')
```


## References

- https://stackoverflow.com/a/18161115/3744499
