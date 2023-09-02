#!/bin/bash

distro() {
  lsb_release -si
}

kernel() {
  uname -r
}

uptime() {
  last reboot -F | head -1 | awk '{print $8}'
}

cpu-name() {
  lscpu | grep 'Model name:' | awk ' {gsub("12-Core Processor","",$3);print $3" "$4" "$5" "$6}'
}

cpu-temp() {
  sensors | grep 'Tctl'| awk ' {gsub(/\+/,"",$2);gsub(/\../,"",$3); print $2} ' 
}

nv-name() {
  nvidia-smi -q --id=00000000:01:00.0 | grep "Product Name" | awk {'print $5" "$6" "$7'}
}

nv-driver() {
  nvidia-smi | grep "Driver Version"| awk {'print $3'}
}

nv-temp() {
  nvidia-settings -q gpucoretemp -t 
}

nv-usage() {
nvidia-smi | grep '%' | awk '{print $13}' 
}


if [[ "$1" == "--distro" ]]; then
  distro
elif [[ "$1" == "--kernel" ]]; then
  kernel
elif [[ "$1" == "--uptime" ]]; then
  uptime
elif [[ "$1" == "--cpu-name" ]]; then
  cpu-name
elif [[ "$1" == "--cpu-temp" ]]; then
  cpu-temp
elif [[ "$1" == "--nv-name" ]]; then
  nv-name
elif [[ "$1" == "--nv-driver" ]]; then
  nv-driver
elif [[ "$1" == "--nv-temp" ]]; then
  nv-temp
elif [[ "$1" == "--nv-usage" ]]; then
  nv-usage
fi
