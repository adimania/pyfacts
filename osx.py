import re
import subprocess
import socket

def ipaddress():
  p=subprocess.Popen(["/sbin/ifconfig"],stdout=subprocess.PIPE)
  ip=p.communicate()
  pattern=re.compile(r'inet\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  return pattern.findall(ip[0])

def private_ip():
  ips=[]
  p=subprocess.Popen(["/sbin/ifconfig"],stdout=subprocess.PIPE)
  ip=p.communicate()
  pattern=re.compile(r'inet\s*(192\.168\.\d{1,3}\.\d{1,3})')
  ips.extend(pattern.findall(ip[0]))
  pattern=re.compile(r'inet\s*(10\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  ips.extend(pattern.findall(ip[0]))
  pattern=re.compile(r'inet\s*(127\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  ips.extend(pattern.findall(ip[0]))
  pattern=re.compile(r'inet\s*(172\.(1[6-9]|2[0-9]|3[0-1])\.\d{1,3}\.\d{1,3})')
  for ip_data in pattern.findall(ip[0]):
    ips.append(ip_data[0])
  return ips

def public_ip():
  return list(set(ipaddress())-set(private_ip()))

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
  try:
    return profiler_hardware_datatype()['Total Number of Cores']
  except: 
    return profiler_hardware_datatype()['Total Number Of Cores']

def os():
  return subprocess.Popen(["sw_vers"], stdout=subprocess.PIPE).communicate()[0].split('\n')[0].split('\t')[1]

def os_version():
  return subprocess.Popen(["sw_vers"], stdout=subprocess.PIPE).communicate()[0].split('\n')[1].split('\t')[1]

def processor_speed():
  return profiler_hardware_datatype()['Processor Speed']

def cpu_type():
  return profiler_hardware_datatype()['Processor Name']

def serial_number():
  return profiler_hardware_datatype()['Serial Number (system)']

def model():
  return profiler_hardware_datatype()['Model Name']

#def cpu_threads():
#  return profiler_hardware_datatype()['Memory']
