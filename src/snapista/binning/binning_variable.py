import attr
import lxml.etree as etree


@attr.s
class BinningVariable(object):

    name = attr.ib()
    expression = attr.ib()
    valid_expression = attr.ib()

    def __str__(self):

        return self.__repr__()

    def __repr__(self):

        return "BinningVariable({})".format(
            ", ".join(
                ["{}='{}'".format(key, value) for key, value in self.to_dict().items()]
            )
        )

    def to_dict(self):

        return attr.asdict(self)

    def format_key(self, key):

        if key in ["expression"]:

            return "expr"

        elif key in ["valid_expression"]:

            return "validExpr"

        else:

            return key

    def to_xml(self):

        root = etree.Element("variable")

        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, self.format_key(key))

            elem.text = value

        return root
