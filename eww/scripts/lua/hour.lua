#!/bin/lua

local function hour()
  
  local hour = os.date("%H")
  local cur_hour = (100/24)*hour

  print(tonumber(cur_hour))

end

hour()

