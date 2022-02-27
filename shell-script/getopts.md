# Different versions of getopt(s)

There are three implementations that may be considered:

- Bash builtin `getopts`. This does not support long option names with the
  double-dash prefix. It only supports single-character options.
- BSD UNIX implementation of standalone `getopt` command (which is what MacOS
  uses). This does not support long options either.
- GNU implementation of standalone `getopt`. GNU getopt(3) (used by the
  command-line getopt(1) on Linux) supports parsing long options.

## References

- [Small getopts tutorial [Bash Hackers Wiki]](https://wiki.bash-hackers.org/howto/getopts_tutorial)
- [bash - Using getopts to process long and short command line options - Stack Overflow](https://stackoverflow.com/a/402410/3744499)
- [shell - parse - getopt long example - Code Examples](https://code-examples.net/en/q/623c9)
