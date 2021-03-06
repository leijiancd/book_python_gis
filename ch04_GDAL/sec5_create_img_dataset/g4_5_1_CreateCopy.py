# -*- coding: utf-8 -*-
import os
from osgeo import gdal

driver = gdal.GetDriverByName("GTiff")

src_filename = "gdata/lu75c.tif"
dst_filename = "gdata/x_foo_copy.tif"
src_ds = gdal.Open(src_filename)
dst_ds = driver.CreateCopy(dst_filename, src_ds, 0)

dst_filename2 = "gdata/x_foo_copy2.tif"
dst_ds = driver.CreateCopy(dst_filename2, src_ds, 0, ['TILED = YES', 'COMPRESS=PACKBITS'])

dst_filename3 = "gdata/x_foo_copy3.tif"
dst_ds = driver.CreateCopy(dst_filename3, src_ds, 0, ['TILED = YES', 'COMPRESS=PACKBITS'])

dataset = gdal.Open("foo.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0, 0, width, height)
driver = gdal.GetDriverByName("Gtiff")
driver.CreateCopy("gdata/xx_foo5.tif", dataset)


def Test():
    assert True
