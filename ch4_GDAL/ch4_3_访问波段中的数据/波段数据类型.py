In [54]: from osgeo import gdalconst
In [55]: dir(gdalconst)
Out[55]: 
['CE_Debug',
 'CE_Failure',
 'CE_Fatal',
 'CE_None',
 'CE_Warning',
 'CPLES_BackslashQuotable',
 'CPLES_CSV',
 'CPLES_SQL',
 'CPLES_URL',
 'CPLES_XML',
 'CPLE_AppDefined',
 'CPLE_AssertionFailed',
 'CPLE_FileIO',
 'CPLE_IllegalArg',
 'CPLE_NoWriteAccess',
 'CPLE_None',
 'CPLE_NotSupported',
 'CPLE_OpenFailed',
 'CPLE_OutOfMemory',
 'CPLE_UserInterrupt',
 'CXT_Attribute',
 'CXT_Comment',
 'CXT_Element',
 'CXT_Literal',
 'CXT_Text',
 'DCAP_CREATE',
 'DCAP_CREATECOPY',
 'DCAP_VIRTUALIO',
 'DMD_CREATIONDATATYPES',
 'DMD_CREATIONOPTIONLIST',
 'DMD_EXTENSION',
 'DMD_HELPTOPIC',
 'DMD_LONGNAME',
 'DMD_MIMETYPE',
 'GARIO_COMPLETE',
 'GARIO_ERROR',
 'GARIO_PENDING',
 'GARIO_UPDATE',
 'GA_ReadOnly',
 'GA_Update',
 'GCI_AlphaBand',
 'GCI_BlackBand',
 'GCI_BlueBand',
 'GCI_CyanBand',
 'GCI_GrayIndex',
 'GCI_GreenBand',
 'GCI_HueBand',
 'GCI_LightnessBand',
 'GCI_MagentaBand',
 'GCI_PaletteIndex',
 'GCI_RedBand',
 'GCI_SaturationBand',
 'GCI_Undefined',
 'GCI_YCbCr_CbBand',
 'GCI_YCbCr_CrBand',
 'GCI_YCbCr_YBand',
 'GCI_YellowBand',
 'GDT_Byte',
 'GDT_CFloat32',
 'GDT_CFloat64',
 'GDT_CInt16',
 'GDT_CInt32',
 'GDT_Float32',
 'GDT_Float64',
 'GDT_Int16',
 'GDT_Int32',
 'GDT_TypeCount',
 'GDT_UInt16',
 'GDT_UInt32',
 'GDT_Unknown',
 'GFT_Integer',
 'GFT_Real',
 'GFT_String',
 'GFU_Alpha',
 'GFU_AlphaMax',
 'GFU_AlphaMin',
 'GFU_Blue',
 'GFU_BlueMax',
 'GFU_BlueMin',
 'GFU_Generic',
 'GFU_Green',
 'GFU_GreenMax',
 'GFU_GreenMin',
 'GFU_Max',
 'GFU_MaxCount',
 'GFU_Min',
 'GFU_MinMax',
 'GFU_Name',
 'GFU_PixelCount',
 'GFU_Red',
 'GFU_RedMax',
 'GFU_RedMin',
 'GF_Read',
 'GF_Write',
 'GMF_ALL_VALID',
 'GMF_ALPHA',
 'GMF_NODATA',
 'GMF_PER_DATASET',
 'GPI_CMYK',
 'GPI_Gray',
 'GPI_HLS',
 'GPI_RGB',
 'GRA_Bilinear',
 'GRA_Cubic',
 'GRA_CubicSpline',
 'GRA_Lanczos',
 'GRA_NearestNeighbour',
 '__builtins__',
 '__doc__',
 '__file__',
 '__name__',
 '__package__',
 '_gdalconst',
 '_newclass',
 '_object',
 '_swig_getattr',
 '_swig_property',
 '_swig_repr',
 '_swig_setattr',
 '_swig_setattr_nondynamic']
以GDT开头的就是数值数据类型
要想查看图像中某一波段的数据类型，只需要打印这一波段的DataType属性即可
band.DataType

