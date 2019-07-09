import sqlite3
connect = sqlite3.connect("platter.db")
cur = connect.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS platter(songname, singer, song_type, year)")
