#!/usr/bin/python3
import masscan
from mcstatus import JavaServer
import random

maxrate = 250

first = random.randint(0,255)
second = random.randint(0,255)
first = 85
second = 214

iprange = str(first) + '.' + str(second) + ".0.0/16"
print(iprange)


mas = masscan.PortScanner()
try:
    mas.scan(iprange, ports='25565', arguments=('--max-rate ' + str(maxrate) + " --excludefile exclude.conf"))
    ips = mas.all_hosts


except Exception as e:
    print(e)

else:
    for ip in ips:
        try:
            server = JavaServer.lookup(ip)
            status = server.status().raw
        except Exception as e:
            print('\n')
            print(ip + ": " + str(e))
        else:
            print('\n')
            print(ip)
            print(status)
            if int(status["players"]["online"]) > 0:
                for player in status["players"]["sample"]:
                    print(player)