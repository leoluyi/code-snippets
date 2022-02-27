#!/usr/bin/env bash

# < https://stackoverflow.com/a/2705678/3744499 >

KEYWORD="The Keyword You Need"
REPLACE="<funny characters here>"

ESCAPED_KEYWORD=$(printf '%s\n' "$KEYWORD" | sed -e 's/[]\/$*.^[]/\\&/g');
ESCAPED_REPLACE=$(printf '%s\n' "$REPLACE" | sed -e 's/[\/&]/\\&/g')
# Remember, if you use a character other than / as delimiter, you need replace
# the slash in the expressions above wih the character you are using.

# Now you can use it inside the original sed statement to replace text
sed "s/ESCAPED_KEYWORD/$ESCAPED_REPLACE/g"
