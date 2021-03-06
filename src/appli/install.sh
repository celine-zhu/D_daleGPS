#!/bin/bash
python3 -m venv env 
source env/bin/activate 
pip3 install Flask 
pip3 install Flask-Images
pip3 install geopandas
pip3 install imutils
pip3 install opencv-python
pip3 install matplotlib
echo 'env/' >> .gitignore  
pip3 freeze 
pip3 freeze > requirements.txt 
pip3 install -r requirements.txt 
pip3 install click
deactivate
exit $?
