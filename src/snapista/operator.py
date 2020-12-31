from types import SimpleNamespace
from snappy import GPF, jpy
from .operatorparams import OperatorParams


class Operator(SimpleNamespace):
    def __init__(self, operator, **kwargs):

        self.operator = operator
        self._params = {**OperatorParams(self.operator).params, **kwargs}

        return super().__init__(**self._params)

    def __str__(self):

        return "{}:\n\t{}".format(
            self.operator, "\n\t".join(["{}='{}'".format(key, value) for key, value in self.to_dict().items()])
        )

    def __repr__(self):

        return "Operator('{}', {})".format(
            self.operator, ", ".join(["{}='{}'".format(key, value) for key, value in self.to_dict().items()])
        )

    def to_dict(self):

        return dict([(name, getattr(self, name)) for name in list(self._params.keys())])

    def describe(self):
        """This function prints the human readable information about a SNAP operator

        Args:
            operator: SNAP operator

        Returns
            The human readable information about the provided SNAP operator.

        Raises:
            None.
        """
        op_spi = GPF.getDefaultInstance().getOperatorSpiRegistry().getOperatorSpi(self.operator)

        print("Operator name: {}\n".format(op_spi.getOperatorDescriptor().getAlias()))
        print("Description: {}".format(op_spi.getOperatorDescriptor().getDescription()))
        print("Authors: {}\n".format(op_spi.getOperatorDescriptor().getAuthors()))
        print("{}".format(op_spi.getOperatorDescriptor().getName()))
        print("Version: {}\n".format(op_spi.getOperatorDescriptor().getVersion()))
        print("Parameters:\n")
        param_Desc = op_spi.getOperatorDescriptor().getParameterDescriptors()

        for param in param_Desc:
            print(
                "\t{}: {}\n\t\tDefault Value: {}\n".format(
                    param.getName(), param.getDescription(), param.getDefaultValue()
                )
            )

            if self.operator == "Write" and param.getName() == "formatName":

                print("\t\tPossible values: {}\n".format(self._get_formats("Write")))

            elif self.operator == "Read" and param.getName() == "formatName":

                print("\t\tPossible values: {}\n".format(self._get_formats("Read")))

            else:

                print("\t\tPossible values: {}\n".format(list(param.getValueSet())))

    @staticmethod
    def _get_formats(method):
        """This function provides a human readable list of SNAP Read or Write operator formats.

        Args:
            None.

        Returns
            Human readable list of SNAP Write operator formats.

        Raises:
            None.
        """
        ProductIOPlugInManager = jpy.get_type("org.esa.snap.core.dataio.ProductIOPlugInManager")

        if method == "Read":
            plugins = ProductIOPlugInManager.getInstance().getAllReaderPlugIns()
        elif method == "Write":
            plugins = ProductIOPlugInManager.getInstance().getAllWriterPlugIns()
        else:
            raise ValueError

        formats = []

        while plugins.hasNext():
            plugin = plugins.next()
            formats.append(plugin.getFormatNames()[0])

        return formats
