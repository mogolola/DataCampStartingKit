def preprocess_save_data_parallel(file):

    datadir = 'data/'
    MODIS_dir = datadir + "data_image_full/"
    MODIS_temperature_dir = datadir + "data_temperature/"
    MODIS_mask_dir = datadir + "data_mask/"
    img_output_dir = "img_full_output/"
    img_zoom_output_dir = "img_zoom_full_output/"



    data_yield = np.genfromtxt('yield_final.csv', delimiter=',', dtype=float)



    if file.endswith(".tif"):
        MODIS_path=os.path.join(MODIS_dir, file)
        # check file size to see if it's broken
        # if os.path.getsize(MODIS_path) < 10000000:
        #     print 'file broken, continue'
        #     continue
        MODIS_temperature_path=os.path.join(MODIS_temperature_dir,file)
        MODIS_mask_path=os.path.join(MODIS_mask_dir,file)

        # get geo location
        raw = file.replace('_',' ').replace('.',' ').split()
        loc1 = int(raw[0])
        loc2 = int(raw[1])
        # read image
        try:
            MODIS_img = np.transpose(np.array(gdal.Open(MODIS_path).ReadAsArray(), dtype='uint16'),axes=(1,2,0))
        except ValueError as msg:
            print msg
        # read temperature
        MODIS_temperature_img = np.transpose(np.array(gdal.Open(MODIS_temperature_path).ReadAsArray(), dtype='uint16'),axes=(1,2,0))
        # shift
        # MODIS_temperature_img = MODIS_temperature_img-12000
        # scale
        # MODIS_temperature_img = MODIS_temperature_img*1.25
        # clean
        # MODIS_temperature_img[MODIS_temperature_img<0]=0
        # MODIS_temperature_img[MODIS_temperature_img>5000]=5000
        # read mask
        MODIS_mask_img = np.transpose(np.array(gdal.Open(MODIS_mask_path).ReadAsArray(), dtype='uint16'),axes=(1,2,0))
        # Non-crop = 0, crop = 1
        MODIS_mask_img[MODIS_mask_img != 12] = 0
        MODIS_mask_img[MODIS_mask_img == 12] = 1

        # Divide image into years
        MODIS_img_list=divide_image(MODIS_img, 0, 46 * 7, 14)
        MODIS_temperature_img_list = divide_image(MODIS_temperature_img, 0, 46 * 2, 14)
        MODIS_mask_img = extend_mask(MODIS_mask_img, 3)
        MODIS_mask_img_list = divide_image(MODIS_mask_img, 0, 1, 14)

        # Merge image and temperature
        MODIS_list = merge_image(MODIS_img_list,MODIS_temperature_img_list)

        # Do the mask job
        MODIS_list_masked = mask_image(MODIS_list,MODIS_mask_img_list)

        # check if the result is in the list
        year_start = 2003
        for i in range(0, 14):
            year = i+year_start
            key = np.array([year,loc1,loc2])
            if np.sum(np.all(data_yield[:,0:3] == key, axis=1))>0:
                # # detect quality
                # quality = quality_dector(MODIS_list_masked[i])
                # if quality < 0.01:
                #     print 'omitted'
                #     print year,loc1,loc2,quality

                    # # delete
                    # yield_all = np.genfromtxt('yield_final_highquality.csv', delimiter=',')
                    # key = np.array([year,loc1,loc2])
                    # index = np.where(np.all(yield_all[:,0:3] == key, axis=1))
                    # yield_all=np.delete(yield_all, index, axis=0)
                    # np.savetxt("yield_final_highquality.csv", yield_all, delimiter=",")

                    # continue

                ## 1 save original file
                filename=img_output_dir+str(year)+'_'+str(loc1)+'_'+str(loc2)+'.npy'
                np.save(filename,MODIS_list_masked[i])
                print filename,':written '

                ## 2 save zoomed file (48*48)
                zoom0 = float(48) / MODIS_list_masked[i].shape[0]
                zoom1 = float(48) / MODIS_list_masked[i].shape[1]
                output_image = zoom(MODIS_list_masked[i], (zoom0, zoom1, 1))

                filename=img_zoom_output_dir+str(year)+'_'+str(loc1)+'_'+str(loc2)+'.npy'
                np.save(filename,output_image)
                print filename,':written '