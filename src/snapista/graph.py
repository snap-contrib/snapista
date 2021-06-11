import os
import subprocess
import tempfile
import lxml.etree as etree
from snappy import GPF

from snapista.binning.output_bands import BinningOutputBands
from .target_band_descriptors import TargetBandDescriptors
from .binning import Aggregators
from .binning import BinningVariables


class Graph:
    """SNAP Graph class

    This class provides the methods to create, view and run a SNAP Graph

    Attributes:
        None.
    """

    def __init__(self, wdir=".", root=None):

        if root is None:
            self.root = etree.Element("graph")

            version = etree.SubElement(self.root, "version")
            version.text = "1.0"

        else:
            self.root = root

        self.pid = None
        self.p = None
        self.wdir = wdir
        self.gpt_path = self.get_gpt_cmd()

        if not self.gpt_path:

            raise Exception("gpt not found")

    def __str__(self):

        return "gpt binary: {}\nworking dir: {}\n\n{}".format(
            self.gpt_path,
            self.wdir,
            etree.tostring(self.root, pretty_print=True).decode("utf-8"),
        ).replace("\\n", "\n")

    def __repr__(self):

        return "Graph(wdir='{}')".format(self.wdir)

    @staticmethod
    def get_gpt_cmd():

        gpt_cmd = None

        for p in os.environ["PATH"].split(":"):

            if os.path.exists(os.path.join(p, "gpt")):

                gpt_cmd = os.path.join(p, "gpt")

                break

        return gpt_cmd

    @staticmethod
    def list_operators():
        """This function provides a Python dictionary with all SNAP operators.

        Args:
            None.

        Returns
            Python dictionary with all SNAP operators.

        Raises:
            None.
        """
        GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()

        op_spi_it = (
            GPF.getDefaultInstance()
            .getOperatorSpiRegistry()
            .getOperatorSpis()
            .iterator()
        )

        snap_operators = []

        while op_spi_it.hasNext():

            op_spi = op_spi_it.next()

            snap_operators.append(op_spi.getOperatorAlias())

        return snap_operators

    @staticmethod
    def describe_operators():
        """This function provides a Python dictionary with all SNAP operators.

        Args:
            None.

        Returns
            Python dictionary with all SNAP operators.

        Raises:
            None.
        """

        desc_dict = {}

        GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()

        op_spi_it = (
            GPF.getDefaultInstance()
            .getOperatorSpiRegistry()
            .getOperatorSpis()
            .iterator()
        )

        while op_spi_it.hasNext():

            op_spi = op_spi_it.next()

            alias = op_spi.getOperatorDescriptor().getAlias()
            description = op_spi.getOperatorDescriptor().getDescription()

            desc_dict[alias] = description
            print("{} - {}".format(alias, description))

        return desc_dict

    def nice_view(self):

        try:
            from pygments import highlight
            from pygments.lexers import XmlLexer
            from pygments.formatters import HtmlFormatter
            import IPython
            from IPython.display import HTML

            def display_xml_nice(xml):
                formatter = HtmlFormatter()
                IPython.display.display(
                    HTML(
                        '<style type="text/css">{}</style>    {}'.format(
                            formatter.get_style_defs(".highlight"),
                            highlight(xml, XmlLexer(), formatter),
                        )
                    )
                )

            display_xml_nice(etree.tostring(self.root, pretty_print=True))

        except ModuleNotFoundError:

            print(etree.tostring(self.root, pretty_print=True).decode("utf-8")).replace(
                "\\n", "\n"
            )

    def view(self):
        """This method prints SNAP Graph

        Args:
            None.

        Returns
            None.

        Raises:
            None.
        """
        print(etree.tostring(self.root, pretty_print=True).decode("utf-8"))

    def add_node(self, operator, node_id, source=None):
        """This method adds or overwrites a node to the SNAP Graph

        Args:
            operator: SNAP operator
            node_id: node identifier
            source: string or list of sources (previous node identifiers in the SNAP Graph)

        Returns
            None.

        Raises:
            None.
        """
        xpath_expr = '/graph/node[@id="%s"]' % node_id

        if len(self.root.xpath(xpath_expr)) != 0:

            node_elem = self.root.xpath(xpath_expr)[0]
            operator_elem = self.root.xpath(xpath_expr + "/operator")[0]
            sources_elem = self.root.xpath(xpath_expr + "/sources")[0]
            parameters_elem = self.root.xpath(xpath_expr + "/parameters")

            for param in [
                name
                for name in dir(operator)
                if name[:2] != "__"
                and name[-2:] != "__"
                and name != "_params"
                and name != "operator"
                and type(getattr(operator, name)).__name__
                in [
                    "str",
                    "NoneType",
                    "TargetBandDescriptors",
                    "Aggregators",
                    "BinningOutputBands",
                    "BinningVariables",
                ]
            ]:

                if param in [
                    "targetBandDescriptors",
                    "aggregatorConfigs",
                    "variableConfigs",
                    "bandConfigurations",
                    "postProcessorConfig",
                    "productCustomizerConfig",
                ]:
                  
                    if (param in ["bandConfigurations", "variableConfigs", "postProcessorConfig", "productCustomizerConfig" ] and not getattr(operator, param)): continue

                    if (
                        isinstance(getattr(operator, param), TargetBandDescriptors)
                        or isinstance(getattr(operator, param), Aggregators)
                        or isinstance(getattr(operator, param), BinningOutputBands)
                        or isinstance(getattr(operator, param), BinningVariables)
                    ):
                        parameters_elem.append(getattr(operator, param).to_xml())

                    elif isinstance(getattr(operator, param), str):

                        parameters_elem.append(
                            etree.fromstring(getattr(operator, param))
                        )
                    else:

                        raise ValueError()

                else:
                    p_elem = self.root.xpath(xpath_expr + "/parameters/%s" % param)[0]

                    if getattr(operator, param) is not None:
                        if getattr(operator, param)[0] != "<":
                            p_elem.text = getattr(operator, param)
                        else:
                            p_elem.text.append(
                                etree.fromstring(getattr(operator, param))
                            )

        else:

            node_elem = etree.SubElement(self.root, "node")
            operator_elem = etree.SubElement(node_elem, "operator")
            sources_elem = etree.SubElement(node_elem, "sources")

            if isinstance(source, list):

                for index, s in enumerate(source):
                    if index == 0:
                        source_product_elem = etree.SubElement(
                            sources_elem, "sourceProduct"
                        )

                    else:
                        source_product_elem = etree.SubElement(
                            sources_elem, "sourceProduct.%s" % str(index)
                        )

                    source_product_elem.attrib["refid"] = s

            elif isinstance(source, dict):

                for key, value in source.iteritems():

                    source_product_elem = etree.SubElement(sources_elem, key)
                    source_product_elem.text = value

            elif source is not None:
                source_product_elem = etree.SubElement(sources_elem, "sourceProduct")
                source_product_elem.attrib["refid"] = source

            parameters_elem = etree.SubElement(node_elem, "parameters")
            parameters_elem.attrib["class"] = "com.bc.ceres.binding.dom.XppDomElement"

            for param in [
                name
                for name in dir(operator)
                if name[:2] != "__"
                and name[-2:] != "__"
                and name != "_params"
                and name != "operator"
                and type(getattr(operator, name)).__name__
                in [
                    "str",
                    "NoneType",
                    "TargetBandDescriptors",
                    "Aggregators",
                    "BinningOutputBands",
                    "BinningVariables",
                ]
            ]:

                if param in [
                    "targetBandDescriptors",
                    "aggregatorConfigs",
                    "variableConfigs",
                    "bandConfigurations",
                    "postProcessorConfig",
                    "productCustomizerConfig",
                ]:
                    print(param, getattr(operator, param))
                    if (param in ["bandConfigurations", "variableConfigs", "postProcessorConfig", "productCustomizerConfig" ] and not getattr(operator, param)): continue

                    if (
                        isinstance(getattr(operator, param), TargetBandDescriptors)
                        or isinstance(getattr(operator, param), Aggregators)
                        or isinstance(getattr(operator, param), BinningOutputBands)
                        or isinstance(getattr(operator, param), BinningVariables)
                    ):

                        parameters_elem.append(getattr(operator, param).to_xml())

                    elif isinstance(getattr(operator, param), str):

                        parameters_elem.append(
                            etree.fromstring(getattr(operator, param))
                        )
                    else:

                        raise ValueError()

                else:

                    parameter_elem = etree.SubElement(parameters_elem, param)

                    if getattr(operator, param) is not None:
                        if getattr(operator, param)[0] != "<":
                            parameter_elem.text = getattr(operator, param)
                        else:
                            parameter_elem.append(
                                etree.fromstring(getattr(operator, param))
                            )

        node_elem.attrib["id"] = node_id

        operator_elem.text = operator.operator

    def save_graph(self, filename):
        """This method saves the SNAP Graph

        Args:
            filename: XML filename with '.xml' extension

        Returns
            None.

        Raises:
            None.
        """
        with open(filename, "w") as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write(etree.tostring(self.root, pretty_print=True).decode())

    def run(self, gpt_options=["-x", "-c", "1024M"]):
        """This method runs the SNAP Graph using gpt

        Args:
            gpt_options: list of options to pass to gpt. Defaults to ['-x', '-c', '1024M']

        Returns
            res: gpt exit code
            err: gpt stderr

        Raises:
            None.
        """

        def _run_command(command, **kwargs):

            process = subprocess.Popen(args=command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  **kwargs)
            while True:
                output = process.stdout.readline()
                err = process.stderr.readline()
                if output.decode() == "" and process.poll() is not None:
                    break
                if output:
                    print(output.strip().decode())
                if err:
                    print(err.strip().decode())
            rc = process.poll()

            return rc

        os.environ["LD_LIBRARY_PATH"] = "."

        print("Processing the graph")

        fd, path = tempfile.mkstemp()

        rc = None

        try:

            self.save_graph(filename=path)

            options = [self.gpt_path, *gpt_options, path]

            rc = _run_command(options)

        finally:

            os.remove(path)

        if rc != 0:

            raise Exception("Graph execution failed (exit code {})".format(rc))

        return rc
