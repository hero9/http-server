server {
        server_name 207.154.246.33;
        root /var/www;
        index index.html;
        location / {
                try_files $uri =404;
                expires -1;
        }
}