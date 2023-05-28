## Script show all the point cloud in a csv file

import csv
import numpy as np
import open3d as o3d

# csv_path = '/Users/hu/Downloads/C16_v4.0.0_2023-03-11-13-02_660Frame.csv'
csv_path = "/home/darkblue/Downloads/outdoor.csv"


## Read the first 10 lines
read_lines = 3

## Make sure the csv file has the same number of columns in each row
for i, line in enumerate(csv.reader(open(csv_path, "r"))):
    if i == read_lines:
        break
    print(line)

row_item_num = len(line)

## show each frame point cloud using open3d
total_frames = 2400
reader = open(csv_path, "r")
reader.readline()
buffer_size = 32000
pcl = o3d.geometry.PointCloud()
data = np.genfromtxt(
    reader,
    delimiter=",",
    max_rows=buffer_size,
    missing_values=None,
    filling_values=0,
    usecols=range(0, 5),
)
vis = o3d.visualization.Visualizer()
vis.create_window()
point_cloud = data[:, 2:5]
pcl.points = o3d.utility.Vector3dVector(point_cloud)
vis.add_geometry(pcl)
for i in range(0, total_frames):
    ## Use numpy to read the first 32000 lines (exclude the first line)
    print(f"current frame {i}")
    data = np.genfromtxt(
        reader,
        delimiter=",",
        max_rows=buffer_size,
        missing_values=None,
        filling_values=0,
        usecols=range(0, 5),
    )

    point_cloud = data[:, 2:5]
    # exclude the points with all zeros data
    point_cloud = point_cloud[~np.all(point_cloud == 0, axis=1)]
    print(f"delete {len(data)-len(point_cloud)} points")
    ## Use open3d to visualize the point cloud
    pcl.points = o3d.utility.Vector3dVector(point_cloud)
    vis.update_geometry(pcl)
    vis.poll_events()
    vis.update_renderer()
