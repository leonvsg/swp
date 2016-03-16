sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE ask;"
sudo python ask/manage.py validate
sudo python ask/manage.py syncdb