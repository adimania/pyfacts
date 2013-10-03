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

def profiler_hardware_datatype():
  data = filter(None, subprocess.Popen(["system_profiler","SPHardwareDataType"], stdout=subprocess.PIPE).communicate()[0].split('\n'))
  data_dict = {}
  for d in data[2:]:
    data_dict[ d.split(':')[0].strip() ] = d.split(':')[1].strip()
  return data_dict

def memory():
  return profiler_hardware_datatype()['Memory']

#def swap():

def cpu_cores():
  return profiler_hardware_datatype()['Total Number of Cores']

#def cpu_threads():
#  return profiler_hardware_datatype()['Memory']
