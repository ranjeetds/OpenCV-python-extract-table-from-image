# OpenCV-python-extract-table-from-image

#### ```extract_data.py``` will extract table from any image and store it in csv format

### Example
- Input image

![alt text](https://github.com/ranjeetds/OpenCV-python-extract-table-from-image/blob/master/test.png "Input matrix/table")

- Output

|	  | 0| 1| 2| 3| 4| 5|
|---|--|--|--|--|--|--|
|0	| 0| 0| 0| 0| 0| 0|
|1	| 1| 0|	1| 0| 0| 1|
|2	| 0| 1|	0| 0|	1| 0|
|3	| 1| 0|	1| 0|	1| 0|
|4	| 0| 0|	1| 0|	0| 0|

### Requirements
- Please run ```pip install requirements.txt```

### Notes
- This script might not work out of the box for all the images, hence you might neet to edit script and tune parameters to get optimal solutions for your images

### How to run this script?
- ```python3.x extract_data.py```
- It will ask you to enter image name (Provide image name with path)
