# Go Centos Build

## Overview

This repo has ``Dockerfile`` that creates environment to build and test golang services.

This environment is comprised of centos + systemd, go 1.10, rpm tools and a few extra utilities such as tcpdump and screen.

## Docker Operations

### How to build image

```bash
docker build -t godev-centos:7.0 .
```

## How to run it

If all that you need is a bash shell then do the following:

```bash
docker run -it godev-centos:7.0 /bin/bash
```

The same, but with mapped ``$GOPATH/src`` folder:

```bash
docker run -it --mount type=bind,source=$GOPATH/src,target=/goproj/src godev-centos:7.0 /bin/bash
```

The command above maps ``$GOPATH/src`` onto ``/goproj/src``. Note, that container maps it's internal ``GOPATH`` onto ``/goproj``.

## How to run test services within it

If you need ``systemd`` and be able to build you local go sources then do the following:

```bash
docker run -d -e=container=docker --stop-signal=SIGRTMIN+3 --cap-add=SYS_ADMIN --security-opt=seccomp:unconfined -v /sys/fs/cgroup:/sys/fs/cgroup:ro --mount type=bind,source=$GOPATH/src,target=/goproj/src godev-centos:7.0 /sbin/init
```

## Links

* [Docker cleanup guide](https://gist.github.com/bastman/5b57ddb3c11942094f8d0a97d461b430)
