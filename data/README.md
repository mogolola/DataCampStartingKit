We provide a sub dataset of remote sensing images and their histogram representation of one state in the US. 

*data\_image_full* contains original satellite images. 
*data\_temperature* contains temperature images. 
*data\_mask* contains masks which is used to filter non farm informations.

The merge of these three types of images are in *img\_full_output*.
The unsampling of the precessed images are in *img\_zoom_full_output*.

All of those raw data can be found in https://drive.google.com/open?id=1CXWSM-7YFaVgRGXMIulpyMruDWvCFc19.

For accessing the whole raw data of the US, using the files in *download_data*, note that you should have access to Google Earth cause we using its Python interface to download data. Then use *clean\_data.py* to get precessed images.

The list of crop field locations in the US is saved in *locations.csv*. Each column represents code of state, code of county, latitude and longitude. The list of crop field locations of state 1 is saved in *location\_state.csv*.
 The list of yield of the US is saved in *yields.csv*. Each column represents year, code of state, code of county and yield. The list of yield of state 1 is saved in *yield\_state.csv*. 
 
 The pretraited histogram vectors are packaged in *data.npz*, then we separate it in trainset *train.npz* and testset *test.npz* which you can used directly for prediction.