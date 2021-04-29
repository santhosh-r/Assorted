#!/usr/bin/python3
"""
CSI 502 Homework 2 Problem 1

Santhosh

Code: http://www.open3d.org/docs/tutorial/Basic/pointcloud.html
"""

import numpy as np
import open3d

def main():
  pc_files = ["input/bunny-pts.ply", "input/mobius_3t.xyz"] # files storing point cloud data
  for i in range(2):
    print("\nReading and Displaying", pc_files[i])
    pcd = open3d.read_point_cloud(pc_files[i]) # read point cloud data from file
    print(pcd) # print details of point cloud
    open3d.draw_geometries([pcd]) # display point cloud
  
if __name__ == "__main__":
  main()