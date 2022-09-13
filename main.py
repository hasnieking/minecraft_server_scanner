#!/usr/bin/python3
import masscan
from mcstatus import JavaServer
import random
import dbHandler
import general

#masscan rate
maxrate = 250

#range to scan
range_addition = ".0.0/16"

#minecraft port range
portrange = "25565"


def start():
    #get database ready
    dbHandler.readyDB()
    while True:
        loop()


#main loop
def loop():
    servers = []

    #scan ip range for port 25565
    mas = masscan.PortScanner()
    try:
        mas.scan(iprange(), ports=portrange, arguments=('--max-rate ' + str(maxrate) + " --excludefile exclude.conf"))
        ips = mas.all_hosts

    except Exception as e:
        print(e)

    else:
        for ip in ips:
            #get server info
            serverinfo(servers, ip)

    dbHandler.saveservers(servers)


#get server information through mcstatus
def serverinfo(servers, ip):
    try:
        server = JavaServer.lookup(ip)
        status = server.status().raw
        max = int(status["players"]["max"])
        version = status["version"]["name"]
        onlinenr = int(status["players"]["online"])
        samplepl = list
        if onlinenr > 0:
            samplepl = status["players"]["sample"]
    #catch exception
    except Exception as e:
        print('\n')
        print(ip + ": " + str(e))
    #prints info
    else:
        playerlist = getplayers(onlinenr, samplepl)
        server = (ip, onlinenr, max, version, playerlist)
        printserver(server)
        servers.append(server)
        


#set ip range to scan
def iprange():
    first = random.randint(0,255)
    second = random.randint(0,255)
    iprange = str(first) + '.' + str(second) + range_addition
    print(iprange)
    return iprange



#get players from server json data
def getplayers(onlinenr, samplepl):
    playerlist = []
    if onlinenr == 0:
        return playerlist
    if onlinenr <= 12:
        if onlinenr != len(samplepl):
            print("No player data available")
            return playerlist
    for player in samplepl:
        if len(player["name"]) <= 16 and len(player["id"]) == general.uuidlen:
            playerlist.append(player)
        else:
            print("Error getting player")
    return playerlist
    

#print server details to stdout
def printserver(server):
    print("ip: " + server[0])
    print("Version: " + server[3])
    print("Players: " + str(server[1]) + "/" + str(server[2]))
    for player in server[4]:
        print(player)
    print("\n")



start()