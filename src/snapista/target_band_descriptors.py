import lxml.etree as etree


class TargetBandDescriptors(object):
    
    def __init__(self, target_bands):
        
        self.target_bands = target_bands
        
    def to_xml(self):
        
        root = etree.Element("targetBands")
        
        for target_band in self.target_bands:
            
            root.append(target_band.to_xml())
        
        return root
        