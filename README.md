# ros2_example

# ROS2 Create Package:
```bash
ros2 pkg create --build-type ament_python <package_name> # for python
ros2 pkg create --build-type ament_cmake <package_name> # for c++
```
# ROS2 Change Name Node:
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=another_news_station # if have been parameter: -p robot_name:another_robot
``` 

# Service
## Learn list, type, interface, call:
```bash
ros2 service list
ros2 service type /Spawn
ros2 interface show turtlesim/srv/Spawn
ros2 service call /Spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name:'my_turtle'}"
```


# Parameters

If we want to see the parameters on Ros2 nodes:
```bash
ros2 param
```

To declare a parameter:
```python
self.declare_parameter("test123")
```

I would say to set a parameter value which is already declared.
```bash
ros2 run my_py_pkg number_publisher --ros-args -p test123:=3
```
 