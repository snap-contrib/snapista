# Getting Started


## Import Libraries

```
# Import the entire library
import snapista

# Import specific modules
from snapista import Operator, OperatorParams
from snapista import Graph
from snapista import TargetBand, TargetBandDescriptors
```


## Class: Operator

In snapista, an operator is an individual node that embeds specific processing steps. 

Visualise the list of available operators 

```
from snapista import Graph

Graph.list_operators() # List operators 
Graph.describe_operators() # List with a brief description
```

List of available Operators:


<table>
  <tr>
   <td>AATSR.Ungrid
   </td>
   <td>Forest-Area-Classification
   </td>
   <td>MsaviOp
   </td>
   <td>SAR-Simulation
   </td>
  </tr>
  <tr>
   <td>ALOS-Deskewing
   </td>
   <td>Forest-Area-Detection
   </td>
   <td>MtciOp
   </td>
   <td>SARSim-Terrain-Correction
   </td>
  </tr>
  <tr>
   <td>Aatsr.SST
   </td>
   <td>ForestCoverChangeOp
   </td>
   <td>Multi-Temporal-Speckle-Filter
   </td>
   <td>SM-Dielectric-Modeling
   </td>
  </tr>
  <tr>
   <td>AdaptiveThresholding
   </td>
   <td>FuClassification
   </td>
   <td>Multi-sizeMosaic
   </td>
   <td>SRGR
   </td>
  </tr>
  <tr>
   <td>AddElevation
   </td>
   <td>GLCM
   </td>
   <td>MultiMasterStackGenerator
   </td>
   <td>SaviOp
   </td>
  </tr>
  <tr>
   <td>AddLandCover
   </td>
   <td>GRD-Post
   </td>
   <td>Multilook
   </td>
   <td>SetNoDataValue
   </td>
  </tr>
  <tr>
   <td>Apply-Orbit-File
   </td>
   <td>GaborFilter
   </td>
   <td>Ndi45Op
   </td>
   <td>SimulateAmplitude
   </td>
  </tr>
  <tr>
   <td>Arc.SST
   </td>
   <td>GaseousAbsorption
   </td>
   <td>NdpiOp
   </td>
   <td>SliceAssembly
   </td>
  </tr>
  <tr>
   <td>ArviOp
   </td>
   <td>GemiOp
   </td>
   <td>NdtiOp
   </td>
   <td>SmacOp
   </td>
  </tr>
  <tr>
   <td>Azimuth-Shift-Estimation-ESD
   </td>
   <td>GenericRegionMergingOp
   </td>
   <td>NdviOp
   </td>
   <td>SmileCorrection.Olci
   </td>
  </tr>
  <tr>
   <td>AzimuthFilter
   </td>
   <td>GndviOp
   </td>
   <td>Ndwi2Op
   </td>
   <td>SnaphuExport
   </td>
  </tr>
  <tr>
   <td>Back-Geocoding
   </td>
   <td>GoldsteinPhaseFiltering
   </td>
   <td>NdwiOp
   </td>
   <td>SnaphuImport
   </td>
  </tr>
  <tr>
   <td>BandMaths
   </td>
   <td>IEM-Hybrid-Inversion
   </td>
   <td>OWTClassification
   </td>
   <td>Speckle-Divergence
   </td>
  </tr>
  <tr>
   <td>BandMerge
   </td>
   <td>IEM-Multi-Angle-Inversion
   </td>
   <td>Object-Discrimination
   </td>
   <td>Speckle-Filter
   </td>
  </tr>
  <tr>
   <td>BandSelect
   </td>
   <td>IEM-Multi-Pol-Inversion
   </td>
   <td>Offset-Tracking
   </td>
   <td>SpectralAngleMapperOp
   </td>
  </tr>
  <tr>
   <td>BandsDifferenceOp
   </td>
   <td>Image-Filter
   </td>
   <td>Oil-Spill-Clustering
   </td>
   <td>Stack-Averaging
   </td>
  </tr>
  <tr>
   <td>BandsExtractorOp
   </td>
   <td>Import-Vector
   </td>
   <td>Oil-Spill-Detection
   </td>
   <td>Stack-Split
   </td>
  </tr>
  <tr>
   <td>Bi2Op
   </td>
   <td>IntegerInterferogram
   </td>
   <td>OlciO2aHarmonisation
   </td>
   <td>StampsExport
   </td>
  </tr>
  <tr>
   <td>BiOp
   </td>
   <td>Interferogram
   </td>
   <td>Orientation-Angle-Correction
   </td>
   <td>StatisticsOp
   </td>
  </tr>
  <tr>
   <td>Binning
   </td>
   <td>IpviOp
   </td>
   <td>Oversample
   </td>
   <td>StoredGraph
   </td>
  </tr>
  <tr>
   <td>Biophysical10mOp
   </td>
   <td>IreciOp
   </td>
   <td>PCA
   </td>
   <td>SubGraph
   </td>
  </tr>
  <tr>
   <td>BiophysicalLandsat8Op
   </td>
   <td>KDTree-KNN-Classifier
   </td>
   <td>PassThrough
   </td>
   <td>Subset
   </td>
  </tr>
  <tr>
   <td>BiophysicalOp
   </td>
   <td>KMeansClusterAnalysis
   </td>
   <td>PduStitching
   </td>
   <td>Supervised-Wishart-Classification
   </td>
  </tr>
  <tr>
   <td>CP-Decomposition
   </td>
   <td>KNN-Classifier
   </td>
   <td>PhaseToDisplacement
   </td>
   <td>TOPSAR-Deburst
   </td>
  </tr>
  <tr>
   <td>CP-Simulation
   </td>
   <td>L3ToL1
   </td>
   <td>PhaseToElevation
   </td>
   <td>TOPSAR-DerampDemod
   </td>
  </tr>
  <tr>
   <td>CP-Stokes-Parameters
   </td>
   <td>Land-Cover-Mask
   </td>
   <td>PhaseToHeight
   </td>
   <td>TOPSAR-Merge
   </td>
  </tr>
  <tr>
   <td>Calibration
   </td>
   <td>Land-Sea-Mask
   </td>
   <td>PixEx
   </td>
   <td>TOPSAR-Split
   </td>
  </tr>
  <tr>
   <td>Change-Detection
   </td>
   <td>LandWaterMask
   </td>
   <td>Polarimetric-Classification
   </td>
   <td>TemporalPercentile
   </td>
  </tr>
  <tr>
   <td>CiOp
   </td>
   <td>LinearToFromdB
   </td>
   <td>Polarimetric-Decomposition
   </td>
   <td>Terrain-Correction
   </td>
  </tr>
  <tr>
   <td>CloudProb
   </td>
   <td>Maximum-Likelihood-Classifier
   </td>
   <td>Polarimetric-Matrices
   </td>
   <td>Terrain-Flattening
   </td>
  </tr>
  <tr>
   <td>Coherence
   </td>
   <td>McariOp
   </td>
   <td>Polarimetric-Parameters
   </td>
   <td>Terrain-Mask
   </td>
  </tr>
  <tr>
   <td>Collocate
   </td>
   <td>Mci.s2
   </td>
   <td>Polarimetric-Speckle-Filter
   </td>
   <td>TestPattern
   </td>
  </tr>
  <tr>
   <td>Compute-Slope-Aspect
   </td>
   <td>Merge
   </td>
   <td>PpeFiltering
   </td>
   <td>ThermalNoiseRemoval
   </td>
  </tr>
  <tr>
   <td>Convert-Datatype
   </td>
   <td>Meris.AerosolMerger
   </td>
   <td>Principle-Components
   </td>
   <td>Three-passDInSAR
   </td>
  </tr>
  <tr>
   <td>CoregistrationOp
   </td>
   <td>Meris.BlueBand
   </td>
   <td>ProductSet-Reader
   </td>
   <td>TileCache
   </td>
  </tr>
  <tr>
   <td>CreateStack
   </td>
   <td>Meris.Brr
   </td>
   <td>PssraOp
   </td>
   <td>TileWriter
   </td>
  </tr>
  <tr>
   <td>Cross-Channel-SNR-Correction
   </td>
   <td>Meris.CloudClassification
   </td>
   <td>PviOp
   </td>
   <td>TndviOp
   </td>
  </tr>
  <tr>
   <td>Cross-Correlation
   </td>
   <td>Meris.CloudProbability
   </td>
   <td>PyOp
   </td>
   <td>ToolAdapterOp
   </td>
  </tr>
  <tr>
   <td>CrossResampling
   </td>
   <td>Meris.CloudShadow
   </td>
   <td>RRToFRS
   </td>
   <td>TopoPhaseRemoval
   </td>
  </tr>
  <tr>
   <td>DEM-Assisted-Coregistration
   </td>
   <td>Meris.CloudTopPressureOp
   </td>
   <td>Rad2Refl
   </td>
   <td>TsaviOp
   </td>
  </tr>
  <tr>
   <td>Data-Analysis
   </td>
   <td>Meris.CombinedCloud
   </td>
   <td>Random-Forest-Classifier
   </td>
   <td>Undersample
   </td>
  </tr>
  <tr>
   <td>DeburstWSS
   </td>
   <td>Meris.CorrectRadiometry
   </td>
   <td>RangeFilter
   </td>
   <td>Unmix
   </td>
  </tr>
  <tr>
   <td>DecisionTree
   </td>
   <td>Meris.GapLessSdr
   </td>
   <td>RayleighCorrection
   </td>
   <td>Update-Geo-Reference
   </td>
  </tr>
  <tr>
   <td>Demodulate
   </td>
   <td>Meris.GaseousCorrection
   </td>
   <td>Read
   </td>
   <td>Warp
   </td>
  </tr>
  <tr>
   <td>Double-Difference-Interferogram
   </td>
   <td>Meris.LandClassification
   </td>
   <td>ReflectanceToRadianceOp
   </td>
   <td>WdviOp
   </td>
  </tr>
  <tr>
   <td>DviOp
   </td>
   <td>Meris.Mod08Aerosol
   </td>
   <td>ReipOp
   </td>
   <td>Wind-Field-Estimation
   </td>
  </tr>
  <tr>
   <td>EAP-Phase-Correction
   </td>
   <td>Meris.N1Patcher
   </td>
   <td>Remodulate
   </td>
   <td>Write
   </td>
  </tr>
  <tr>
   <td>EMClusterAnalysis
   </td>
   <td>Meris.RayleighCorrection
   </td>
   <td>RemoteExecutionOp
   </td>
   <td>WriteRGB
   </td>
  </tr>
  <tr>
   <td>Ellipsoid-Correction-GG
   </td>
   <td>Meris.Sdr
   </td>
   <td>Remove-GRD-Border-Noise
   </td>
   <td>c2rcc
   </td>
  </tr>
  <tr>
   <td>Ellipsoid-Correction-RD
   </td>
   <td>Meris.SmileCorrection
   </td>
   <td>RemoveAntennaPattern
   </td>
   <td>c2rcc.landsat7
   </td>
  </tr>
  <tr>
   <td>Enhanced-Spectral-Diversity
   </td>
   <td>Minimum-Distance-Classifier
   </td>
   <td>ReplaceMetadata
   </td>
   <td>c2rcc.landsat8
   </td>
  </tr>
  <tr>
   <td>FUB.Water
   </td>
   <td>MndwiOp
   </td>
   <td>Reproject
   </td>
   <td>c2rcc.meris
   </td>
  </tr>
  <tr>
   <td>Fill-DEM-Hole
   </td>
   <td>MoreThenAnIntegerOp
   </td>
   <td>Resample
   </td>
   <td>c2rcc.meris4
   </td>
  </tr>
  <tr>
   <td>FillAerosol
   </td>
   <td>Mosaic
   </td>
   <td>RiOp
   </td>
   <td>c2rcc.modis
   </td>
  </tr>
  <tr>
   <td>FillBand
   </td>
   <td>MphChl
   </td>
   <td>RviOp
   </td>
   <td>c2rcc.msi
   </td>
  </tr>
  <tr>
   <td>Find-Image-Pair
   </td>
   <td>MphChlBasis
   </td>
   <td>S2Resampling
   </td>
   <td>c2rcc.olci
   </td>
  </tr>
  <tr>
   <td>FlhMci
   </td>
   <td>MphChlMeris
   </td>
   <td>S2repOp
   </td>
   <td>c2rcc.seawifs
   </td>
  </tr>
  <tr>
   <td>Flip
   </td>
   <td>MphChlOlci
   </td>
   <td>S2tbx-Reproject
   </td>
   <td>c2rcc.viirs
   </td>
  </tr>
  <tr>
   <td>Flood-Detection
   </td>
   <td>Msavi2Op
   </td>
   <td>SAR-Mosaic
   </td>
   <td>
   </td>
  </tr>
</table>


Assign Operator, using the example of ‘Calibration’

```
from snapista import Operator

calibration = Operator('Calibration')
calibration.describe()
```

Visualise the parameters specific to that Operator:

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


## Class: Graph

The SNAP architecture provides a flexible Graph Processing Framework (GPF) allowing the user to create processing graphs for batch processing and customized processing chains ([http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)).

Graphs allow the user to combine the available operators and connect operator nodes to their sources, for data processing. Graphs can then be saved and batched processed from the GUI or from the command line.

The main functions available for the Graph class are:



*   ```list_operators()```: This function provides a Python dictionary with all SNAP operators;
*   ```describe_operators()```: This function provides a Python dictionary with all SNAP operators with a brief description;
*   ```view()```: This method prints the SNAP Graph;
*   ```add_node(operator, node_id, source)```: This method adds or overwrites a node to the SNAP Graph;
*   ```save_graph(filename)```: This method saves the SNAP Graph with a defined finelname;
*   ```run(gpt_options=["-x", "-c", "1024M"])``` This method runs the SNAP Graph using gpt.

Create a Graph and add two nodes

```
# Create a Graph

from snapista import Graph

g = Graph()

# Add two nodes

g.add_node(operator=Operator('Read'), 
           node_id='read_1')

calibration = Operator('Calibration')

calibration.createBetaBand = 'false'

g.add_node(operator=calibration, 
           node_id='calibration', 
           source='read_1')
```

Visualise the status of the Graph

```
# Visualise the Graph
g.view()

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
  &lt;node id="calibration">
    &lt;operator>Calibration&lt;/operator>
    &lt;sources>
      &lt;sourceProduct refid="read_1"/>
    &lt;/sources>
    &lt;parameters class="com.bc.ceres.binding.dom.XppDomElement">
      &lt;auxFile>Latest Auxiliary File&lt;/auxFile>
      &lt;createBetaBand>false&lt;/createBetaBand>
      &lt;createGammaBand>false&lt;/createGammaBand>
      &lt;externalAuxFile/>
      &lt;outputBetaBand>false&lt;/outputBetaBand>
      &lt;outputGammaBand>false&lt;/outputGammaBand>
      &lt;outputImageInComplex>false&lt;/outputImageInComplex>
      &lt;outputImageScaleInDb>false&lt;/outputImageScaleInDb>
      &lt;outputSigmaBand>true&lt;/outputSigmaBand>
      &lt;selectedPolarisations/>
      &lt;sourceBandNames/>
    &lt;/parameters>
  &lt;/node>
&lt;/graph>

# Print also the path and working directory 
print(g)
```


## Class: TargetBand

The TargetBand class allows to define an object that can be used in the Operators. The following attributes are defined in a TargetBand Object: 

```
name = attr.ib()
expression = attr.ib()
type = attr.ib('float32')
description = attr.ib(default=None)
unit = attr.ib(default=None)
no_data_value = attr.ib(default="NaN")
```

