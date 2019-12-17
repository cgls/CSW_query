from owslib.fes import PropertyIsLike

from owslib.csw import CatalogueServiceWeb

csw = CatalogueServiceWeb('http://geoland2.ipma.pt/csw')

query_like = PropertyIsLike('dc:title', 'Global Land Surface Temperature %')

csw.getrecords2(constraints=[query_like])

csw.results['matches']
