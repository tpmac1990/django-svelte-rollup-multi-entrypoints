# us this to build our docker image. Use this one and not the standard nginx image is because this runs as an unprivilaged user. 
# You don't want to be running your main application in docker as the root user, because that's the most powerful user that has
# permission to do anything in the container. So in the case the application is compromised, they will be able to access anything
# the root user can. An unpriviliged user will only be able to access what it has been provided.
FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="londonappdeveloper.com"

# copy the files created in the proxy folder to the docker image
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

# these are the environment variables used in 'default.conf.tpl'
# to save time later on and to set some default variables we can do that in the docker file so there are default values set so you don't
# need to specify them, they become optional if you need to customize them when you can specify them when you run your image or you run 
# your container 
# Because these are environment variables we can customise them when we run the application
# 8000 is the port the nginx server will listen on
ENV LISTEN_PORT=8000
# app is the name of the service that's going to be runninig our container with our django application
ENV APP_HOST=app
# when the django app is setup with the WSGI service we will set it up to use 9000
ENV APP_PORT=9000

# switch to the root user to perform some actions that require root access on the image.
USER root

# mkdir -p /vol/static: create the static file directory 
# chmod 755 /vol/static: change the permissions of the static directory so the owner can read, write and make changes to it.
# touch /etc/nginx/conf.d/default.conf: create the file, this needs to be done here as the user won't have permission whe it
#   is required to be written to in the 'run.sh' file
# chown nginx:nginx /etc/nginx/conf.d/default.conf:
# chmod +x /run.sh: give executable permissions to our run script
RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

# optional. useful for if you decide to deploy your application to a different service like ecs fargate
VOLUME /vol/static

# switch back from the root user to the nginx user
USER nginx

# this sys the command to run new containers of this image should run the run.sh command by default. we don't need to specify in docker-compose
# we just need to run the image and this is the default script that will be run. this can be overrun if necessary.
CMD ["/run.sh"]
