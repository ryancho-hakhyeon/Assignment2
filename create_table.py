import sqlite3

conn = sqlite3.connect('audio_library_db.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE songs_tb
          (file_name String PRIMARY KEY,
           title String,
           artist String,
           runtime String,
           album String,
           genre String,
           location String(200) NOT NULL)
          ''')

conn.commit()
conn.close()
