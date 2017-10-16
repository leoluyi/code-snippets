#!/usr/bin/env bash

# ssh -L forward multiple ports
# https://stackoverflow.com/a/43165464/3744499

for i in ${@:2}
do
  echo Forwarding port $i
  ssh -N -L $i:localhost:$i $1 &
done

