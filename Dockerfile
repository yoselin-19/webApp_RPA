FROM ubuntu:18.04 
RUN apt-get update
RUN apt-get install python3 python3-pip sqlite3 nano -y
ADD . /webApp_RPA
WORKDIR /webApp_RPA
RUN pip3 install Flask
RUN chmod 777 run.sh
RUN python3 init_db.py
CMD sh ./run.sh
EXPOSE 80
