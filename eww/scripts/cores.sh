#!/bin/bash


cpu0() {
  eval $(awk '/^cpu0 /{print "previdle=" $5 "; prevtotal=" $2+$3+$4+$5 }' /proc/stat); sleep 0.4; eval $(awk '/^cpu0 /{print "idle=" $5 "; total=" $2+$3+$4+$5 }' /proc/stat); intervaltotal=$((total-${prevtotal:-0})); echo "$((100*( (intervaltotal) - ($idle-${previdle:-0}) ) / (intervaltotal) ))"
}

cpu0() {
  eval $(awk '/^cpu1 /{print "previdle=" $5 "; prevtotal=" $2+$3+$4+$5 }' /proc/stat); sleep 0.4; eval $(awk '/^cpu1 /{print "idle=" $5 "; total=" $2+$3+$4+$5 }' /proc/stat); intervaltotal=$((total-${prevtotal:-0})); echo "$((100*( (intervaltotal) - ($idle-${previdle:-0}) ) / (intervaltotal) ))"
}

if [[ "$1" == "--cpu0" ]]; then
  cpu0
elif [[ "$1" == "--mem" ]]; then
  mem
elif [[ "$1" == "--comm" ]]; then
  comm
elif [[ "$1" == "--usage" ]]; then
  usage
fi
