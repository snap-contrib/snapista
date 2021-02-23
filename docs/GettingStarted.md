# Getting Started


# Import Libraries

```

# Import the entire library

import snapista

# Import specific modules

from snapista import Operator

from snapista import Graph

from snapista import TargetBand

from snapista import TargetBandDescriptors’’’


# Operator

In snapista, an operator is an individual node that embeds specific processing steps. 

Visualise the list of available operators 

```from snapista import Graph

Graph.list_operators()

# List operators with a brief description

Graph().describe_operators()```

Assign Operator, with example of ‘Calibration’

```from snapista import Operator

calibration = Operator('Calibration')```

Visualise the parameters specific to that Operator:

```calibration.describe()```

Print status:

```print(calibration)```


# Graph

The SNAP architecture provides a flexible Graph Processing Framework (GPF) allowing the user to create processing graphs for batch processing and customized processing chains ([http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)).

Graphs allow the user to combine the available operators and connect operator nodes to their sources, for data processing. Graphs can then be saved and batched processed from the GUI or from the command line.

```# Create a Graph

from snapista import Graph

g = Graph()

# Add two nodes

```g.add_node(operator=Operator('Read'), 

           node_id='read_1')

calibration = Operator('Calibration')

calibration.createBetaBand = 'false'

g.add_node(operator=calibration, 

           node_id='calibration', 

           source='read_1')```

Visualise the status of the Graph

```# Visualise the Graph

g.view()

# Print also the path and working directory 

print(g)

# Visualise the operators within  also the path and working directory 

print(g)

Example: Create a linear graph

```g = Graph() 

read = Operator('Read')

read.formatName = 'SENTINEL-1'

read.file = 'some1'

operators = [read,

             'Resample',

             'Reproject',

             'Subset',

             'AddLandCover',

             'Write']

for index, operator in enumerate(operators):

    

    print('Adding Operator {} to graph'.format(operator.operator if isinstance(operator, Operator) else operator))

    if index == 0:            

        source_node_id = ''

    else:

        source_node_id = operators[index - 1].operator if isinstance(operators[index - 1], Operator) else operators[index - 1]

        

        

    g.add_node(operator if isinstance(operator, Operator) else Operator(operator),

               operator.operator if isinstance(operator, Operator) else operator,

               source_node_id)```

An interactive notebook developed in Binder with some example code is available here: [https://mybinder.org/v2/gh/snap-contrib/snapista/HEAD?urlpath=lab%2Ftree%2Fdemo.ipynb](https://mybinder.org/v2/gh/snap-contrib/snapista/HEAD?urlpath=lab%2Ftree%2Fdemo.ipynb) 
