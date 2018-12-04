# Python - Argparse cheatsheet

- https://gist.github.com/leoluyi/f9acc71cbbec364f4b0310d7b239c1b1
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

## Misc

#### Convert argparse.Namespace() as a dictionary?

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> args = parser.parse_args(['--foo', 'BAR'])
>>> vars(args)   # Return the __dict__ attribute
{'foo': 'BAR'}
```
