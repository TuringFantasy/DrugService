#Getting the base OS from Docker. If needed, this can be replaced to get the base OS from any
#private registry. It is highly recommended to have a well tested/hardened base container
#OS image in local private registry and use that below.

#Based OS Image.
FROM centos:centos7

#Maintainer information.
MAINTAINER macaw.io

# SERVICE_SHORT_NAME is the name of the service without the service's namespace and version.
# This environment variable is set by the macawpublish tool automatically based on which service
# is being published.

# The below RUN cmd is trying to link /opt/java/bin/java to /usr/bin/java.
# This assumes that container is mounted with JAVA volume from the host. If needed, java can be locally
# installed within the container. To avoid the image bloating, JRE/JDK directory can be mounted to
# the container and used.

RUN     ln -s /opt/java/bin/java /usr/bin/java && \
        mkdir -p /opt/macaw/${SERVICE_SHORT_NAME} && \
	    yum -y install epel-release && \
	    yum -y install python-pip python-yaml && \
        pip install --upgrade pip && \
	    yum clean all && \
        pip install supervisor requests && \
        echo $'[supervisord]\n\
logfile=/dev/null\n\
pidfile=/var/run/supervisord.pid\n\
loglevel=info\n\
minfds=1024\n\
minprocs=200\n\
nodaemon=true\n\
\n\
[program:${SERVICE_SHORT_NAME}-python] \n\
command=/opt/macaw/${SERVICE_SHORT_NAME}/bin/startup.sh\n\
process_name=%(program_name)s\n\
redirect_stderr=true\n\
stdout_logfile=/dev/stdout\n\
stdout_logfile_maxbytes=0\n\
autorestart=unexpected\n\
exitcodes=0\n\
stopasgroup=true\n\
killasgroup=true\n\
stopsignal=TERM\n\
startretries=10\n\
stopwaitsecs=10\n\
numprocs=1\n\
startsecs=5\n\
priority=800\n\
\n\
[program:${SERVICE_SHORT_NAME}-sidecar]\n\
command=/opt/macaw/${SERVICE_SHORT_NAME}/sidecar/bin/startup.sh\n\
process_name=%(program_name)s\n\
redirect_stderr=true\n\
stdout_logfile=/dev/stdout\n\
stdout_logfile_maxbytes=0\n\
autorestart=unexpected\n\
exitcodes=0\n\
stopasgroup=true\n\
killasgroup=true\n\
stopsignal=TERM\n\
startretries=10\n\
stopwaitsecs=10\n\
numprocs=1\n\
startsecs=5\n\
priority=900' > /etc/supervisord.conf


# The SERVICE_DISTRIBUTION_BINARY is the .tar.gz file created by the service's build.
# This environment variable is set by the macawpublish tool automatically based on which service
# is being published.

# ADD command of docker directly untar the contents into the specific directory. This
# doesnt involve copying the tar package to the container. This helps in not bloating
# the container image size.
# ZIP file artifacts can also be used, but they need to be copied to container first and then unzipped,
# which would require unzip utility and would result in image bloating.
# For more details, refer to docker build commands and best practices for writing Dockerfile

ADD     ${SERVICE_DISTRIBUTION_BINARY} /opt/macaw/${SERVICE_SHORT_NAME}

ENV     MACAW_LOG_CONFIG /opt/macaw/${SERVICE_SHORT_NAME}/py/logging.yaml

#Start the supervisor module which in turns starts/monitors the side car and python.
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
