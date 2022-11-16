# wigler
 Input a series of wifi SSIDs, receive geolocation.


**wigler** bridges the somewhat-tedious analytic gap between using WiGLE to get lat/long coordinates of wifi SSIDs and correlating them; this problem especially presents itself when you have a list of fairly-common SSID names (like "Linksys") and are trying to figure out where on the planet 4-5 of them can see each other at once. Enter **wigler** - instead of having an intern plot out the lat/long coords and then analyzing where your location *likely* is, you can have a poorly-written Python script do it instead! Using the Haversine formula, this script will correlate many SSIDs and show you which ones are within a configurable number of meters from each other, default is half a kilometer.

# Requirements

- Python 3
- pygle Python package, set up with your WiGLE key in the config (https://pypi.org/project/pygle/)
- WiGLE Commercial account if you're getting rate-limited (https://wigle.net/commercial)


# Usage
1.) Edit the 'ssids' var at the top of wigler.py to reflect the wireless networks you'd like to search

2.) Tweak the 'successDistance' var at the top if you'd like to increase/decrease the radius of the search, in meters

3.) Run wigler.py

# Tanium Saved Question
If you have Tanium deployed in your enterprise, you can use that to conduct SSID surveying for you - just set up the 'SSID Tanium Question.txt' as a Saved Question that runs at some recurring interval, and then use Connect to drop it into your SIEM. 

# Rate Limiting
Some attendees of the Converge 2022 conference told me after my presentation that they were being rate-limited by WiGLE. This is likely because a bunch of people downloaded this script and ran queries coming from the same hotel IP. You'll want to consider the WiGLE commercial option (linked above) to get around rate-limiting, which is .013 cents per query. 


# Thanks
Thanks to Nathan Rooy who described using the Haversine formula in Python: https://nathanrooy.github.io/posts/2016-09-07/haversine-with-python/

