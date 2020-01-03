#!/usr/bin/env bash
# command to create and prepare the servers for the applications
apt-get update -y
apt-get install -y nginx
DIR="/data/web_static/shared/"
mkdir -p ${DIR}
DIR="/data/web_static/releases/test/"
mkdir -p ${DIR}
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "46i location /hbnb_static {" /etc/nginx/sites-enabled/default
sed -i "47i   alias /data/web_static/current/;" /etc/nginx/sites-enabled/default
sed -i "48i   autoindex off;" /etc/nginx/sites-enabled/default
sed -i "49i }" /etc/nginx/sites-enabled/default
service nginx restart
