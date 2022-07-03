import sqlite3

qan = input("qaysi malumot kerak: ")
ids = input("qaysi user_id ni malumoti kerak: ")

db = sqlite3.connect('probasas.sqlite3')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS bazas ("user_id"  INTEGER,"photo"  INTEGER,"music"  INTEGER, "video" INTEGER);""")
db.commit()

sql.execute(
    f"""INSERT INTO bazas (user_id, photo, music, video) VALUES ('000', 'rasm3', 'musie2c', 'vide21')""")
db.commit()
try:
    sql.execute(f"""SELECT {qan} FROM bazas WHERE user_id = {ids}""")
    ss = sql.fetchall()
    for s in ss:
        print(s[0])
except:
    print("sleep")
