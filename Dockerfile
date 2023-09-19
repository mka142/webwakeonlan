# Section 1- Base Image
FROM python:3.9.12-slim

ENV DRBUG=0
ENV DATA_DIR=/home/webwakeonlan/data

RUN pip install --upgrade pip

# Section 2- Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Section 3- Compiler and OS libraries
RUN apt-get -y update
RUN apt-get -y install iputils-ping

# Section 4- Project libraries and User Creation
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -m -U webwakeonlan 
# Section 5- Code and User Setup

WORKDIR /home/webwakeonlan
USER webwakeonlan:webwakeonlan

COPY --chown=webwakeonlan:webwakeonlan ./webwakeonlan .
RUN mkdir -p ${DATA_DIR}
RUN mkdir -p ${DATA_DIR}/static
RUN chmod +x docker.entrypoint.sh


# Section 6- Docker Run Checks and Configurations
ENTRYPOINT [ "/home/webwakeonlan/docker.entrypoint.sh" ]

