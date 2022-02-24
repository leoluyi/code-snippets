#!/usr/bin/env bash
# < https://stackoverflow.com/a/7680682/3744499 >
# < https://stackoverflow.com/a/46793269/3744499 >

function _usage()
{
  cat >&2 <<EOF
$*
Usage: $0 <[options]>

Options:
  -b --bar          Set bar to argument
  -f --foo          Set foo to argument
  -o --option       Get option to yes
  -h --help         Show this message
EOF
  exit 2
}

optspec=":f:b:ohv-:"
while getopts "$optspec" optchar; do
  case "${optchar}" in
    -)
      case "${OPTARG}" in
        foo)
          val="${!OPTIND}"; OPTIND=$(( OPTIND + 1 ))
          { [ -z "$val" ] || [[ "$val" = -* ]] ; } && _usage "Option -$OPTARG requires an argument."
          echo "Parsing option: '--${OPTARG}', value: '${val}'" >&2
          ;;
        foo=*)
          val=${OPTARG#*=}
          opt=${OPTARG%="$val"}
          { [ -z "$val" ] || [[ "$val" = -* ]] ; } && _usage "Option -$OPTARG requires an argument."
          echo "Parsing option: '--${opt}', value: '${val}'" >&2
          ;;
        bar)
          val="${!OPTIND}"; OPTIND=$(( OPTIND + 1 ))
          { [ -z "$val" ] || [[ "$val" = -* ]] ; } && _usage "Option -$OPTARG requires an argument."
          echo "Parsing option: '--${OPTARG}', value: '${val}'" >&2
          ;;
        bar=*)
          val=${OPTARG#*=}
          opt=${OPTARG%="$val"}
          { [ -z "$val" ] || [[ "$val" = -* ]] ; } && _usage "Option -$OPTARG requires an argument."
          echo "Parsing option: '--${opt}', value: '${val}'" >&2
          ;;
        option)
          echo "Parsing option: '--${OPTARG}'" >&2
          ;;
        *)
          if [ "$OPTERR" = 1 ] && [ "${optspec:0:1}" != ":" ]; then
            _usage ">>>>>>>> Invalid option (--${OPTARG})"
          fi
          ;;
      esac;;
    f)
      echo "Parsing option: '-${optchar}', value: '${OPTARG}'" >&2
      ;;
    b)
      echo "Parsing option: '-${optchar}', value: '${OPTARG}'" >&2
      ;;
    o)
      echo "Parsing option: '-${optchar}'" >&2
      ;;
    v)
      echo "Parsing option: '-${optchar}'" >&2
      ;;
    h) _usage ;;
    :) _usage "Option -$OPTARG requires an argument." ;;
    ?)
      if [ "$OPTERR" != 1 ] || [ "${optspec:0:1}" = ":" ]; then
        _usage ">>>>>>>> Invalid option (-${OPTARG})"
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
