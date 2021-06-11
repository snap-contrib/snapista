import attr
import lxml.etree as etree


@attr.s
class AggregatorPercentile(object):

    type = attr.ib(init=False, default="PERCENTILE")
    varName = attr.ib()
    targetName = attr.ib()
    percentage = attr.ib(default=90)

    @percentage.validator
    def _check_type(self, attribute, value):

        if not (isinstance(value, int)):
            raise ValueError("percentage is an int")

        if int(value) < 0 or int(value > 100):
            raise ValueError("percentage value is in range [0.0, 100.0]")

    def __str__(self):

        self.type = "PERCENTILE"

        return self.__repr__()

    def __repr__(self):

        self.type = "PERCENTILE"

        return "AggregatorPercentile({})".format(
            ", ".join(
                ["{}='{}'".format(key, value) for key, value in self.to_dict().items()]
            )
        )

    def to_dict(self):

        self.type = "PERCENTILE"

        return attr.asdict(self)

    def to_xml(self):

        self.type = "PERCENTILE"

        root = etree.Element("aggregator")

        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, key)

            elem.text = str(value)

        return root
