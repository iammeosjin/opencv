# Setup
I suggest you use python version=3.5, but if you are using [anaconda](https://docs.anaconda.com/anaconda/install/windows/). 
<br/>
Uninstall existing python environment.
<br/>
Install anaconda
<br/>
in command line: conda create -n "p35" python=3.5 anaconda
<br/>
after the env is created, conda activate p35
<br/>
check the python version by python --version
<br/>

# Install Opencv 
if you are using anaconda, conda activate p35
<br>
python -m pip install --upgrade pip
<br/>
pip install opencv-contrib-python
<br>
pip install numpy

# Process
1. Read the image
2. Resize image (648, 480)
3. Remove single color background
4. Convert to gray scale image
5. Add trackbar to adjust threshold and contours
6. Find the areas for each contour
7. Count how many areas greater than 200; if areas > 1 = fertile, areas = 1, infertile

# How to use?
![image](https://github.com/iammeosjin/opencv/blob/master/egg/doc/home.PNG)
The application has trackbar which the user can manually adjust base on the lighting.
<br/>
We have 4 sample images in the input folder, it has tags "_a", "_b". 
<br/>
These 2 images with same tags has same environment, so they must have the same settings.
<br/>
For tag "_a", you can set settings type: 3 and value: 53
<br/>
For tag "_b", you can set settings type: 3 and value: 38