import open3d
import numpy as np

### Begin slightly modified code from: http://www.open3d.org/docs/tutorial/Advanced/customized_visualization.html
def custom_draw_geometry(pcd):
  """Used for black background"""
  # The following code achieves the same effect as:
  # draw_geometries([pcd])
  vis = open3d.Visualizer()
  vis.create_window()
  opt = vis.get_render_option()
  opt.background_color = np.asarray([0, 0, 0])
  vis.add_geometry(pcd)
  vis.run()
  vis.destroy_window()
### End
