#!/usr/bin/env bash

f=$1
t=$2
ext=$3

for file in *.${ext}; do
    iconv -c -f $f -t $t -o "$file.new" "$file" &&
    mv -f "$file.new" "$file"
done

