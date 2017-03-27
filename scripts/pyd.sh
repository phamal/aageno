#!/bin/sh
echo "Download all dependencies "
pip install sh
pip install bs4
pip install lxml
pip install elasticsearch
pip install fire --user
sudo pip install flask
sudo pip install flask_sqlalchemy
sudo pip install sqlalchemy
sudo pip install configparser
sudo pip install flask-cors
echo "sudo pip install pandas "
echo "sudo pip install tika "
echo "Restarting aageno app"
