# SRTM dataset

## Download

Download the data from http://srtm.csi.cgiar.org/

* http://srtm.csi.cgiar.org/SRT-ZIP/SRTM_V41/SRTM_Data_GeoTiff/srtm_39_02.zip
* http://srtm.csi.cgiar.org/SRT-ZIP/SRTM_V41/SRTM_Data_GeoTiff/srtm_39_03.zip

## Patch

Patch the two files using GDAL
```
gdalbuildvrt srtm.vrt srtm_39_03.tif srtm_39_02.tif
```

## Cut out area of interest

```
gdal_translate -of GTiff -projwin 411805.89162 5549990.32375 430548.500693 5535698.83483 -projwin_srs "+init=epsg:32633" srtm.vrt srtm.geotiff -co COMPRESS=LZW
```

## Warp to target projection

```
gdalwarp -t_srs "+init=epsg:32633" srtm.geotiff srtm-utm.geotiff
```



