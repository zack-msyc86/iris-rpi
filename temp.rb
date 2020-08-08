require 'json'

def get_temps
  JSON.parse(`python3 ./py/am2302.py`,{:symbolize_names => true})
end

p get_temps
