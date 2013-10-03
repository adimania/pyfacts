import re
import subprocess
import socket

def ipaddress():
  p = subprocess.Popen(["/sbin/ip","addr","show"], stdout=subprocess.PIPE)
  ip=p.communicate()
  pattern = re.compile(r'inet\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  return pattern.findall(ip[0])

def fqdn():
  return socket.gethostname()

def memory():
  return subprocess.Popen(["grep","MemTotal","/proc/meminfo"], stdout=subprocess.PIPE).communicate()[0].split()[1:]

def swap():
  return subprocess.Popen(["grep","SwapTotal","/proc/meminfo"], stdout=subprocess.PIPE).communicate()[0].split()[1:]

def cpu_cores():
  return subprocess.Popen(["grep","-m1","cores","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0].split()[-1]

def cpu_threads():
  return subprocess.Popen(["grep","-c","processor","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0].split()[-1]


