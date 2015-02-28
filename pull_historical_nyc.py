import urllib2
import json

# Historical data for NYC
f = urllib2.urlopen('http://api.wunderground.com/api/<API_KEY>/history_20100715/q/NY/New_York_City.json')
json_string = f.read()
parsed_json = json.loads(json_string)

# Print all temp readings for day
for m in parsed_json['history']['observations']:
    print m['tempm']
        
f.close()

