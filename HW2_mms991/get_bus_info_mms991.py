# PUI2017 HW2: MTA Bus - Assignment 1 - Michael Sampson (mms911)

from __future__ import print_function
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


if len(sys.argv) ==4:
	mtaKey= sys.argv[1]
	busLine= sys.argv[2]
	csvfile= sys.argv[3]
else:
	print("Invalid number of arguments. Run as: python show_bus_locations.py mtaKey busLine busline.csv")

#http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=YOUR_KEY&VehicleMonitoringDetailLevel=calls&LineRef=B52
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtaKey,busLine)
print(url)

response=urllib.urlopen(url)
dataBus=response.read().decode("utf-8")
dataBus=json.loads(dataBus)

actvVehicles=dataBus["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
busNum=len(actvVehicles)

print('Bus Line: ', busLine)
print('Number of Active Buses: ', actvVehicles)

fout = open(csvfile, "w")
fout.write('Latitude,Longitude,Stop Name,Stop Status\n')

for i in range(0,actvVehicles):
    loc=(actvVehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"])
	print("Bus %i is at latitude %f and longitude %f"%(i+1,loc["Latitude"],loc["Longitude"]))
    if len(dataBus['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']) == 0:
        StopName = 'N/A'
    else:
        StopName = dataBus['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    if len(dataBus['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']) == 0:
       StopStatus = 'N/A'
    else:
       StopStatus = dataBus['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']


    fout.write('{},{},{},{}\n'.format(Lat,Long,StopName,StopStatus))