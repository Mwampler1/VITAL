# get gps coordinates from geopy
import json
import keyboard
# import urlopen from urllib.request
from urllib.request import urlopen

# open following url to get ipaddress
urlopen("http://ipinfo.io/json")

# load data into array
data = json.load(urlopen("http://ipinfo.io/json"))


#get how far
mode = input('Choose feet or meters (type f or m):\n ')
if keyboard.is_pressed(mode):
	if mode != 'f' or mode != 'm':
		while mode != 'f' or mode != 'm':
			print("Invalid input, please type f or m: ")
			mode = input()

length = input("How far are you from the target? ")
#if (mode == f)
#else if (mode == m)

		


# extract lattitude
lat = data['loc'].split(',')[0]

# extract longitude
lon = data['loc'].split(',')[1]

print(lat, lon)
