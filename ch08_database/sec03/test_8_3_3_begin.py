# -*- coding: utf-8 -*-
import sqlite3 as sqlite
import os
import config
import time
os.chdir(config.gisws)

# 这个地方注意，使用挂载的Windows，有问题。
spt_file = "/home/bk/tmp/xx_myDatabase2.sqlite"
if os.path.exists(spt_file):
    os.remove(spt_file)

db = sqlite.connect(spt_file)
db.enable_load_extension(True)
db.execute('SELECT load_extension("libspatialite.so.5")')
cursor = db.cursor()


cursor.execute('SELECT InitSpatialMetaData();')

cursor.execute("DROP TABLE IF EXISTS gshhs")

cursor.execute("CREATE TABLE gshhs (" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "level INTEGER)")


cursor.execute("CREATE INDEX gshhs_level ON gshhs(level)")

cursor.execute("SELECT AddGeometryColumn('gshhs', 'geom', " +
               "4326, 'POLYGON', 2)")

cursor.execute("SELECT CreateSpatialIndex('gshhs', 'geom')")


db.commit()

sql_tpl = "INSERT INTO gshhs (level, geom) VALUES (2, GeomFromText('{0}', 4326))"

import ogr

fName = 'GSHHS_l/GSHHS_l_L1.shp'
shapefile = ogr.Open(fName)
layer = shapefile.GetLayer(0)
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    geometry = feature.GetGeometryRef()
    wkt = geometry.ExportToWkt()
    cursor.execute(sql_tpl.format(wkt))

db.commit()


def Test():
    assert shapefile
    assert db
    assert cursor


def tearDown():
    if cursor:
        cursor.close()
    if db:
        db.close()
    if os.path.exists('xx_myDatabase2.sqlite'):
        pass
        # os.remove('xx_myDatabase2.sqlite')
