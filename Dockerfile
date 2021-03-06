FROM centos:7

RUN echo "Install build environment software..."

# TODO: install gcc and related packages

# Utilities
RUN yum install -y screen tcpdump make
# GCC
RUN yum install -y gcc
# RPM development
RUN yum install -y rpmdevtools rpm-build
RUN yum clean all

# Install Go 1.10
RUN curl -s https://dl.google.com/go/go1.10.1.linux-amd64.tar.gz > /go.tar.gz
RUN tar xfz /go.tar.gz
RUN mv /go /opt/go
RUN rm /go.tar.gz
# Set go dir
ENV GOROOT /opt/go
RUN mkdir /goproj
ENV GOPATH /goproj
# Set up system-wide PATH variables in the global profile
RUN echo 'export PATH=$PATH:/opt/go/bin' > /etc/profile.d/go.sh

RUN echo "Installation completed"

EXPOSE 8000 8080 9090
