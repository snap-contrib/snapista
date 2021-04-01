# Getting Started

_snapista_ was designed to be simple and easy to learn and use.

This page provides the basic elements to get started with _snapista_.

This short guide is based on the assumption that you are familiar with the SNAP GPT, Graph and Operators concepts. If not, please read the [SNAP command line tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf).

As a SNAP GPT thin layer, the goal of _snapista_ is to ease the creation of SNAP graphs and their execution in Python.

## Importing snapista

As for any other Python package, you can import the entire library with:

```python
import snapista
```

Or the classes individually:

```python
from snapista import Operator, OperatorParams
from snapista import Graph
from snapista import TargetBand, TargetBandDescriptors
```

_snapista_ has a reduced number of classes and concepts introduced below.

## Operator

In snapista, an operator is an individual node that embeds specific processing step. It is a node of a SNAP graph. 

### List the available operators 

To list the SNAP operators, use the Graph class method `list_operators()`:

```python
from snapista import Graph

Graph.list_operators()
```

### Describe the available operators 

To list the SNAP operators, use the Graph class method `describe_operators()`:


```python
from snapista import Graph

Graph.describe_operators() 
```

### Instantiate an Operator

The _snapista_ `Operator` class creates a SNAP operator and it is mainly used to set it parameter values.

To create an _Operator_ object for the ‘Calibration’ SNAP module simply use the SNAP module name in the constructor:

```python 
from snapista import Operator

calibration = Operator('Calibration')
```

With this instantiated operator, you can get its description:

```python
calibration.describe()
```

This will print the parameters specific to that SNAP module:

```
Operator name: Calibration

Description: Calibration of products

Authors: Jun Lu, Luis Veci

org.esa.s1tbx.calibration.gpf.CalibrationOp

Version: 1.0

Parameters:

	sourceBandNames: The list of source bands.
		Default Value: None
		Possible values: []

	auxFile: The auxiliary file
		Default Value: Latest Auxiliary File
		Possible values: ['Latest Auxiliary File', 'Product Auxiliary File', 'External Auxiliary File']

	externalAuxFile: The antenna elevation pattern gain auxiliary data file.
		Default Value: None
		Possible values: []

	outputImageInComplex: Output image in complex
		Default Value: false
		Possible values: []

	outputImageScaleInDb: Output image scale
		Default Value: false
		Possible values: []

	createGammaBand: Create gamma0 virtual band
		Default Value: false
		Possible values: []

	createBetaBand: Create beta0 virtual band
		Default Value: false
		Possible values: []

	selectedPolarisations: The list of polarisations
		Default Value: None
		Possible values: []

	outputSigmaBand: Output sigma0 band
		Default Value: true
		Possible values: []

	outputGammaBand: Output gamma0 band
		Default Value: false
		Possible values: []

	outputBetaBand: Output beta0 band
		Default Value: false
		Possible values: []
```

### Setting an Operator parameter value

To set a parameter value, do:

```python 
from snapista import Operator

calibration = Operator('Calibration')
calibration.createBetaBand = 'false'
```

!!! note
    Boolean are set as string and the value is either `'true'` or `'false'`

## Graph

The SNAP architecture provides a flexible Graph Processing Framework (GPF) allowing the user to create processing graphs for batch processing and customized processing chains (see the [SNAP CommandLine Tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf) to learn more).

Graphs allows you to combine the available operators and connect operator nodes to their sources, for data processing. Graphs can then be saved and executed. 

The main members available for the _snapista_ `Graph` class are:

*   `list_operators`: This class function provides a Python dictionary with all SNAP operators;
*   `describe_operators`: This class function provides a Python dictionary with all SNAP operators with a brief description;
*   `view`: This method prints the SNAP Graph;
*   `add_node`: This method adds or overwrites a node to the SNAP Graph;
*   `save_graph`: This method saves the SNAP Graph with a defined filename;
*   `run` This method runs the SNAP Graph using gpt.

### Create a Graph and add two nodes

To instantiate a _snapista_ `Graph` do:

```python
from snapista import Graph

g = Graph()
```

Add a couple of nodes:

```python
g.add_node(operator=Operator('Read'), 
           node_id='read_1')

calibration = Operator('Calibration')

calibration.createBetaBand = 'false'

g.add_node(operator=calibration, 
           node_id='calibration', 
           source='read_1')
```

Print the SNAP Graph XML representation:

```python
g.view()
```

This will print:

```xml
<graph>
  <version>1.0</version>
  <node id="read_1">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <bandNames/>
      <copyMetadata>true</copyMetadata>
      <file/>
      <formatName/>
      <geometryRegion/>
      <maskNames/>
      <pixelRegion/>
    </parameters>
  </node>
  <node id="calibration">
    <operator>Calibration</operator>
    <sources>
      <sourceProduct refid="read_1"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <auxFile>Latest Auxiliary File</auxFile>
      <createBetaBand>false</createBetaBand>
      <createGammaBand>false</createGammaBand>
      <externalAuxFile/>
      <outputBetaBand>false</outputBetaBand>
      <outputGammaBand>false</outputGammaBand>
      <outputImageInComplex>false</outputImageInComplex>
      <outputImageScaleInDb>false</outputImageScaleInDb>
      <outputSigmaBand>true</outputSigmaBand>
      <selectedPolarisations/>
      <sourceBandNames/>
    </parameters>
  </node>
</graph>
```

### Load an existing graph

snapista can create a `Graph` object from an  existing graph XML file (either local or on HTTP).

Example:

```python

from snapista import * 

g = read_file("https://gist.githubusercontent.com/fabricebrito/fe7df152e9f0df3a3ff6d3974b87e9e2/raw/294b5d8fec9b2b1d4fdc7468611c9bb7756f9e7a/graph.xml")

g.view()

g.add_node(
        operator=Operator(
            "Read",
            formatName="DIMAP",
            file='a file',
        ),
        node_id="read",
    )

g.view()
```


## Using BandMath

In _snapista_, the SNAP BandMath module requires a sligthly different approach as the developer needs to create `TargetBand` and then create the `BandMath` node.

First create a `BandMath` operator with:

```python
band_maths = Operator('BandMaths')
```

Get its description with:

```python
band_maths.describe()
```

This returns:

```
Operator name: BandMaths

Description: Create a product with one or more bands using mathematical expressions.
Authors: Marco Zuehlke, Norman Fomferra, Marco Peters

org.esa.snap.core.gpf.common.BandMathsOp
Version: 1.1

Parameters:

	targetBandDescriptors: List of descriptors defining the target bands.
		Default Value: None

		Possible values: []

	variables: List of variables which can be used within the expressions.
		Default Value: None

		Possible values: []
```

Then create a `TargetBand` with:

```python
active_fire_band = TargetBand(name='active_fire_detected',
                              expression='S9_BT_in > 265 ? 0 : F1_BT_in > 315 and (F1_BT_in - F2_BT_in) > 15 ? 1 : 0')
```

Finally associate the `TargetBand` instance to the `BandMaths` operator as a `List` with:

```python
band_maths.targetBandDescriptors = TargetBandDescriptors([active_fire_band])
```


The _snapista_ `TargetBand` class used above allows to define an object that can be used with the `BandMath` operator

The following attributes are defined in a _snapista_ `TargetBand` object: 

```
name = attr.ib()
expression = attr.ib()
type = attr.ib('float32')
description = attr.ib(default=None)
unit = attr.ib(default=None)
no_data_value = attr.ib(default="NaN")
```

