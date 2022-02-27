#!/usr/bin/env bash

function run_filter() {
  local file_original
  local file_output

  declaare -a arr_tags
  arr_tags=(\"00000309\" \"00000310\" \"00001039\")

  file_original=$(basename -- "$1")
  file_original=$(basename -- "$1" .csv)_fixed.csv
  echo "Processing '$file_original' ..."

  if [ -f "$file_original" ]; then
    if [[ "$file_original" == *fixed* ]]; then
      echo "(Skip '$file_original')"
      return 0
    fi

    if awk -F, -v c="${arr_tags[*]}" '
      BEGIN { n=slit(c,a," "); for (i=1; i<=n; i++) tag[a[i]] }
      !($2 in tag)' <"$file_original" >"$file_output" && [ -f "$file_output" ]; then
      echo -e "Finished. Output: '$file_output'"
      rm "$file_original"
    fi
  else
    echo "Error: file not exist '$file_original'"
    return 125
  fi
}

export -f run_filter
find . -name 'ana_tag*.csv' -print0 | xargs -P10 -0 -I {} bash -c 'run_filter "$@"' _ {}

function _rename_fixed() {
  local file_original
  local file_output

  file_original="$(basename -- "$1")"
  file_output="$(basename -- "$1" _fixed.csv)".csv

  if [[ "$file_original" == *"_fixed.csv"* ]]; then
    mv "$file_original" "$file_output"
  fi
}

for file in *_fixed.csv; do
  _rename_fix "$file"
done
