FROM python:3.10.7
MAINTAINER grey thomas
WORKDIR /home/gjt01/Desktop/EA\ Assessment/Docker\ app/
COPY src/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src/ .
CMD [ "python3", "port_code.py", "EA_RESTAPI.py"]
