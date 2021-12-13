FROM wordpress

VOLUME /Data

ENV   WORDPRESS_DB_HOST=wp-db:3306 \
      WORDPRESS_DB_USER=wp_user \
      WORDPRESS_DB_PASSWORD=wordpress \
      WORDPRESS_DB_NAME=wordpress

COPY small-app.py /usr/lib/cgi-bin/small-app.py
COPY small-app.py /usr/lib/cgi-bin/testpage.py
RUN chmod +x /usr/lib/cgi-bin/*.py

RUN apt-get update && apt-get install python3
RUN apt-get install pip3
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade mysql-connector
RUN pip3 install --upgrade tabulate

RUN a2enmod cgid

# sudo ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/



