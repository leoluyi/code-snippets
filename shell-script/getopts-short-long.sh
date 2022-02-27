#!/usr/bin/env bash
# < https://stackoverflow.com/a/7680682/3744499 >
# < https://stackoverflow.com/a/46793269/3744499 >
set -Eeuo pipefail
_filename=$(basename -- "$0")
_script="${_filename%.*}"

function _usage()
{
  cat >&2 <<EOF
>>>>>>>> $*
Usage:
  _filename <[options]>

Options:
  -f --foo          Set foo to argument
  -b --bar-bar      Set bar to argument
  -o --option       Get option to yes
  -h --help         Show this message
EOF
  exit 2
}

[ $# = 0 ] && _usage "No options given."

need_arg() {
  if [ -z "$2" ] || [[ "$2" = -* ]]; then
    _usage "Option ($1) requires an argument."
  fi
}
no_need_arg() {
  if [ -n "$2" ] && [[ "$2" != -* ]]; then
    _usage "Option ($1) does not suppot an argument."
  fi
}

optspec=":f:b:ohv-:"
while getopts "$optspec" optchar; do
  case "${optchar}" in
    -)
      case "${OPTARG}" in
        foo)
          val="${!OPTIND}"; OPTIND=$(( OPTIND + 1 ))
          need_arg "--$OPTARG" "$val"
          echo "Parsing option: '--${OPTARG}', value: '${val}'" >&2
          ;;
        foo=*)
          val=${OPTARG#*=}
          opt=${OPTARG%="$val"}
          need_arg "--$OPTARG" "$val"
          echo "Parsing option: '--${opt}', value: '${val}'" >&2
          ;;
        bar-bar)
          val="${!OPTIND}"; OPTIND=$(( OPTIND + 1 ))
          need_arg "--$OPTARG" "$val"
          echo "Parsing option: '--${OPTARG}', value: '${val}'" >&2
          ;;
        bar-bar=*)
          val=${OPTARG#*=}
          opt=${OPTARG%="$val"}
          need_arg "--$OPTARG" "$val"
          echo "Parsing option: '--${opt}', value: '${val}'" >&2
          ;;
        option)
          val="${!OPTIND}"
          no_need_arg "--$OPTARG" "$val"
          echo "Parsing option: '--${OPTARG}'" >&2
          ;;
        *)
          if [ "$OPTERR" = 1 ] && [ "${optspec:0:1}" = ":" ]; then
            _usage "Invalid option (--${OPTARG})"
          fi
          ;;
      esac;;
    f) echo "Parsing option: '-${optchar}', value: '${OPTARG}'" >&2 ;;
    b) echo "Parsing option: '-${optchar}', value: '${OPTARG}'" >&2 ;;
    o) echo "Parsing option: '-${optchar}'" >&2 ;;
    v) echo "Parsing option: '-${optchar}'" >&2 ;;
    h) _usage ;;
    :) _usage "Option -$OPTARG requires an argument." ;;
    ?)
      if [ "$OPTERR" != 1 ] || [ "${optspec:0:1}" = ":" ]; then
        _usage "Invalid option (-${OPTARG})"
      fi
      ;;
  esac
done
shift $((OPTIND -1))

if [ -n "$*" ]; then
  echo "--------------------------"
  echo "Positional arguments:"
  echo "$*"
fi

trap 'cleanup $? $LINENO $0' EXIT ERR
cleanup() {
  local rv=$1
  local lineno=$2
  local script=$3

  # housekeeping: temp files
  [ -d "${TMP_DIR}" ] && rm -rf "${TMP_DIR}" || true
  echo "(Exit) temp file removed."

  if [ "$rv" != "0" ] && [ "$lineno" != 1 ]; then
    # error handling
    >&2 echo "$(logger "ERROR" "$script") (Traceback) status_code $rv occurred on $lineno in $script"
    exit "$rv"
  fi
}

logger() {
  local level="$1"
  local prefix
  local message

  case "$level" in
    E*|e*) level=ERROR ;;
    W*|w*) level=WARN ;;
    I*|i*) level=INFO ;;
    D*|d*) level=DEBUG ;;
    *) level=INFO ;;
  esac

  if [ $# -gt 2 ]; then
    prefix=$2
    message="${*:3}"
  else
    prefix=""
    message="${*:2}"
  fi

  if [ -n "$prefix" ]; then
    echo "$(date +%Y-%m-%dT%H:%M:%S) [$level] ($prefix)" "$message"
  else
    echo "$(date +%Y-%m-%dT%H:%M:%S) [$level]" "$message"
  fi
}
