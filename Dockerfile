ARG BASE_IMAGE=selenium/standalone-chrome
# We take BASE_IMAGE as an argument but it will default to Dockerhub if not specified.
FROM $BASE_IMAGE:latest
ARG URL_TO_TEST

WORKDIR /app

ENV URL=$URL_TO_TEST 
 
RUN sudo apt-get update && sudo apt install python3.12-venv -y
RUN python3 -m venv /app/venv 
COPY requirements.txt . 
RUN /app/venv/bin/pip install -r requirements.txt

COPY . . 

CMD [ "/app/venv/bin/python3", "test_script.py" ]
