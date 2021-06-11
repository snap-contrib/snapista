import attr
import lxml.etree as etree


@attr.s
class AggregatorMinMax(object):

    type = attr.ib(init=False, default="MIN_MAX")
    varName = attr.ib()
    targetName = attr.ib()

    def __str__(self):

        self.type = "MIN_MAX"

        return self.__repr__()

    def __repr__(self):

        self.type = "MIN_MAX"

        return "AggregatorMinMax({})".format(
            ", ".join(
                ["{}='{}'".format(key, value) for key, value in self.to_dict().items()]
            )
        )

    def to_dict(self):

        self.type = "MIN_MAX"

        return attr.asdict(self)

    def to_xml(self):

        self.type = "MIN_MAX"

        root = etree.Element("aggregator")

        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, key)

            elem.text = str(value)

        return root
