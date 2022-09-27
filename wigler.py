from pygle import network
import time
import math

ssids = ['netgear', 'starbucks', 'arris'] # The SSIDs to iterate through
successDistance = 500 # How close, in meters, the SSIDs must be to each other 

def geolocate():
    """Locate SSID geocoords within a given list of SSIDs
    """
    locatedSSID = []
    lats = []
    longs = []
    successes = ["SSIDs within " + str(successDistance) + " meters"]
    fails = ["SSIDs NOT within " + str(successDistance) + " meters "]	
    for ssid in ssids:
        print("Now enumerating SSID locations from WiGLE for:", ssid)
        lat, lng = wigle_search_ssids(ssid)  # Obtain lat/long from our array of SSIDs
        if lat and lng:
          for res in range(len(lat)):
            locatedSSID.append(ssid)
            lats.append(lat[res])
            longs.append(lng[res])
            #print ("FOUND " + ssid + " at lat/long " + str(lat[res]) + "," + str(lng[res]))
        time.sleep(0.1)
    if locatedSSID and lats and longs:	
		
        for n in range(len(locatedSSID)): #Outer loop. It iterates through all of the SSIDs and geo-coords in our list
          #print ("N is " + str(n) + " and " + locatedSSID[n] + " " + str(lats[n]) + "," + str(longs[n]))
          if n < len(locatedSSID):
            for x in range((n+1), (len(locatedSSID))): #Inner loop iterates through n+1 elements of the SSIDs and compares them to the original
              #print ("X is " + str(x) + " and " + locatedSSID[x] + " " + str(lats[x]) + "," + str(longs[x]))
              if locatedSSID[n] != locatedSSID[x]:
                 haversineDistance = Haversine([lats[n],longs[n]],[lats[x],longs[x]])
                 if (haversineDistance <= successDistance):
                   successes.append("Distance between SSID " + locatedSSID[n] + " [" + str(lats[n]) + "," + str(longs[n]) + "] and of SSID " + locatedSSID[x] + " [" + str(lats[x]) + "," + str(longs[x]) + "] is " + str(haversineDistance) + " meters")
                 else:  
                   fails.append("Distance between SSID " + locatedSSID[n] + " [" + str(lats[n]) + "," + str(longs[n]) + "] and of SSID " + locatedSSID[x] + " [" + str(lats[x]) + "," + str(longs[x]) + "] is " + str(haversineDistance) + " meters")
        return successes, fails
    else:
        return ["No geolocation possible", ""]



def wigle_search_ssids(ssidToProcess):
    """Search WiGLE for a SSID and return lat/lng.
    """
    results = network.search(ssid=ssidToProcess)
	
    if results['success'] and results['resultCount']:
        lat = []
        lng = []
        for res in results['results']:
           if res['trilat'] and res['trilong']:     #I don't _think_ WiGLE will return a lat without a long, but we'd better check anyway
             lat.append(res['trilat'])
             lng.append(res['trilong'])	
    else:
        print("WiGLE returned no hits for this SSID!")
        lat, lng = None, None
    return lat, lng
	
def Haversine(coord1,coord2): # From https://nathanrooy.github.io/posts/2016-09-07/haversine-with-python/

        lon1,lat1=coord1
        lon2,lat2=coord2
        
        R=6371000                               # radius of Earth in meters. Don't touch this unless the earth changes size
        phi_1=math.radians(lat1)                # in fact, don't change this entire section unless you're a mathematician 
        phi_2=math.radians(lat2)

        delta_phi=math.radians(lat2-lat1)
        delta_lambda=math.radians(lon2-lon1)

        a=math.sin(delta_phi/2.0)**2+\
           math.cos(phi_1)*math.cos(phi_2)*\
           math.sin(delta_lambda/2.0)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        
        return R*c                         # output distance in meters

	
if __name__ == "__main__":
    print("Starting Up WiGLEr!")
    for g in geolocate():
       print(*g, sep='\n')