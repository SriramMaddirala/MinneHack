import sqlite3
def initconnect():
    conn = sqlite3.connect("Health.db")
    c = conn.cursor()
    c.execute('CREATE TABLE {tn} ({patName}, {regid}, {sport}, {inj},{partId}, {preweig},{currweig},{recov})'\
              .format(tn="Patient Data", patName="Name", regid = "Registration ID", sport = "Sport", inj = "Injury", preweig= "Pre-Injury Weight",currweig= "Current Weight",recov = "Status of Recovery" ))
    conn.commit()
    conn.close()
def adduser(name,id,sprt, injury, partner, goalweigh, currweigh, recove):
    conn = sqlite3.connect("Health.db")
    c = conn.cursor()
    c.execute("INSERT INTO {tn} ({patName}, {regid}, {sport}, {inj},{partId}, {preweig},{currweig},{recov}) VALUES (?,?,?,?,?,?,?,?)",(name,id,sprt,injury,partner,goalweigh,currweigh,recove))
    conn.commit()
    conn.close()
def getuser(name):
    conn= sqlite3.connect("Health.db")
    c = conn.cursor()
    c.execute("SELECT * FROM {tn} WHERE {patName}={getName}".\
              format(tn="Patient Data",patName="Name",getName=name))
    name, id, sprt, injury, partner, goalweigh, currweigh, recove = c.fetchall()
    return name, id, sprt, injury, partner, goalweigh, currweigh, recove