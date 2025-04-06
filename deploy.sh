# Shell script to deploy the application
#!/bin/bash

# build the docker image
docker build -t pipol_challenge:latest .

# run the docker container
docker run pipol_challenge:latest
