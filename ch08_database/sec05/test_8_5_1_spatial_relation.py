# -*- coding: utf-8 -*-
import os
import shutil
import sqlite3 as sqlite

import config

os.chdir(config.gisws)
shutil.copy("test-2.3.sqlite", 'xx_new_db.sqlite')

conn = sqlite.connect('xx_new_db.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')
cur = conn.cursor()

recs = cur.execute("SELECT count (*) FROM Towns;")

for rec in recs:
    print(rec)

sql = '''SELECT Regions.Name, COUNT(*) FROM Towns, Regions
 WHERE Regions.Name IN (
 'VALLED','AOSTA', 'PIEMONTE', 'UMBRIA', 'LOMBARDIA',
 'CALABRIA', 'MOLISE', 'MARCHE', 'BASILICATA') AND
 Within(Towns.geometry, Regions.Geometry)
 GROUP BY Regions.Name;'''
res = cur.execute(sql)

for rec in recs:
    print(rec)
sql = '''SELECT t2.Name, t2.Peoples,
Distance(t1.geometry, t2.geometry) AS Distance
FROM Towns AS t1, Towns AS t2
WHERE t1.Name = 'Firenze' AND
Distance(t1.geometry, t2.geometry) < 10000;'''
res = cur.execute(sql)

for rec in recs:
    print(rec)
