FROM python:3.10.7
MAINTAINER Grey Thomas
WORKDIR /home/gjt01/Desktop/EA\ Assessment/Docker\ app/
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "port_code.py", "EA_RESTAPI.py"]
