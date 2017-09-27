# PUI2017 HW2: MTA Bus - Assignment 1 - Michael Sampson (mms911)

from __future__ import print_function
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


if len(sys.argv) ==3:
	mtaKey=sys.argv[1]
	busLine=sys.argv[2]
else:
	print("Invalid number of arguments. Run as: python show_bus_locations.py mtaKey busLine")


#http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=YOUR_KEY&VehicleMonitoringDetailLevel=calls&LineRef=B52
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtaKey,busLine)
print(url)

response=urllib.urlopen(url)
dataBus=response.read().decode("utf-8")
dataBus=json.loads(dataBus)

actvVehicles=dataBus["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
busNum=len(actvVehicles)

#print(busNum)

print("Bus Line %s"%(busLine))
print("Number of Active Buses: %i" %(busNum))

for i in range(busNum):
	loc=(actvVehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"])
	print("Bus %i is at latitude %f and longitude %f"%(i+1,loc["Latitude"],loc["Longitude"]))


