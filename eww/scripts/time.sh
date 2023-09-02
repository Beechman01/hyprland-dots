#!/bin/bash

clock_time(){
  date "+%H:%M:%S"
}

clock_date(){
  date "+%A, %B %d, %Y"
}

hour(){
  cur_hour = $(date "+%H")
  hour_perc = $(($((100/24))*cur_hour))

  echo $hour_perc
}

minute(){
  date "+%M"
}

second(){
  date "+%S"
}

if [[ "$1" == "--time" ]]; then
  clock_time
elif [[ "$1" == "--date" ]]; then
  clock_date
elif [[ "$1" == "--hour" ]]; then
  hour
elif [[ "$1" == "--minute" ]]; then
  minute
elif [[ "$1" == "--second" ]]; then
  second
fi
