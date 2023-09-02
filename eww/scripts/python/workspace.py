#!/usr/bin/env python3

#wsIcons = (0,"\" 󱅊 \"", "\" 󱅋 \"", "\" 󱅌 \"", "\" 󱅍 \"", "\" 󱅎 \"", "\" 󱅏 \"", "\"  \"", "\"  \"", "\"  \"")

from wsicons import wsIcons
import subprocess

a = 5

while a == 5: 
  getWS = subprocess.run(["hyprctl", "activeworkspace"], capture_output=True, text=True, timeout=0.2) #| grep ID | awk \'{print $3}\'"])
  WS = [int(i) for i in getWS.stdout.split() if i.isdigit()]


  if WS[0] == 1:
    ws1 = "\"active\""
  else:
    ws1 = "\"inactive\""   

  if WS[0] == 2:
    ws2 = "\"active\""
  else:
    ws2 = "\"inactive\""   

  if WS[0] == 3:
    ws3 = "\"active\""
  else:
    ws3 = "\"inactive\""   

  if WS[0] == 4:
    ws4 = "\"active\""
  else:
    ws4 = "\"inactive\""   

  if WS[0] == 5:
    ws5 = "\"active\""
  else:
    ws5 = "\"inactive\""   

  if WS[0] == 6:
    ws6 = "\"active\""
  else:
    ws6 = "\"inactive\""   

  if WS[0] == 7:
    ws7 = "\"active\""
  else:
    ws7 = "\"inactive\""   

  if WS[0] == 8:
    ws8 = "\"active\""
  else:
    ws8 = "\"inactive\""   

  if WS[0] == 9:
    ws9 = "\"active\""
  else:
    ws9 = "\"inactive\""   


  print(
    "(box :class \"ws\" :vexpand \"false\" :hexpand \"false\" :halign \"center\" :height 100 :width 20 :orientation \"vertical\"",
      f"(label :class {ws1} :text {wsIcons[1]})",
      f"(label :class {ws2} :text {wsIcons[2]})",
      f"(label :class {ws3} :text {wsIcons[3]})",
      f"(label :class {ws4} :text {wsIcons[4]})",
      f"(label :class {ws5} :text {wsIcons[5]})",
      f"(label :class {ws6} :text {wsIcons[6]})",
      f"(label :class {ws7} :text {wsIcons[7]})",
      f"(label :class {ws8} :text {wsIcons[8]})",
      f"(label :class {ws9} :text {wsIcons[9]})",
     ")"
  )
print(WS)
