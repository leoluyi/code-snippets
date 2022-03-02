#!/usr/bin/env bash

# < https://stackoverflow.com/a/23357277 >
# < https://stackoverflow.com/a/30988704/3744499 >
# < https://www.computerhope.com/unix/bash/read.htm >
# < https://www.baeldung.com/linux/read-command >

# for 4.4-alpha or later
# ------------------------
# Use Bash's builtin mapfile (or its synonym readarray) and process substitution:
mapfile -t -s 1 myarr < <(ps -u myusername | awk '{print $1}')
readarray -d '' array < <(find . -name "pattern" -print0)
# for a method that works with arbitrary filenames including blanks, newlines,
# and globbing characters.


# for bash 4.3 or earlier
# ------------------------
array=()
while IFS= read -r line; do array+=("$line"); done < <(mycommand)
while IFS= read -r line; do echo ">>$line<<"; done < file.txt
#> To preserve white space at the beginning or the end of a line, it's common to
#  specify IFS= (with no value) to prevent from field splitting.
#> Default -d param for `read` is $'\n'. Use '' ($'\0') to define
#  null-separated lines for loop.

# e.g. creating an array from find result:
while IFS=  read -r -d '' line; do
  array+=("$line")
done < <(find . -name "pattern" -print0)


# (Don't do this)
# ------------------------
# If you are doing unquoted command expansion in an array. This will invoke the
# shell's sloppy word splitting and glob expansion.
myarr=( $(ps -u myusername | awk '{ print $1 }') )
