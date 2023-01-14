#! /bin/bash

#stop all containers
docker stop $(docker ps -a -q)
# docker ps -a
docker rm -f $(docker ps -aq)
docker kill $(docker ps -q)
#docker system prune -a --volumes
#docker system prune -a -f
docker rmi $(docker images -q -f dangling=true)
#docker rmi $(docker images -a -q)

docker rm $(docker ps -aq)





# docker rm $(docker ps -qa)
