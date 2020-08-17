#!/usr/bin/env bash
# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)

apt-get update
apt-get install -y nginx


# Create directories if they don't already exist
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

echo "Holberton School" > /usr/share/nginx/html/index.html
echo "Holberton School - hbnb_static" > /data/web_static/releases/test/index.html
echo "Ceci n'est pas une page" > /usr/share/nginx/html/404.html

printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    location /hbnb_static/ {
        alias /data/web_static/current/;
        autoindex off;
    }
    location /redirect_me {
        return 301 http://finalesoft.tech/;
    }
    error_page 404 /404.html;
    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default



service nginx restart
