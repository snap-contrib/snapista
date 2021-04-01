import lxml.etree as etree
import requests 
from urllib.parse import urlparse
from .graph import Graph

def read_file(uri):

    parsed = urlparse(uri)

    if parsed.scheme[:4] == 'http':
    
        r = requests.get(uri)
        root = etree.fromstring(r.content).xpath('/graph')[0]

    else:

        root = etree.parse(uri)

    return Graph(root=root) 