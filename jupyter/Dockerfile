From jupyter/datascience-notebook 
MAINTAINER Masashi Shibata <contact@c-bata.link>

USER root
RUN apt-get update && \
    apt-get install -y graphviz-dev graphviz && \
    rm -rf /var/lib/apt/lists/*

USER jovyan
COPY requirements.txt ./
RUN pip install -r requirements.txt