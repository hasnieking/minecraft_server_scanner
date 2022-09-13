import mysql.connector
import json
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

    readyDB(db)
    return db


#create tables in database
def readyDB(db):
    cursor = db.cursor()
    sql = general.readText("db/create_tables.sql")
    cursor.execute(sql)


def saveservers(db, servers):
    server = servers[0]
    insertservers(db, server)
    db.commit()


#insert server info into entry in db
def insertservers(db, server):
    cursor = db.cursor()
    sql = general.readText("db/insertserver.sql")
    values = (server[0], server[1], server[2], server[3])
    cursor.execute(sql, values)