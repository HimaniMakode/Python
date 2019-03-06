import urllib.request, urllib.parse, urllib.error, urllib
import xml.etree.ElementTree as ET
import ssl


url = 'http://py4e-data.dr-chuck.net/comments_140759.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0
for count in counts:
    total += int(count.text)

print ('total: ', total)

