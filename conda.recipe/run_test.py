from py_snap_helpers import Graph
from py_snap_helpers import Operator
from py_snap_helpers import OperatorParams


calibration = Operator('Calibration')

calibration.createBetaBand = 'true'

g = Graph()

g.add_node(Operator('Read'), 'read_1')

calibration = Operator('Calibration')

calibration.createBetaBand = 'false'

g.add_node(calibration, 'calibration', 'read_1')
