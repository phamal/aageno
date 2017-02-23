#!/bin/sh
echo "Download all dependencies "
pip install sh
pip install bs4
pip install lxml
pip install elasticsearch
sudo pip install flask
sudo pip install flask_sqlalchemy
sudo pip install sqlalchemy
sudo pip install configparser
echo "sudo pip install pandas "
echo "sudo pip install tika "
echo "Restarting aageno app"
aagenotool -a
