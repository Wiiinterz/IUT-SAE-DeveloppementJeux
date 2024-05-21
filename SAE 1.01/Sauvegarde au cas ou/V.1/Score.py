from Devinette import *
import sqlite3
con=sqlite3.connect("./Database/Score.db")
curseur = con.cursor()

new_user = (curseur.lastrowid, "Julie", 1,0,0,0)
curseur.execute("INSERT INTO Score VALUES(?,?,?,?,?,?)",new_user)
con.commit()
print  ("nouvel utilisateur !")

con.close

