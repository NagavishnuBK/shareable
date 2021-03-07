FROM ubuntu:18.04
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python
RUN apt-get install -y curl
RUN apt-get install -y nano
RUN pip3 install flask
RUN pip3 install requests
EXPOSE 5000 
ENTRYPOINT [ "python3" ] 
CMD [ "run_app.py" ]
