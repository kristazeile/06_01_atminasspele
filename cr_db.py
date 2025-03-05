import sqlite3

db = sqlite3.connect('dati.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS rezultati (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vards TEXT NOT NULL,
            klikski INTEGER NOT NULL,
            laiks INTEGER NOT NULL,
            datums TEXT NOT NULL
            )""")
ieraksti = [
    ('Anonimais', 100, 100, "2020-01-01"),
    ('Anonimais', 100, 100, "2020-01-01"),
    ('Anonimais', 100, 100, "2020-01-01"),
    ('Anonimais', 100, 100, "2020-01-01"),
    ('Anonimais', 100, 100, "2020-01-01")
]
sql.executemany('''
INSERT INTO rezultati (vards, klikski, laiks, datums)
                VALUES (?, ?, ?, ?)
''', ieraksti)
db.commit()
db.close()

print("Datubāze un ieraksti izveidoti")