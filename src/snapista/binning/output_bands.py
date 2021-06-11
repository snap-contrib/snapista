import lxml.etree as etree
from .binning_band import BinningBand


class BinningOutputBands(object):
    def __init__(self, output_bands):

        if not isinstance(output_bands, list):

            raise ValueError("Provide a list with BinningBand")

        self.output_bands = output_bands

        for band in self.output_bands:

            if not isinstance(band, BinningBand):

                raise ValueError("Provide a list with BinningBand")

    def to_xml(self):

        root = etree.Element("outputBands")

        for band in self.output_bands:

            if isinstance(band, BinningBand):

                root.append(band.to_xml())

            else:

                raise ValueError("Provide a BinningBand object")

        return root
