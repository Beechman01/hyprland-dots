#!/bin/bash

vol-text() {
  amixer sget Master | awk -F"[][]" '/Left:/ { print $2 }'
}

vol-num() {
  amixer sget Master | awk -F"[][]" '/Left:/ { gsub(/["%"]/,"",$2); print $2 }' 
}

if [[ "$1" == "--text" ]]; then 
  vol-text
elif [[ "$1" == "--num" ]]; then
  vol-num
fi 
