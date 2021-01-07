FROM ubuntu:20.04

MAINTAINER Terradue S.r.l
USER root

ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    SHELL=/bin/bash \
    PATH=/srv/conda/bin:$PATH \
    DEBIAN_FRONTEND=noninteractive \
    NB_USER=jovyan \
    NB_UID=1002 \
    NB_GID=1002

    
ENV USER=${NB_USER} \ 
    HOME=/home/${NB_USER}
    
RUN groupadd --gid ${NB_GID} ${NB_USER}                                                                                             && \
    useradd --comment "Default user" --create-home --gid ${NB_GID} --no-log-init --shell /bin/bash --uid ${NB_UID} ${NB_USER}

RUN apt-get -qq update                                                                                                              && \
    apt-get -qq install --yes apt-utils 

RUN apt-get -qq update                                                                                                              && \
    apt-get -qq install --yes --no-install-recommends ttf-dejavu wget make g++ sudo vim less unzip tree file locales git procps > /dev/null              && \
    apt-get -qq purge                                                                                                               && \
    apt-get -qq clean                                                                                                               && \
    rm -rf /var/lib/apt/lists/*

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment                                                                                   && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen                                                                                     && \
    echo "LANG=en_US.UTF-8" > /etc/locale.conf                                                                                      && \
    locale-gen en_US.UTF-8

ENV APP_BASE=/srv 

ENV CONDA_DIR=${APP_BASE}/conda 

# conda installation via miniforge
ADD .docker/install-miniforge.bash /tmp/install-miniforge.bash

RUN chmod 755 /tmp/install-miniforge.bash                                                                                           && \
    /tmp/install-miniforge.bash                                                                                                     && \
    rm -f /tmp/install-*.bash 

# setup the python dev tools
RUN mamba install -n base -y black flake8 pylint autopep8 mypy yapf bandit pycodestyle pydocstyle pylint

# fix permissions
RUN chown -R $NB_USER:$NB_GID ${HOME} 

RUN mkdir /workspace
RUN chown -R $NB_USER:$NB_GID /workspace

RUN git config --global http.sslverify false

WORKDIR /workspace

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER ${NB_USER}

ENV NB_PYTHON_PREFIX=${CONDA_DIR}/envs/env_snap 

ENV PATH=${NB_PYTHON_PREFIX}/snap/bin:${NB_PYTHON_PREFIX}/bin:$CONDA_DIR/bin:$PATH \
    KERNEL_PYTHON_PREFIX=${NB_PYTHON_PREFIX} \
    PREFIX=${NB_PYTHON_PREFIX}

ADD environment.yml /tmp/environment.yml

RUN mamba env create -f /tmp/environment.yml                                                                 && \
    mamba clean --all -f -y







#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# FROM continuumio/anaconda3

# # Copy default endpoint specific user settings overrides into container to specify Python path
# COPY .devcontainer/settings.vscode.json /root/.vscode-remote/data/Machine/settings.json

# # Install git, process tools
# RUN apt-get update && apt-get -y install git procps

# RUN mkdir /workspace
# WORKDIR /workspace

# # Install Python dependencies from requirements.txt if it exists
# COPY .devcontainer/environment.yml.temp environment.yml* /workspace/
# RUN if [ -f "environment.yml" ]; then conda env update base -f environment.yml && rm environment.yml*; fi

# # Clean up
# RUN apt-get autoremove -y \
#     && apt-get clean -y \
#     && rm -rf /var/lib/apt/lists/*

