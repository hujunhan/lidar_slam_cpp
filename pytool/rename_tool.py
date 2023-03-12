import glob
import os
## rename files by minus 1 from the file name
# example: frame_000001.pcd to frame_000000.pcd
name_list = glob.glob('./data/test_csv/*.pcd')
# sort the list
name_list.sort()
for name in name_list:
    print(name)
    # get the file name
    file_name = name.split('/')[-1]
    # get the file number
    file_num = int(file_name.split('_')[-1].split('.')[0])
    # minus 1 from the file number
    new_file_num = file_num - 1
    # get the new file name
    new_file_name = f'frame_{new_file_num:06d}.pcd'
    # rename the file
    os.rename(name, './data/test_csv/'+new_file_name)
    # print(new_file_name)