# ar_tag_drone

## prerequisites

    $ sudo apt-get install v4l-utils

    $ sudo apt-get install ros-meldic-usb-cam
	
	$ sudo apt-get install ros-melodic-video-stream-opencv
	
	$ sudo apt-get install ros-melodic-image-pipeline

### testing usb_cam_node

    $ rosrun usb_cam usb_cam_node _video_device:=/dev/video0
> Notes:
> - Choosing between camera devices can be done changing "N" /dev/videoN 
> - Video format can cause problems (mpeg, yuyv)

## Installation
source: <https://projectsfromtech.blogspot.com/2017/09/tracking-ar-tags-with-ros-monocular.html>
	
In your catkin workspace:

	$ git clone https://github.com/ros-perception/ar_track_alvar.git 
	$ cd ..
	$ catkin_make

Create own project in catkin workspace

	$ catkin_create_pkg ar_tag_demo std_msgs rospy
	
## run ar_track_alvar
	$ roslaunch ar_tag_demo main.launch
	
## Markers in Gazebo
<https://github.com/mikaelarguedas/gazebo_models>
## Tutorials
<https://realitybytes.blog/2017/06/02/detecting-and-tracking-ar-tags/>

<https://wiki.ros.org/ar_track_alvar>

## Troubleshooting
### Swap space
If the catkin_make process freezes your computer, it may be caused by small RAM capacity. Then make or increase swap memory space: <https://stackoverflow.com/questions/54886993/problem-with-the-installation-of-dji-osdk-on-raspberry-pi-3-for-dji-matrice-100>

	$ sudo fallocate -l 8G /swapfile
	$ sudo chmod 600 /swapfile
	$ sudo mkswap /swapfile
	$ free -h
	$ echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

Then restart your computer.