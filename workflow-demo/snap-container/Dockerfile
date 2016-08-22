FROM ubuntu
RUN apt-get update
RUN apt-get -f install
RUN apt-get -y install wget
RUN apt-get install -y python python-pip wget
RUN wget --no-check-certificate https://snap.stanford.edu/releases/snap-1.2-2.4-centos6.5-x64-py2.6.tar.gz
RUN tar -xvf snap-1.2-2.4-centos6.5-x64-py2.6.tar.gz
RUN rm -rf snap-1.2-2.4-centos6.5-x64-py2.6.tar.gz

RUN  cd snap-1.2-2.4-centos6.5-x64-py2.6;python setup.py install

RUN wget --no-check-certificate https://snap.stanford.edu/data/facebook_combined.txt.gz
RUN gunzip facebook_combined.txt.gz
#RUN rm -rf facebook_combined.txt.gz
#RUN apt-get install -y git


# also for the demo, igraph!
RUN apt-get install -y python-igraph


RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]




