# SNAPISTA

The ESA Sentinel Applications Platform, or SNAP for short ([https://step.esa.int/main/toolboxes/snap/](https://step.esa.int/main/toolboxes/snap/)), is a free and open toolbox for processing data products from numerous satellite missions such as the EU’s Copernicus Sentinel-1, Sentinel-2 and Sentinel-3, as well as ESA’s SMOS mission, and ‘Third Party Missions’. Third Party Missions describe missions for which ESA uses its multimission ground systems to acquire, process, distribute and archive data from satellites owned by other organisations than ESA.

SNAP is distributed together with a Python language interface called snappy, however this interface is lacking in terms of performance and ease of use (far from a python language style).

The community has replied to this by creating numerous wrappers around the SNAP execution engine (GPT) command.

This documentation refers to yet another SNAP GPT Python wrapper called _snapista_. The goal of _snapista_ is to:

*   ease the programmatic generation of SNAP GPT graphs in a Pythonic way
*   provide access to all operators of all existing toolboxes
*   ease the processing of these graphs with methods wrapping the system call to the SNAP GPT command

A few documents and links of interest are:

*   The [installation guide](installation/). 
*   A [getting started](../gettingstarted/) section with an introduction to snapista including some examples .
*   An [interactive notebook developed for Binder](https://mybinder.org/v2/gh/snap-contrib/snapista/HEAD?urlpath=lab%2Ftree%2Fdemo.ipynb with a few code snippets  
*   The [snapista software repository](https://github.com/snap-contrib/snapista)  

