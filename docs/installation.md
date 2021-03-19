# Install

## Linux

_snapista_ is a conda package available under Terradue conda channel.

To install _snapista_, use `conda` (slower) or `mamba` (faster) to install snapista.

On a terminal, run:

```conda install -c terradue snapista```

From your Python script/notebook, you can now import snapista and use its modules. 

Refer to the [getting started](../gettingstarted/) documentation for more information.

## Windows and Mac OS

_snapista_ relies on SNAP packaged as a conda package called `snap-conda`. 

The conda package is available at https://anaconda.org/Terradue/snap.

The software repository hosting the SNAP conda package recipe is available at: https://github.com/snap-contrib/snap-conda

The goal of this conda packaging is to ease the installation on headless systems like a docker container or Linux terminal. 

With this context, using _snapista_ on Windows and Mac OS follows different approaches:

- Using docker with the image https://github.com/snap-contrib/docker-snap
- Using docker and a Jupyter/Theia IDE playground https://github.com/snap-contrib/docker-snap-jpn-theia
- Using Visual Studio Remote Containers, see https://github.com/snap-contrib/vscode-remote-snap

