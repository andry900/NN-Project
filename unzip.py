import os
import gzip
import shutil

PATH_DATA = "C:\\Users\\andre\\Desktop\\Università\\Esami Non Superati\\Neural Networks\\Datasets\\MICCAI_BraTS2020_TestData"
PATH_DEST = "./Dataset/Test"

for folder_name in os.listdir(PATH_DATA):
    for file in os.listdir(PATH_DATA + "\\" + folder_name):
        if file.__contains__("t1ce.nii.gz") or file.__contains__("t2.nii.gz"):
            with gzip.open(PATH_DATA + "\\" + folder_name + "\\" + file, 'rb') as f_in:
                with open(PATH_DEST + "\\" + file.replace(".gz", ""), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            print(file)
