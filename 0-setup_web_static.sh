#!/usr/bin/env bash
# Comment

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Khingz
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
if [ -L "/data/web_static/current" ]; then
    rm "/data/web_static/current"
fi
sudo ln -s "/data/web_static/releases/test" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu /data/
sudo echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /data/web_static/current/;
        index index.html index.htm;
        server_name khingz.tech;
        add_header X-Served-By $HOSTNAME;

        location /hbnb_static/ {
                alias /data/web_static/current/;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        error_page 404 /404_page.html;
        location = /404_page.html {
                root /etc/nginx/html;
                internal;
        }
}" | sudo tee /etc/nginx/sites-available/default > /dev/null
sudo nginx -t
sudo service nginx restart
