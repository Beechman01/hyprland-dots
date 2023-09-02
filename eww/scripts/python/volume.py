#!/usr/bin/env python3

import subprocess

a = 3

while a < 5:
  get_volume = subprocess.run(["amixer","sget","Master"],capture_output=True, text=True, timeout=0.2)
  split_volume = get_volume.stdout.split(" ")
  volume = split_volume[30]
  vol_text = f"{volume[1]}{volume[2]}{volume[3]}"
  vol_num = int(f"{volume[1]}{volume[2]}")

#print(get_volume.stdout)
#print("<---------------->")
#print(f"{volume[1]}{volume[2]}")
#print("<---------------->")
#print(vol_num)

  print(f"(centerbox :class \"fetch-box\" :vexpand \"true\" :hexpand \"false\" :halign \"center\" :height 10 :width 10 :orientation \"vertical\"",
          f"(scale :class \"scale\" :halign \"center\" :valign \"start\" :height 100 :min 0 :max 100 :orientation \"vertical\" :flipped \"true\" :value {vol_num})",
          f"(label :class \"volume-wid\" :halign \"center\" :valign \"center\" :text {vol_text})",
          f"(label :class \"volume-icon\" :halign \"center\" :valign \"end\" :text \"󰋋\")",
       ")")
