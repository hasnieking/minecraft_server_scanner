#!/usr/bin/python3
import masscan
from mcstatus import JavaServer
import random

#masscan rate
maxrate = 250

#set ip range
first = random.randint(0,255)
second = random.randint(0,255)
first = 85
second = 214
iprange = str(first) + '.' + str(second) + ".0.0/16"
print(iprange)

#scan ip range for port 25565
mas = masscan.PortScanner()
try:
    mas.scan(iprange, ports='25565', arguments=('--max-rate ' + str(maxrate) + " --excludefile exclude.conf"))
    ips = mas.all_hosts


except Exception as e:
    print(e)

else:
    for ip in ips:
        #get server info
        try:
            server = JavaServer.lookup(ip)
            status = server.status().raw
            max = int(status["players"]["max"])
            version = status["version"]["name"]
            onlinenr = int(status["players"]["online"])
            if onlinenr > 0:
                samplepl = status["players"]["sample"]
        #catch exception
        except Exception as e:
            print('\n')
            print(ip + ": " + str(e))
        #prints info
        else:
            print('\n')
            print(ip)
            print(str(onlinenr) + "/" + str(max))
            print(version)
            if int(onlinenr) > 0:
                for player in samplepl:
                    print(player)