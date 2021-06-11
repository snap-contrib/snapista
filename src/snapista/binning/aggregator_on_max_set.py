import attr
import lxml.etree as etree


@attr.s
class AggregatorOnMaxSet(object):

    type = attr.ib(init=False, default="ON_MAX_SET")
    targetName = attr.ib()
    onMaxVarName = attr.ib()
    setVarNames = attr.ib(default=None)

    def __str__(self):

        self.type = "ON_MAX_SET"

        return self.__repr__()

    def __repr__(self):

        self.type = "ON_MAX_SET"

        return "AggregatorOnMaxSet({})".format(
            ", ".join(
                ["{}='{}'".format(key, value) for key, value in self.to_dict().items()]
            )
        )

    def to_dict(self):

        self.type = "ON_MAX_SET"

        return attr.asdict(self)

    def to_xml(self):

        self.type = "ON_MAX_SET"

        root = etree.Element("aggregator")

        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, key)

            elem.text = str(value)

        return root
