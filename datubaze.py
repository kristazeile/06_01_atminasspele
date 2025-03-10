import sqlite3



def get_top_results():
  conn = sqlite3.connect('database.db')
  c = conn.cursor()
  c.execute("SELECT * FROM rezultati")
  rezultati = SQL.fetchall()
  conn.close()
  dati = [
    {"id": r[0], "vards": r[1], "rezultats": r[2], "laiks": r[3], "datums": r[4]}
    for r in rezultati
    ]
  
  return dati

def pievienot(dati):
  conn = sqlite3.connect('database.db')
  c = conn.cursor()
  c.execute("""INSERT INTO rezultati (vards, rezultats, laiks, datums)
  VALUES (?, ?, ?, ?)
  """, (dati['vards'], dati['rezultats'],dati['laiks'],dati['datums']))
  conn.commit()
  conn.close()
  