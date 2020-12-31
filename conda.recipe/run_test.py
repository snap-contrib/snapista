from snapista import Graph
from snapista import Operator

calibration = Operator('Calibration')

calibration.createBetaBand = 'true'

g = Graph()

g.add_node(Operator('Read'), 'read_1')

calibration = Operator('Calibration')

calibration.createBetaBand = 'false'

g.add_node(calibration, 'calibration', 'read_1')
