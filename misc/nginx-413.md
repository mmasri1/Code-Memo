
To fix this issue edit the config file of nginx:

```shell
nano /etc/nginx/nginx.conf
```

Add a line in the `http`, `server` or `location` section:

```shell
client_max_body_size 100M;
```

Use M instead of MB, MB will not work. To test the nginx configurations:

```shell
sudo nginx -t
```

Then restart the nginx service:

```shell
sudo systemctl restart nginx
```