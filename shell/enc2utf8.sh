#!/user/bin/bash

# Reference:
# https://gist.github.com/leoluyi/85b45a3a750fb6f1d8cab0ea8203320d

if [ $# -lt 1]; then
  echo "Usage "$0" <file_name>"
  echo "Convert text files  to UTF-8"
  exit
fi


for i in $*; do

  if [ -f $i ]; then
    encoding=$(chardet $i | cut -d ' ' -f 2)
    if [ "$encoding" == "Big5" ]; then
      encoding="cp950"
    fi
    
    if [ "$encoding" != "utf-8"]; then
      echo "encoding "$i" ("$encoding") to utf-8"
      iconv -f "$encoding" -t utf-8 "$i" > "$i.tmp" &&
      mv -f "$i.tmp" "$i"
      rm -f "$i.tmp"
    else
      echo ""$i" ("$encoding") not modified"
    fi
  fi
  
done
