FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

ENV BASH_ENV=~/.bashrc                                       \
    MAMBA_ROOT_PREFIX=/srv/conda                             \
    PATH=/srv/conda/envs/env_snap/bin:/srv/conda/envs/dev/bin:${PATH}                  \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update                                                      && \
    apt-get install -y ca-certificates ttf-dejavu wget bash bzip2  git vim       

COPY . /tmp

# Install basic commands and mamba
RUN wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1 && \
    ./micromamba shell init -s bash -p ~/micromamba                     && \
    apt-get clean autoremove --yes                                      && \
    rm -rf /var/lib/{apt,dpkg,cache,log}                                && \
    cp ./micromamba /usr/bin                                            
    
RUN micromamba create -f /tmp/.devcontainer/dev.environment.yml                           && \
    micromamba create -f /tmp/.devcontainer/environment.yml                      

ARG NB_USER=vscode
ARG NB_UID=1000
ARG HOME=/home/vscode

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    --home ${HOME} \
    --force-badname \
    ${NB_USER}

RUN chown -R vscode:vscode /srv/conda/envs/env_snap