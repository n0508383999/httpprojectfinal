FROM node:10-alpine

RUN apk add --no-cache python python-dev python3 python3-dev \
    linux-headers build-base bash git ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools==45 && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

# syntax=docker/dockerfile:1

#FROM python:3.8-slim-buster


# Step 2 Setting up environment
#RUN apk add --no-cache python3-dev && pip install --upgrade pip
#run pip install --upgrade pip setuptools
# Step 3 Configure a softwar
# Defining working directory
WORKDIR  /app
# Installing dependencies.
COPY /requirements.txt /app

COPY requirements.txt /tmp/
RUN pip3 install --requirement /tmp/requirements.txt
#RUN pip install -r requirements.txt

# Copying project files.
COPY ["app.py", "/app"]
COPY ["*.*", "/app"]

# Exposing an internal port
EXPOSE 5001


# Step 4 set default commands
ENTRYPOINT [ "python3" ] # Default command

# These commands will be replaced if user provides any command by himself
CMD ["app.py"]

