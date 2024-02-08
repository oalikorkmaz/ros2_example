# ros2_example

# ROS2 Create Package:
```bash
ros2 pkg create --build-type ament_python <package_name> # for python
ros2 pkg create --build-type ament_cmake <package_name> # for c++
```


# Service
## Learn list, type, interface, call:
```bash
ros2 service list
ros2 service type /Spawn
ros2 interface show turtlesim/srv/Spawn
ros2 service call /Spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name:'my_turtle'}"
```

 