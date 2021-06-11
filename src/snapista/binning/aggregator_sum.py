import attr
import lxml.etree as etree


@attr.s
class AggregatorSum(object):

    type = attr.ib(init=False, default="SUM")
    varName = attr.ib()
    targetName = attr.ib()

    def __str__(self):

        self.type = "SUM"

        return self.__repr__()

    def __repr__(self):

        self.type = "SUM"

        return "AggregatorSum({})".format(
            ", ".join(
                ["{}='{}'".format(key, value) for key, value in self.to_dict().items()]
            )
        )

    def to_dict(self):

        self.type = "SUM"

        return attr.asdict(self)

    def to_xml(self):

        self.type = "SUM"

        root = etree.Element("aggregator")

        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, key)

            elem.text = str(value)

        return root
