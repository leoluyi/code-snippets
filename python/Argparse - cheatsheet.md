# Python - Argparse cheatsheet

- https://gist.github.com/drmalex07/9995807

## TL;DR

+ Arg Name or Optional Flags:
    - `positional`  : str       = `"foo"`
    - `options`     : str       = `"-f", "--foo"`
+ Standard:
    - `action`      : str       = `[store], append, store_true, store_false, store_const, append_const, version`
    - `default`     : *         = `[None]`
    - `type`        : callable  = [str], argparse.FileType(mode='wb', bufsize=0)
+ Exotic:
    - `const`       : *         = `[None]`
        - Value to `action="store_const"` or `action="append_const"`
    - `choices`     : indexable = `[None]`
        - Allowed values.
        - ex: 
            
            ```
            parser.add_argument( "-f", type=int, choices=(1,2,3) )
            ```

    - `nargs`
        - `int`       # require exactly N args
        - `'?'`       # default if opt is missing; const if opt is present; value if supplied with opt
        - `'*'`       # gather any args (after the opt, or positional)
        - `'+'`       # require 1+ and gather
        - ex (`int`):

            ```
            parser.add_argument("-p", type="float", nargs=3, dest="point")
            $ feh.py -p 1 -3.5 4 ==> options.point = (1.0, -3.5, 4.0)
            ```

        - ex (optional stdio):

            ```
            parser.add_argument('infile',  nargs='?', type=argparse.FileType('r'), default=sys.stdin)
            parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
            ```

    - `dest`        : str       = `[inferred]`
    - `required`    : bool      = `[False]`
    - `metavar`     : str       = `[inferred from name: "--foo-bar" -> "foo_bar"]` A name for the argument in usage messages.
    - `help`        : str       = `[None]`
        - `Specifiers`: `%(prog)s`, and the keyword args here: 
        - eg: `%(default)s`, `%(metavar)s`, `%(type.__name__)s`
    - `action`      : callable
        - ex:

            ```
            class FooAction(argparse.Action):
                def __call__(self, parser, namespace, values, option_string=None):
                    print '%r %r %r' % (namespace, values, option_string)
                    setattr(namespace, self.dest, values)
            ```

Usage:

```py
import argparse
parser = argparse.ArgumentParser(
    description         = "can use %(default)s %(prog)s"
    epilog              = ''
    prog                = sys.argv[0]
    usage               = (generated)
    add_help            = True
    argument_default    = None
    parents             = None
    prefix_chars        = '-'
    conflict_handler    = None
    formatter_class     = 
)

parser.add_argument('--version', action='version', version='%(prog)s 2.0')
parser.add_argument(name_or_flags[, ...], attr=value, ...)

parser.set_defaults(arg=value)
args = parser.parse_args()
```

#### What are the entry args taken?

`parser.parse_args(args=None, namespace=None)`

When `args` is `None`, the default is taken from `sys.argv[1:]`.

```
parser.parse_args(['--sum', '7', '-1', '42'])
```

## argparse-example-1

A typical example of Python's argparse combined with configparser. 

> The preferred order is to (1) have a set of hardcoded configuration parameters in the code, which will first get overwritten by (2) config.ini file and (3) finally the command line arguments have the highest priority and they will overwrite whatever has been specified. You are missing the hardcoded configuration parameter data.

```py
import os
import logging
import argparse
import ConfigParser as configparser

# Declare expected command-line arguments

argp = argparse.ArgumentParser()

# Add positional arguments (many)
argp.add_argument("inputs", metavar='INFILE', type=str, nargs='+',
                  help='Provide input logs to parse and load into database')
# Add an optional string argument 'config' 
argp.add_argument("-c", "--config", dest='config_file', default='config.ini',
                   type=str)
# Add a optional switch (boolean optional argument)
argp.add_argument("-v", "--verbose", dest='verbose', default=False,
                  action='store_true', help='Be verbose')
# Add config for logging
argp.add_argument(
    '-l',
    '--log',
    help    = "Set logging level",
    choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    nargs   = '?',
    dest    = "logging_level",
    const   = "INFO",
    default = DefaultConfiguration['DEFAULT']['LogLevel'],
    type    = str.upper
)

# Parse a config ini-style file
here = os.path.realpath('.')

config_file = args.config_file
logging.info(f'Reading configuration from {config_file}')
config = configparser.ConfigParser(defaults = {'here': here})
config.read(args.config_file)

# Parse command line    
args = argp.parse_args()

# Do something with them
if args.verbose:
    args.logging_level = 'DEBUG'
    logging.info('Will produce verbose output')

syslog.setLevel(args.loggingLevel)

sqla_url = config.get('main', 'sqlalchemy_url')
```

---

## Misc

### Convert argparse.Namespace() to a dictionary?

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> args = parser.parse_args(['--foo', 'BAR'])
>>> 
>>> vars(args)   # Return the __dict__ attribute
{'foo': 'BAR'}
```

### Option for passing a list as option?

https://stackoverflow.com/questions/15753701/argparse-option-for-passing-a-list-as-option

**TL;DR**

Use the `nargs` option or the `'append'` setting of the `action` option (depending on how you want the user interface to behave).

**nargs**

```python
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
# Use like:
# python arg.py -l 1234 2345 3456 4567
```

`nargs='+'` takes 1 or more arguments, `nargs='*'` takes zero or more.

**append**

```python
parser.add_argument('-l','--list', action='append', help='<Required> Set flag', required=True)
# Use like:
# python arg.py -l 1234 -l 2345 -l 3456 -l 4567
```

With `append` you provide the option multiple times to build up the list.

**Don't use `type=list`!!!** - There is probably no situation where you would want to use `type=list` with `argparse`. Ever.

Let's take a look in more detail at some of the different ways one might try to do this, and the end result.


```python
import argparse

parser = argparse.ArgumentParser()

# By default it will fail with multiple arguments.
parser.add_argument('--default')

# Telling the type to be a list will also fail for multiple arguments,
# but give incorrect results for a single argument.
parser.add_argument('--list-type', type=list)

# This will allow you to provide multiple arguments, but you will get
# a list of lists which is not desired.
parser.add_argument('--list-type-nargs', type=list, nargs='+')

# This is the correct way to handle accepting multiple arguments.
# '+' == 1 or more.
# '*' == 0 or more.
# '?' == 0 or 1.
# An int is an explicit number of arguments to accept.
parser.add_argument('--nargs', nargs='+')

# To make the input integers
parser.add_argument('--nargs-int-type', nargs='+', type=int)

# An alternate way to accept multiple inputs, but you must
# provide the flag once per input. Of course, you can use
# type=int here if you want.
parser.add_argument('--append-action', action='append')

# To show the results of the given option to screen.
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        print(value)
```

Here is the output you can expect:

```shell
$ python arg.py --default 1234 2345 3456 4567
...
arg.py: error: unrecognized arguments: 2345 3456 4567

$ python arg.py --list-type 1234 2345 3456 4567
...
arg.py: error: unrecognized arguments: 2345 3456 4567

$ # Quotes won't help here... 
$ python arg.py --list-type "1234 2345 3456 4567"
['1', '2', '3', '4', ' ', '2', '3', '4', '5', ' ', '3', '4', '5', '6', ' ', '4', '5', '6', '7']

$ python arg.py --list-type-nargs 1234 2345 3456 4567
[['1', '2', '3', '4'], ['2', '3', '4', '5'], ['3', '4', '5', '6'], ['4', '5', '6', '7']]

$ python arg.py --nargs 1234 2345 3456 4567
['1234', '2345', '3456', '4567']

$ python arg.py --nargs-int-type 1234 2345 3456 4567
[1234, 2345, 3456, 4567]

$ # Negative numbers are handled perfectly fine out of the box.
$ python arg.py --nargs-int-type -1234 2345 -3456 4567
[-1234, 2345, -3456, 4567]

$ python arg.py --append-action 1234 --append-action 2345 --append-action 3456 --append-action 4567
['1234', '2345', '3456', '4567']
```

*Takeaways*:

 - Use `nargs` or `action='append'`
   - `nargs` can be more straightforward from a user perspective, but it can be unintuitive if there are positional arguments because `argparse` can't tell what should be a positional argument and what belongs to the `nargs`; if you have positional arguments then `action='append'` may end up being a better choice.
   - The above is only true if `nargs` is given `'*'`, `'+'`, or `'?'`. If you provide an integer number (such as `4`) then there will be no problem mixing options with `nargs` and positional arguments because `argparse` will know exactly how many values to expect for the option.
 - Don't use quotes on the command line[^1]
 - Don't use `type=list`, as it will return a list of lists
   - This happens because under the hood `argparse` uses the value of `type` to coerce *each individual given argument* you your chosen `type`, not the aggregate of all arguments.
   - You can use `type=int` (or whatever) to get a list of ints (or whatever)


[^1]: I don't mean in general.. I mean using quotes to *pass a list to `argparse`* is not what you want.
