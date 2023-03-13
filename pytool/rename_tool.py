import glob
import os
## rename files by minus a zero from the file name
# example: frame_000001.pcd to frame_00001.pcd
name_list = glob.glob('/home/darkblue/code/oh_my_loam/data/test_csv/*.pcd')
# sort the list
name_list.sort()
for name in name_list:
    # get the file name
    file_name = os.path.basename(name)
    # get the file path
    file_path = os.path.dirname(name)
    # get the file name without extension
    file_name_no_ext = os.path.splitext(file_name)[0]
    # get the file extension
    file_ext = os.path.splitext(file_name)[1]
    # get the file name without the first zero
    file_name_no_zero = file_name_no_ext[0:6] + file_name_no_ext[7:]
    print(file_name_no_zero)
    # rename the file
    os.rename(name, os.path.join(file_path, file_name_no_zero + file_ext))