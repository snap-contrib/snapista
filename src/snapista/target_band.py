import attr
import lxml.etree as etree
from xml.sax.saxutils import escape


@attr.s
class TargetBand(object):

    name = attr.ib()
    expression = attr.ib()
    type = attr.ib('float32')
    description = attr.ib(default=None)
    unit = attr.ib(default=None)
    no_data_value = attr.ib(default="NaN")


    def __str__(self):

        return self.__repr__()

    def __repr__(self):

        return "TargetBand({})".format(
            ", ".join(["{}='{}'".format(key, value) for key, value in self.to_dict().items()])
        )

    def to_dict(self):
       
        return attr.asdict(self)
    
    def to_xml(self):
        
        root = etree.Element("targetBand")
        
        for key, value in self.to_dict().items():

            elem = etree.SubElement(root, key)

            if key == 'expression':
                elem.text = escape(value)
            else:
                elem.text = value
            
        return root