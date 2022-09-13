### Better factory simulations
#### Scale map image creation
Using whichever environment you please, install the pip requirements (Only numpy
and opencv required). You can do so manually, or going to the src folder and
executing the following command:
```bash
pip install -r requirements.txt
```
Then, go through the utils.py script, which is documented and self-explanatory,
modify the "boxes" variable in the main execution block, with the tuples
following the convention given in the documentation and based on the desired
map to create. Then execute the script:
```bash
python utils.py
```
And a file called "basemap.jpg" will be created in the directory you executed
from. This image corresponds to the created map with your given dimensions.
#### Gazebo world
- Manually created through Gazebo based on a properly scaled map image.
- The image can be created with the python script "script_name_here.py".
#### Map file creation of the Gazebo world through Neobotix's SLAM
- Follow the instructions given by [neobotix slam official docs - here]().
#### Heatmap through laser aggregation
- The LIDAR URDF is provided, and they are placed in the Gazebo world, by running
  the following ros instructions.
- Use lidar aggregator given by [ragesh's repo - here]().

