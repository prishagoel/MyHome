import mysql.connector
f = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mycur = f.cursor()
mycur.execute("drop database healocode;")
f.commit()
print("Database deleted successfully")