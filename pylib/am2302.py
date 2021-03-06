#!/usr/bin/python
import json
import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print(json.dumps({"temperature": round(temperature, 1), "humidity": round(humidity,1)}))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
