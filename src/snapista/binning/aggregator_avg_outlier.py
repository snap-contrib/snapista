import attr
import lxml.etree as etree


@attr.s
class AggregatorAvgOutlier(object):

    type = attr.ib(init=False, default="AVG_OUTLIER")
    varName = attr.ib()
    targetName = attr.ib()

    def __str__(self):

        self.type = "AVG_OUTLIER"

        return self.__repr__()

    def __repr__(self):

        self.type = "AVG_OUTLIER"

        return "AggregatorAvgOutlier({})".format(
            ", ".join(
                ["{}='{}'".format(key, value) for key, value in self.to_dict().items()]
            )
        )

    def to_dict(self):

        self.type = "AVG_OUTLIER"

        return attr.asdict(self)

    def to_xml(self):

        self.type = "AVG_OUTLIER"

        root = etree.Element("aggregator")

        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, key)

            elem.text = str(value)

        return root
