#!/bin/lua

local function second()
  
  local second = os.date("%S")
  local cur_second = (100/60)*second

  print(tonumber(cur_second))

end

second()

