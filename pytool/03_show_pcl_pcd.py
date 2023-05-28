## Script show all the point cloud in a csv file

import csv
import numpy as np
import open3d as o3d
import glob

root_path = "/home/darkblue/code/oh_my_loam/data/test_csv/"
## read the pcd file, frame_000001.pcd
names = glob.glob(root_path + "*.pcd")
pcd = o3d.io.read_point_cloud(root_path + names[0] + ".pcd")


## show each frame point cloud using open3d
total_frames = 2400

vis = o3d.visualization.Visualizer()
vis.create_window()

vis.add_geometry(pcd)
for i in range(100):
    ## Use numpy to read the first 32000 lines (exclude the first line)
    print(f"current frame {i}")
    name = names[i]
    path = root_path + name + ".pcd"
    print(f"reading {path}")
    ## Use open3d to visualize the point cloud
    pcl = o3d.io.read_point_cloud(path)
    pcd.points = pcl.points
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
