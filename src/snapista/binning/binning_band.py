import attr
import lxml.etree as etree


@attr.s
class BinningBand(object):

    index = attr.ib()
    name = attr.ib()
    minValue = attr.ib()
    maxValue = attr.ib()

    def __str__(self):

        return self.__repr__()

    def __repr__(self):

        return "BinningBand({})".format(
            ", ".join(
                ["{}='{}'".format(key, value) for key, value in self.to_dict().items()]
            )
        )

    def to_dict(self):

        return attr.asdict(self)

    def to_xml(self):

        root = etree.Element("band")

        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, key)

            elem.text = str(value)

        return root
