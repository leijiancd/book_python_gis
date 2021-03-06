# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)

#dian
# class Point( coordinates)

from shapely.geometry import Point
point = Point(0.0,0.0)
point.area
point.length
point.bounds

list(point.coords)
point.x
point.y

Point(point)

#xian
# class LineString(coordinates)

from shapely.geometry import LineString
line = LineString([(0,0),(1,1)])
print(line.area)
print(line.length)
print(line.bounds)
len(line.coords)
list(line.coords)
point.coords[:]
point.coords[1:]
LineString(line)

#mian
# class Polygon(exterior[,interiors =none])

from shapely.geometry import Polygon
polygon =Polygon([(0,0),(1,1),(1,0)])
polygon.area
polygon.length
polygon.bounds
list(polygon.exterior.coords)
list(polygon.interiors)
coords = [(0,0),(1,1),(1,0)]

from shapely.geometry import LinearRing
r = LinearRing(coords)
s = Polygon(r)
s.area
t = Polygon(s.buffer(1.0).exterior,[r])
t.area

# shapely.geometry.box(minx,miny,maxx,maxy,ccw=True)

from shapely.geometry import box
b = box(0.0,0.0,1.0,1.0)
list(b.exterior.coords)

# shapely.geometry.polygon.orient(polyfon,sign=1.0)

#duixianzhuang
import os
from osgeo import ogr
import shapely
import shapely.geometry

from shapely.ops import cascaded_union
driver = ogr.GetDriverByName('ESRI Shapefile')
out_shp ='x_world_borders.shp'
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)

newds = driver.CreateDataSource(out_shp)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

ds = ogr.Open('world_borders.shp')

layer = ds.GetLayer(0)
feat = layer.GetNextFeature()
while feat:
    geom = feat.GetGeometryRef()
    pts = geom.GetGeometryCount()
    for ii in range(pts):
        poly = geom.GetGeometryRef(ii)
        points_num = poly.GetPointCount()
        # print(points_num)
        zc_points = poly.GetPoints()
        # print(type(zc_points))
        tmp_pt_arr = []
        for x in zc_points:
            tmp_pt_arr.append(x)
        
        pt = shapely.geometry.LineString(tmp_pt_arr)
        vv = pt.buffer(3000.0)
        new_feat = ogr.Feature(layernew.GetLayerDefn())
        tmp_wkb = vv.to_wkb()
        new_geom = ogr.CreateGeometryFromWkb(tmp_wkb)
        new_feat.SetGeometry(new_geom)
        layernew.CreateFeature(new_feat)
    
    feat = layer.GetNextFeature()

newds.Destroy()


