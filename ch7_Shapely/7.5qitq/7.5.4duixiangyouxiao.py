# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

coords =[(0,0),(0.2),(1,1),(2,2),(2,0),(1,1),(0,0)]
p = Polygon(coords)
from shapely.validatiom import explain_validity
explain_validity(p)
