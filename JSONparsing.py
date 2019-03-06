
import json
import urllib.request, urllib.parse, urllib.error, urllib
import ssl

url= 'http://py4e-data.dr-chuck.net/comments_140760.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

info = json.loads(data)
tot = 0
print ('Retrieved ', len(data), 'characters')
print ('Count: ', len(info['comments']))
for i in range(0, len(info['comments'])):
    tot += int(info['comments'][i]['count'])
print ('Sum ', tot)

