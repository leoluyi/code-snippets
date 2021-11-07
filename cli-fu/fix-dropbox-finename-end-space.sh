#!/usr/bin/env bash

# Command Line Fu - sed + find tricks
# https://www.youtube.com/watch?v=CyVV2FI7-DE

command -v fd >/dev/null && \
  fd -HI '\s+[.]\w+$' | sed -E 's/((.+?)\s+[.](\w+)?)$/"\1" "\2.\3"/' | \
  xargs -n 2 mv

command -v fd >/dev/null && \
  fd -HI '^\s+' | sed -E 's#((.+?/)\s+(.+))#"\1" "\2\3"#' | \
  xargs -n 2 mv
