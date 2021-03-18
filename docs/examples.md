# Examples


## Example 1: Operator BandMaths

```
band_maths = Operator('BandMaths')

band_maths.describe()
```

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

active_fire_detected float32 S9_BT_in &lt; 265 ? 0 : F1_BT_in > 315 and (F1_BT_in - F2_BT_in) > 15 ? 1 : 0 NaN
```

```
active_fire_band = TargetBand(name='active_fire_detected',
                              expression='S9_BT_in &lt; 265 ? 0 : F1_BT_in &gt; 315 and (F1_BT_in - F2_BT_in) &gt; 15 ? 1 : 0')

active_fire_band
```

```
TargetBand(name='active_fire_detected', expression='S9_BT_in &lt; 265 ? 0 : F1_BT_in &gt; 315 and (F1_BT_in - F2_BT_in) &gt; 15 ? 1 : 0', type='float32', description=None, unit=None, no_data_value='NaN')
```

```
band_maths.targetBandDescriptors = TargetBandDescriptors([active_fire_band])

band_maths.targetBandDescriptors

&lt;snapista.target_band_descriptors.TargetBandDescriptors at 0x7f6a71568850>
```


## Example 2: Operator Subset

```
subset = Operator('Subset')

subset.describe()
```

```
Operator name: Subset

Description: Create a spatial and/or spectral subset of a data product.

Authors: Marco Zuehlke, Norman Fomferra, Marco Peters

org.esa.snap.core.gpf.common.SubsetOp

Version: 1.2

Parameters:

	bandNames: The list of source bands.
		Default Value: None
		Possible values: []

	region: The subset region in pixel coordinates. Use the following format: &lt;x>,&lt;y>,&lt;width>,&lt;height> If not given, the entire scene is used. The 'geoRegion' parameter has precedence over this parameter.
		Default Value: None
		Possible values: []

	referenceBand: The band used to indicate the pixel coordinates.
		Default Value: None
		Possible values: []

	geoRegion: The subset region in geographical coordinates using WKT-format, e.g. POLYGON((&lt;lon1> &lt;lat1>, &lt;lon2> &lt;lat2>, ..., &lt;lon1> &lt;lat1>)) (make sure to quote the option due to spaces in &lt;geometry>). If not given, the entire scene is used.
		Default Value: None
		Possible values: []

	subSamplingX: The pixel sub-sampling step in X (horizontal image direction)
		Default Value: 1
		Possible values: []

	subSamplingY: The pixel sub-sampling step in Y (vertical image direction)
		Default Value: 1
		Possible values: []

	fullSwath: Forces the operator to extend the subset region to the full swath.
		Default Value: false
		Possible values: []

	tiePointGridNames: The comma-separated list of names of tie-point grids to be copied. If not given, all bands are copied.
		Default Value: None
		Possible values: []

	copyMetadata: Whether to copy the metadata of the source product.
		Default Value: false
		Possible values: []
```

```
subset.geoRegion = 'POLYGON((12.76 41.73,12.84 41.73,12.84 41.68,12.76 41.68,12.76 41.73))'

subset
```

```
Operator('Subset', bandNames='None', region='None', referenceBand='None', geoRegion='POLYGON((12.76 41.73,12.84 41.73,12.84 41.68,12.76 41.68,12.76 41.73))', subSamplingX='1', subSamplingY='1', fullSwath='false', tiePointGridNames='None', copyMetadata='false')
```


## Example 3: Create a linear Graph

```
g = Graph() 

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
               source_node_id)

g.view()
```

```
&lt;graph>
  &lt;version>1.0&lt;/version>
  &lt;node id="read_1">
    &lt;operator>Read&lt;/operator>
    &lt;sources/>
    &lt;parameters class="com.bc.ceres.binding.dom.XppDomElement">
      &lt;bandNames/>
      &lt;copyMetadata>true&lt;/copyMetadata>
      &lt;file/>
      &lt;formatName/>
      &lt;geometryRegion/>
      &lt;maskNames/>
      &lt;pixelRegion/>
    &lt;/parameters>
  &lt;/node>
  &lt;node id="band_maths">
    &lt;operator>BandMaths&lt;/operator>
    &lt;sources>
      &lt;sourceProduct refid="read_1"/>
    &lt;/sources>
    &lt;parameters class="com.bc.ceres.binding.dom.XppDomElement">
      &lt;targetBands>
        &lt;targetBand>
          &lt;name>active_fire_detected&lt;/name>
          &lt;expression>S9_BT_in &amp;lt; 265 ? 0 : F1_BT_in &amp;gt; 315 and (F1_BT_in - F2_BT_in) &amp;gt; 15 ? 1 : 0&lt;/expression
          &lt;type>float32&lt;/type>
          &lt;description/>
          &lt;unit/>
          &lt;no_data_value>NaN&lt;/no_data_value>
        &lt;/targetBand>
      &lt;/targetBands>
      &lt;variables/>
    &lt;/parameters>
  &lt;/node>
&lt;/graph>
```

An interactive notebook developed in Binder with some example code is available here: [https://mybinder.org/v2/gh/snap-contrib/snapista/HEAD?urlpath=lab%2Ftree%2Fdemo.ipynb](https://mybinder.org/v2/gh/snap-contrib/snapista/HEAD?urlpath=lab%2Ftree%2Fdemo.ipynb) 
