# SNAPISTA - A SNAP GPT Python wrapper

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

## About

The ESA Sentinel Applications Platform, or SNAP for short, is a free and open toolbox for processing data products from numerous satellite missions such as the EU’s Copernicus Sentinel-1, Sentinel-2 and Sentinel-3, as well as ESA’s SMOS mission, and ‘Third Party Missions’. Third Party Missions describe missions for which ESA uses its multimission ground systems to acquire, process, distribute and archive data from satellites owned by other organisations than ESA.

SNAP is distributed together with a Python language interface called snappy, however this interface is lacking in terms of performance and ease of use (far from a python language style). 

The community has replied to this by creating numerous wrappers around the SNAP execution engine (GPT) command.  

This repository contains yet another SNAP GPT Python wrapper.

This SNAP GPT Python wrapper goal is to:

- ease the programmatic generation of SNAP GPT graphs in a Pythonic way
- provide access to all operators of all existing toolboxes
- ease the processing of these graphs with methods wrapping the system call to the SNAP GPT command

## Installation

Use conda or mamba to install snapista:

```console
conda install -c terradue snapista
```

## Getting started

Run the demo note on Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/snap-contrib/snapista/HEAD?urlpath=lab%2Ftree%2Fdemo.ipynb)
