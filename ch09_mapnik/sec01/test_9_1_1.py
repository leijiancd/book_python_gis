import mapnik2 as mapnik
m = mapnik.Map(6000,3000,"+proj=latlong +datum=WGS84")
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r=mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9'))
r.symbols.append(polygon_symbolizer)
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
lyr = mapnik.Layer('world',"+proj=latlong +datum=WGS84")
lyr.datasource = mapnik.Shapefile(file='world_borders.shp')
lyr.styles.append('My Style')
m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())
mapnik.render_to_file(m,'xworld.png', 'png')

def Test():
    assert True