# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)



# 创建点状数据集
from osgeo import ogr
import os ,math
driver = ogr.GetDriverByName("ESRI Shapefile")

extfile='xx_1world_borders.shp'
point_coors = [[300,450],[750,700],[1200,450],[750,200],[750,450]]
print(point_coors)
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point',None,ogr.wkbPoint)
for aa in point_coors:
    wkt = 'POINT (' + str(aa[0]) + ' ' + str(aa[1]) + ')'
    geom = ogr.CreateGeometryFromWkt(wkt)
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)

newds.Destroy()


def Test():
    assert True
