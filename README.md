# zenoh-python-ros2


## run zenoh bridge
zenoh-bridge-ros2dds -l udp/0.0.0.0:7447 -d 2 --ros-localhost-only


## usage
### senario1: topic home -> robot
robot(terminal1):

`ROS_LOCALHOST_ONLY=1 ROS_DOMAIN_ID=2 RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 run robot_side subscriber`

home(terminal2):

`python home_side/publisher.py`


### senario2: topic home <- robot
robot(terminal1):

`ROS_LOCALHOST_ONLY=1 ROS_DOMAIN_ID=2 RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 run robot_side publisher`

home(terminal2):

`python home_side/subscriber.py`

### senario3: service request (home -> robot) and response (home <- robot)
robot(terminal1):

`ROS_LOCALHOST_ONLY=1 ROS_DOMAIN_ID=2 RMW_IMPLEMENTATION=rmw_cyclonedds_cpp ros2 run robot_side math_server`

home(terminal2):

`python home_side/call_service.py`