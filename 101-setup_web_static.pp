# Configures a web server for deployment of web_static.

$nginx_conf = "server {
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
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data':
  ensure  => 'directory'
} ->

file { '/data/web_static':
  ensure => 'directory'
} ->

file { '/data/web_static/releases':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

file { '/data/web_static/shared':
  ensure => 'directory'
} ->

file { 'data/web_static/current':
  ensure => 'absent',
} ->

file { 'data/web_static/current':
  ensure => 'directory',
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
} ->

exec { 'change own':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  path    => ['/bin', '/usr/bin'],
} ->

file { '/data/web_static/releases/test/index.html'
  ensure  => 'file',
  content => '<html> <head></head><body>Khingz </body></html>',
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
  notify  => Service['nginx'],
} ->

exec { 'restart nginx':
  command => 'sudo nginx -t; sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
} ->
