#!/usr/bin/env bash
# A Bash script tah sets up a web server for deplou=yment

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo "<html<head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i 's|^.*server_name.*$|&\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-available/default

sudo service nginx restart
