require 'json'

def get_temp
  p JSON.parse(`python3 ./py/am2302.py`)
end

get_temp
