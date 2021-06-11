import lxml.etree as etree
from .binning_variable import BinningVariable


class BinningVariables(object):
    def __init__(self, output_bands):

        if not isinstance(output_bands, list):

            raise ValueError("Provide a list with BinningVariable")

        self.output_bands = output_bands

        for band in self.output_bands:

            if not isinstance(band, BinningVariable):

                raise ValueError("Provide a list with BinningVariable")

    def to_xml(self):

        root = etree.Element("variables")

        for band in self.output_bands:

            if isinstance(band, BinningVariable):

                root.append(band.to_xml())

            else:

                raise ValueError("Provide a BinningVariable object")

        return root
