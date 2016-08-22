# Start from Vinod' shiny container (based on: https://github.com/rocker-org/shiny/blob/master/Dockerfile)
FROM vinodmang/baylor_app
RUN rm -fr BaylorInteractiveViewer/    # remove the old versions of the shiny
RUN rm -fr /opt/shiny-server/samples/sample-apps/BaylorInteractiveViewer

# For debugging
RUN sudo apt-get install vim -y

# Python/Flask
RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get install -y python python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Copy the shiny to the correct directory and then make sure there aren't permission issues
COPY ./shiny /opt/shiny-server/samples/sample-apps/BaylorInteractiveViewer
RUN chmod 777 -R /opt/shiny-server/samples/sample-apps/BaylorInteractiveViewer
#RUN R -e "install.packages(c('shiny', 'rmarkdown', 'DT', 'shinydashboard', 'jsonlite', 'ggplot2', 'plotly'), dependencies=TRUE, repos='https://cran.rstudio.com/')"

# Setup and run multiple processes with supervisor
# see: https://docs.docker.com/engine/admin/using_supervisord/
RUN apt-get update && apt-get install -y openssh-server apache2 supervisor
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
