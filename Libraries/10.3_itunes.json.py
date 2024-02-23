# to traget a specific data from the output, to be specific to get the results from the key 
# filtering out all the track songs of weezer and results for 50 track songs from the webiste
import json
import requests
import sys

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])