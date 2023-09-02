#!/bin/lua

--local workspaces = {"\" 󱅊 \"", "\" 󱅋 \"", "\" 󱅌 \"", "\" 󱅍 \"", "\" 󱅎 \"", "\" 󱅏 \"", "\"  \"", "\"  \"", "\"  \"" }
--local workspace = require 'wsicons'


local function getCurWS()
  curWS = os.popen("hyprctl activeWorkspace | grep ID | awk \'{print $3}\'")
  ws = curWS:read('*a')
  print(ws)
end

local function workspace1()
  
  local activeWorkspace = "\"inactive\""

  print( "(label :class " ..activeWorkspace.. " :text \" 󱅊 \")")

end

workspace1()
getCurWS()

