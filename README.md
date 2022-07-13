# Imx219Camera
this is arepo for access image data for imx219 monocular camera, typically used in Jetson device vis CSI interface.
## imx219py
this folder contains python version of imx 219 camera nodes, with **imx219_pub** as image publishing node and **imx219_sub** as a simple opencv visualization node.

## image topic
raw image topic is **imx219cam**, you can modify it as your wish.

## Usage

## for python

```shell
source /opt/ros/<your rosdistro>/setup.bash
cd /path/to/imx219py //folder which contains packages.xml file.
rosdep install --from-paths . -y
cd ..
colcon build --packages-select imx219py
```

to run our node (publishing node and subscribing node):

```shell
ros2 run imx219py imx219_pub
```

```shell
ros2 run imx219py imx219_sub
```


## for c plus plus

00
