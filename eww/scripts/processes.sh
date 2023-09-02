#!/bin/bash

cpu() {
  top -b -n1 | grep '^ *[0-9]' | head -n 10 | cut -c 51,52,53,54
}

mem() {
  top -b -n1 | grep '^ *[0-9]' | head -n 10 | cut -c 57,58,59,60
}

comm() {
  top -b -n1 | grep '^ *[0-9]' | head -n 10 | cut -c 72,73,74,75,76,77,78,79,80,81,82
}

usage() {
  eval $(awk '/^cpu0 /{print "previdle=" $5 "; prevtotal=" $2+$3+$4+$5 }' /proc/stat); sleep 0.4; eval $(awk '/^cpu0 /{print "idle=" $5 "; total=" $2+$3+$4+$5 }' /proc/stat); intervaltotal=$((total-${prevtotal:-0})); echo "$((100*( (intervaltotal) - ($idle-${previdle:-0}) ) / (intervaltotal) ))"
}

if [[ "$1" == "--cpu" ]]; then
  cpu
elif [[ "$1" == "--mem" ]]; then
  mem
elif [[ "$1" == "--comm" ]]; then
  comm
elif [[ "$1" == "--usage" ]]; then
  usage
fi
