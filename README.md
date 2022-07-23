# docker-dash
![Ci Status](https://github.com/declan-wade/docker-dash/actions/workflows/docker-image.yml/badge.svg)
A very lightweight web-based GUI for Docker written in Python with Bootstrap 5

## Run:

```docker run -d --name=dockerdash -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 gundamire/dockerdash:latest```
