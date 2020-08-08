require 'json'

def get_temps
  JSON.parse(`python3 ./py/am2302.py`).symbolize
end

p get_temps
