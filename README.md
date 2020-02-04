# OpenCV-python-extract-table-from-image
OpenCV script to extract table from binary matrix image (Can be applied to any image containing table) and travel from bottom row to top

#IMPORTANT
Script extract_data.py will extract table data in csv format from any image

## About getting solution
There are two scripts
1. extract_data.py - It will extract matrix from image and will store it in csv file
2. compute_distance.py - It will find out shortest distance to the top floor

How to run?
1. Copy image file to the same folder as that of the scripts
2. Run 'python3 extract_data.py'
    - It will ask you to 'Enter image name : '
    - Type image name. for example test.png
    - Once done script will prompt you with the message 'Data extracted successfuly'
3. Then run 'python3 compute_distance.py'
    - It will ask you to 'Enter start location : '
    - Type start location in terminal (space seperated) for example: 0 2
    - Once done script will tell you answer like 'Shortest distance to top floor is ::  6'
    
#NOTE - I will update README File soon
