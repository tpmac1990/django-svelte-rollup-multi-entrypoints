#!/bin/sh

# used to stop execution instantly as a query exits while having a non-zero status
set -e

# envsubst: takes a file and substitutes all of the syntax '${}' and substitutes with the envirnment variables with that name.
# By default, as this is running as an unprivilaged user so it won't have permission to create the below file, so we do this
# with this line 'touch /etc/nginx/conf.d/default.conf' in the proxy/Dockerfile where are still root permission. It does have permission to 
# write to the file here, just not to create it.
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
# start the nginx server. 'daemon off;' means don't run it as a background, but in the foreground of the container. this is recommended
# when running docker because each docker container should only ever run one application at a time and that should be at the foreground
# of the container so all of the logs that are output to the application get sent to the docker logs so you can see them in the docker logs.
nginx -g 'daemon off;'
