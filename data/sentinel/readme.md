# Sentinel data

The dataset is downloaded from the Copernicus Open Hub https://scihub.copernicus.eu/dhus/#/home

For metadata, see the
`S2A_OPER_MTD_SAFL1C_PDMC_20160606T204858_R022_V20150704T101337_20150704T101337.xml`
file.

For purpose of this dataset, data were cut of from two raster images and put
togeher using gdal_translate. For the projection window

 ```
 gdal_translate -projwin 411805.89162 5549990.32375 430548.500693 5535698.83483 -of GTiff S2A_OPER_MSI_L1C_TL_EPA__20160605T113933_A000162_T33UUR_B${i}.vrt sentinel/S2A_OPER_MSI_L1C_TL_EPA__20160605T113933_B${i}.tiff -co COMPRESS=LZW
 ```
