![msg](http://207.154.246.33/msg1.png)
# http-server
python 2.7
# continuos integration
fully ready!

# nginx_config
```
server {
        server_name 207.154.246.33;
        root /var/www;
        index index.html;
        location / {
                try_files $uri =404;
                expires -1;
        }
}
```
!!@@
