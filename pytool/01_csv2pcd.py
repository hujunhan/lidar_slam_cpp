## Script show all the point cloud in a csv file

import csv
import numpy as np
import open3d as o3d
csv_path = '/Users/hu/Downloads/C16_v4.0.0_2023-03-11-13-02_660Frame.csv'
csv_path = '/home/darkblue/Downloads/outdoor.csv'


## Read the first 10 lines
read_lines = 3

## Make sure the csv file has the same number of columns in each row
for i, line in enumerate(csv.reader(open(csv_path, 'r'))):
    if i == read_lines:
        break
    print(line)

row_item_num = len(line)

## show each frame point cloud using open3d
# vis=o3d.visualization.Visualizer()
# vis.create_window()
pcd=o3d.geometry.PointCloud()
total_frames=2400
reader=open(csv_path, 'r')
reader.readline() # skip the first line
buffer_size=32000
data=np.empty((buffer_size,row_item_num))
for i in range(0,total_frames):
    ## Use numpy to read the first 32000 lines (exclude the first line)
    print(f'current frame {i}')
    # data = np.genfromtxt(csv_path, delimiter=',', skip_header=1+32000*i, max_rows=32000,missing_values=None)
    data=np.genfromtxt(reader, delimiter=',', max_rows=buffer_size,missing_values=None, filling_values=0, usecols=range(0,5))
    point_cloud=data[:,2:5]
    # exclude the points with all zeros data
    point_cloud=point_cloud[~np.all(point_cloud == 0, axis=1)]
    ## Use open3d to visualize the point cloud
    pcd.points=o3d.utility.Vector3dVector(point_cloud)
    ## save to pcd file, frame_000001.pcd to frame_000660.pcd
    pcd_file_name = f'/home/darkblue/code/oh_my_loam/data/outdoor/frame_{i:06d}.pcd'
    o3d.io.write_point_cloud(pcd_file_name, pcd)
    
    