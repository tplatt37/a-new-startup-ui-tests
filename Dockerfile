ARG BASE_IMAGE=selenium/standalone-chrome
# We take BASE_IMAGE as an argument but it will default to Dockerhub if not specified.
FROM $BASE_IMAGE:latest
ARG URL_TO_TEST

WORKDIR /usr/src/app

ENV URL=$URL_TO_TEST 
 
RUN sudo apt-get update && sudo apt-get install python3-pip -y && pip install selenium

COPY . . 

CMD [ "python3", "test_script.py" ]
