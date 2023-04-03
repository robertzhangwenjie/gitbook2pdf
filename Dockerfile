FROM python:3.9.7-slim-bullseye

RUN echo """deb http://mirrors.ustc.edu.cn/debian stable main contrib non-free \
deb http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free \
deb http://mirrors.ustc.edu.cn/debian-security stable-security main contrib non-free""" > /etc/apt/sources.list

RUN apt update \
    && apt-get install -y ttf-mscorefonts-installer fontconfig \
    && apt-get install ttf-wqy-microhei ttf-wqy-zenhei

ENV LANG=zh_CN.UTF-8 LANGUAGE=zh_CN.UTF-8 

RUN apt-get install -y locales \
    && dpkg-reconfigure --frontend=noninteractive locales 

RUN  rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

ENTRYPOINT [ "python","gitbook.py" ]


