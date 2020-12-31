from snappy import GPF


class OperatorParams:
    def __init__(self, operator):

        self.operator = operator

        self.params = self.get_operator_default_parameters()

    def _get_snap_parameters(self):
        """This function returns the SNAP operator ParameterDescriptors (snappy method op_spi.getOperatorDescriptor().getParameterDescriptors())

        Args:
            operator: SNAP operator

        Returns
            The snappy object returned by op_spi.getOperatorDescriptor().getParameterDescriptors().

        Raises:
            None.
        """
        op_spi = GPF.getDefaultInstance().getOperatorSpiRegistry().getOperatorSpi(self.operator)

        op_params = op_spi.getOperatorDescriptor().getParameterDescriptors()

        return op_params

    def get_operator_default_parameters(self):
        """This function returns a Python dictionary with the SNAP operator parameters and their default values, if available.

        Args:
            operator: SNAP operator

        Returns
            A Python dictionary with the SNAP operator parameters and their default values.

        Raises:
            None.
        """
        parameters = dict()

        for param in self._get_snap_parameters():

            parameters[param.getName()] = param.getDefaultValue()

        return parameters
