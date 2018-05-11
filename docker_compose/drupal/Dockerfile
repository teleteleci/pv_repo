FROM drupal:8.2

RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/list/*

WORKDIR /war/www/html/themes

RUN git clone --branch 8.x-3.x --single-branch --dept 1 https://git.drupal.org/project/bootstrap.git \
    && chown -R www-data:www-data bootstrap

WORKDIR /war/www/html
