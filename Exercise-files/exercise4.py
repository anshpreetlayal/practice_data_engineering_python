import urllib.request
import urllib.parse
import json
import ssl

api_key = False


if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    
    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')
    except:
        print("Failed to retrieve data from the service")
        continue

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    # Extracting the place_id
    place_id = js['results'][0]['place_id']
    print('Place ID:', place_id)
