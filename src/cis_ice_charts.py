"""Visualize g02171 data

https://nsidc.org/data/g02171/versions/2

Goal: Focus on the Eastern Arctic with a focus on visualizing the North Water
Polynya over time (https://en.wikipedia.org/wiki/North_Water_Polynya)

Data are given as zipped/tarred polygons as Shapefiles. Each polygon represents an area of roughly consistent conditions.

The `CT` attribute gives Sea Ice Concentration (SIC).

One idea is to threshold SIC like we do for the Sea Ice Index (SII) to visualize Sea Ice Extent (SIC).

Might want to convert to raster, average SIC over a month, then convert to SIE.

------------

Rough process of converting to raster (in EPSG:3413):

First,  reproject:

$ ogr2ogr -t_srs "EPSG:3413" reprojected.gpkg CIS_EA_19760618_pl_a.shp

Then, convert to raster for our area of interest:

$ gdal_rasterize -a CT -te -1614945.125000 -1641002.625000 -64659.257812 -703273.562500 -tr 100 100 -tap reprojected.gpkg out.tif

------------
"""
