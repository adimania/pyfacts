import json 
import platform
from types import ModuleType
import sys
import urllib
import urllib2

if platform.system().lower() == 'linux':
  import linux as FactsLib
elif platform.system().lower() == 'darwin':
  import mac as FactsLib
else:
  print "OS not supprted"
  sys.exit(0)

facts={}
for method in dir(FactsLib):
  if method[0] != '_' and type(getattr(FactsLib,method)) is not ModuleType:
    facts[str(method)] = getattr(FactsLib,method)()
print facts
if sys.argv[1]:
  url = sys.argv[1]
  tmp=json.dumps(facts)
  print tmp
  facts_json = urllib.urlencode(facts)
  req = urllib2.Request(url, facts_json)
  response = urllib2.urlopen(req)
  the_page = response.read()
