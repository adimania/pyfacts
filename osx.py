import re
import subprocess
import socket

def ipaddress():
  p=subprocess.Popen(["/sbin/ifconfig"],stdout=subprocess.PIPE)
  ip=p.communicate()
  pattern=re.compile(r'inet\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  return pattern.findall(ip[0])

def fqdn():
  return socket.gethostname()

