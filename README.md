# wigler
 Input a series of wifi SSIDs, receive geolocation


**wigler** bridges the somewhat-tedious analytic gap between using WiGLE to get lat/long coordinates of wifi SSIDs and correlating them; this problem especially presents itself when you have a list of fairly-common SSID names (like "Linksys") and are trying to figure out where on the planet 4-5 of them can see each other at once. Enter **wigler** - instead of having an intern plot out the lat/long coords and then analyzing where your location *likely* is, you can have a poorly-written Python script do it instead! Using the Haversine formula, this script will correlate many SSIDs and show you which ones are within a configurable number of meters from each other, default is half a kilometer.

