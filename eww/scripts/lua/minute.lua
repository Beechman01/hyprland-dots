#!/bin/lua

local function minute()
  
  local minute = os.date("%M")
  local cur_minute = (100/60)*minute

  print(print(cur_minute))

end

minute()

