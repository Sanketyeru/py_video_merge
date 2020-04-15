# Video merge tool written in python

## Prerequisite
1. Python 3
2. OpenCV
3. Numpy

## Quick Start
* Clone the gt repository
    ```
    git clone https://github.com/Sanketyeru/py_video_merge.git
    cd py_video_merge
    ```
* Arguments
    |Name   	|Option   	|Description   	                                                 |
    |---	    |---	    |---	                                                         |
    |Videos   	|-v   	    |Space separated list of videos   e.g. vid1.mp4 vid2.mp4 vid3.mp4|
    |Config   	|-c   	    |Output video configuration Row x Column e.g.(2x4)|
    |Resize   	|-r   	    |To resize or not maintain original e.g.(True/False)   	        |


* Example 
    ```bash
    python main.py -v path_to_video1.mp4 path_to_video2.mp4 path_to_video3.mp4 -c 2x2 -r True
    ```
    |           OUTPUT FRAME|           |
    |---	    |---	    |
    |vid 1   	|vid2    	|
    |vid 3   	|black frame |
    