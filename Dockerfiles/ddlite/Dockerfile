FROM alejandroniculescu/ddlite
##The original ddlite container is adapted from joyvan's jupyter and contains the ddlite installation amongst other components


USER root

# add webupd8 repository
RUN \
    echo "===> add webupd8 repository..."  && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list  && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  && \
    apt-get update  && \
    \
    \
    echo "===> install Java"  && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
    DEBIAN_FRONTEND=noninteractive  apt-get install -y --force-yes oracle-java8-installer oracle-java8-set-default  && \
    \
    \
    echo "===> clean up..."  && \
    rm -rf /var/cache/oracle-jdk8-installer  && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/*

# David's fix (we should probably ask a rebase from stanford later)
# Install the coreNLP parser 
RUN rm -rf /home/jovyan/work/ddlite/parser
RUN wget -nc http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip
RUN unzip stanford-corenlp-full-2015-12-09.zip
RUN mv stanford-corenlp-full-2015-12-09 /home/jovyan/work/ddlite/parser

#Just in case, curl
RUN apt-get -qq update ; apt-get -qq -y install curl

# Ugly hack to get mindtagger work ... fix the port used and get the machine IP addr from an environment variable that I specify at container start
RUN  sed 's/socket.gethostname()/os.environ.get("MY_HOST")/' /home/jovyan/work/ddlite/ddlite_mindtagger.py | sed 's/hash(pwd.getpwuid(os.getuid()).pw_name) % 1000 + 8000/8889/' > /home/jovyan/work/ddlite/tmp
RUN mv /home/jovyan/work/ddlite/tmp /home/jovyan/work/ddlite/ddlite_mindtagger.py 

# Pre-install mindtagger so that we don't need to download code during the demo
RUN export PREFIX="/home/jovyan/work/ddlite/examples/deepdive"
RUN wget  -qO- git.io/getdeepdive > /home/jovyan/work/ddlite/examples/installer.sh
RUN PREFIX="/home/jovyan/work/ddlite/examples/deepdive" bash /home/jovyan/work/ddlite/examples/installer.sh deepdive_from_release

