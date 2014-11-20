import json 
import os
from types import ModuleType
import sys
import urllib
import urllib2
import datetime

if os.uname()[0].lower() == 'linux':
  import linux as FactsLib
elif os.uname()[0].lower() == 'darwin':
  import osx as FactsLib
elif os.uname()[0].lower() == 'vmkernel':
  import esxi as FactsLib
else:
  print "OS not supprted"
  sys.exit(0)

facts={}
for method in dir(FactsLib):
  if method[0] != '_' and type(getattr(FactsLib,method)) is not ModuleType:
    facts[str(method)] = getattr(FactsLib,method)()
  facts["time"] = str(datetime.datetime.utcnow())
try:
  custom_facts=open('custom_facts')
  for f in custom_facts:
    f = f.split(':')
    facts[f[0]] = f[1]
except:
  pass

try:
  if sys.argv[1]:
    url = sys.argv[1]
    tmp=json.dumps(facts)
    print tmp
    facts_json = urllib.urlencode(facts)
    req = urllib2.Request(url, facts_json)
    response = urllib2.urlopen(req)
    the_page = response.read()
except:
  print json.dumps(facts)
