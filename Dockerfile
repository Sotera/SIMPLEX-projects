FROM alejandroniculescu/ddlite
##The original ddlite container is adapted from joyvan's jupyter and contains the 
ddlite installation amongst other components


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

#David's fix (we should probably ask a rebase from stanford later)
# Install the coreNLP parser
RUN rm -rf /home/jovyan/work/ddlite/parser
RUN wget -nc http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip
RUN unzip stanford-corenlp-full-2015-12-09.zip
RUN mv stanford-corenlp-full-2015-12-09 /home/jovyan/work/ddlite/parser



#things to troubleshoot / worth mentioning
#virtualbox -> enable nat ip forwarding on the vm
#https://docs.docker.com/engine/userguide/networking/default_network/custom-docker0/

#ps -ef | grep 'mindtagger' // expose [pid]
#add a pointer to the exposed port for the session