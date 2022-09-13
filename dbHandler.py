import mysql.connector
import general

#create connector for database
def createDBConnector():
    settings = general.readJSON("settings.json")

    db = mysql.connector.connect(
        host = settings["database"]["host"],
        user = settings["database"]["user"],
        password = settings["database"]["password"],
        database = settings["database"]["database"]
    )
    return db


#create tables in database
def readyDB():
    db = createDBConnector()
    cursor = db.cursor()
    sql = general.readText("db/create_tables.sql")
    cursor.execute(sql)
    db.close()

    #store queries in memory
    global insertserversql
    global insertplayersql
    insertserversql = general.readText("db/insertserver.sql")
    insertplayersql = general.readText("db/insertplayer.sql")


#run insertservers and insertplayers, and then commit at the end
def saveservers(servers):
    db = createDBConnector()
    for server in servers:
        serverid = insertservers(db, server)
        insertplayers(db, server[4], serverid)
    db.commit()
    db.close()


#insert server info into entry in db
def insertservers(db, server):
    cursor = db.cursor()
    values = (server[0], server[1], server[2], server[3])
    cursor.execute(insertserversql, values)
    return cursor.lastrowid

#insert players in the database with the server they are connected to
def insertplayers(db, playerlist, serverid):
    cursor = db.cursor()
    for player in playerlist:
        values = (serverid, player["id"], player["name"])
        cursor.execute(insertplayersql, values)