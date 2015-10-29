import subprocess
import re

def ipaddress():
    p = subprocess.Popen(["esxcli","network","ip","interface","ipv4","get"], stdout=subprocess.PIPE)
    ip = p.communicate()
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    return pattern.findall(ip[0])[::3]

def memory():
    p = subprocess.Popen(["esxcli","hardware","memory","get"], stdout=subprocess.PIPE)
    return int(p.communicate()[0].split()[2])/1024/1024
    
def processor_speed():
    p = subprocess.Popen(["vim-cmd","hostsvc/hosthardware"], stdout=subprocess.PIPE)
    cpu = p.communicate()    
    pattern = re.compile(r'hz = (\d{10}),')
    return pattern.findall(cpu[0])[0]

def cpu_cores():
    p = subprocess.Popen(["vim-cmd","hostsvc/hosthardware"], stdout=subprocess.PIPE)
    cpu = p.communicate()
    pattern = re.compile(r'numCpuCores = (\d+)')
    return int(pattern.findall(cpu[0])[0])

def cpu_threads():
    p = subprocess.Popen(["vim-cmd","hostsvc/hosthardware"], stdout=subprocess.PIPE)
    cpu = p.communicate()
    pattern = re.compile(r'numCpuThreads = (\d+)')
    return int(pattern.findall(cpu[0])[0])

def cpu_name():
    p = subprocess.Popen(["vim-cmd","hostsvc/hosthardware"], stdout=subprocess.PIPE)
    cpu = p.communicate()
    pattern = re.compile(r'description = "([^"]+)')
    return pattern.findall(cpu[0])[0]

def os_name():
   p = subprocess.Popen(["esxcli", "system", "version", "get"], stdout=subprocess.PIPE).communicate()[0].split('\n')
   data_dict = {}
   for d in p[0:]:
      data_dict[d.split(':')[0].strip()] = d.split(':')[-1].strip()
   return data_dict['Product'] + ' ' + data_dict['Build'] + ' ' + data_dict['Version']
