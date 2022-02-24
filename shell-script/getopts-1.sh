#!/usr/bin/env bash

MY_BOOL_VAR=0
MY_OTHER_VAR="nothing"

usage() {
  cat >&2 <<EOOPTS
  $(basename $0) [OPTIONS] <required_arg> [<other_arg> ...]

  required_arg: This argument is required and the script will fail if it's
  missing!

  OPTIONS:
  -h:         Print this help message
  -m:         My bool flag. Enable whatever this boolean flag enables

  -M <M>:     Set this other variable to <M>. Default: ${MY_OTHER_VAR}
EOOPTS
}

while getopts "hmM:" opt; do
  case $opt in
    h)
      usage
      exit 0
      ;;
    m)
      MY_BOOL_VAR1=1
      ;;
    M)
      MY_OTHER_VAR=$OPTARG
      ;;
    *)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

shift "$((OPTIND - 1))"

REQUIRED_ARG=$1

if [ -z "${REQUIRED_ARG}" ]; then
  echo "Missing required_arg" >&2
  usage
  exit 1
fi

shift 1

echo "REQUIRED ARG: $REQUIRED_ARG" >&2
echo "ALL OTHER ARGS: $*" >&2
