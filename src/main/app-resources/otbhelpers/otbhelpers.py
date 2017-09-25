import lxml.etree as et

def set_OTB_param(key, value, xmlfile):
  expr = '/OTB/application/parameter/key[text() = $key]/../value'
  
  tree = et.parse(xmlfile)
  root = tree.getroot()
  
  exp = root.xpath(expr, key = key )
  exp[0].text = value
  
  et.ElementTree(root).write(xmlfile , pretty_print=True)
  
  return;

def set_OTB_params(key, values, xmlfile):
  expr = '/OTB/application/parameter/key[text() = $key]/../values/value'

  tree = et.parse(xmlfile)
  root = tree.getroot()

  exp = root.xpath(expr, key = key )
  for i in range(len(values)):
    exp[i - 1].text = values[i]

  et.ElementTree(root).write(xmlfile , pretty_print=True)

  return;

def get_OTB_appname(xmlfile):
  
   appname = '/OTB/application/name'
   
   tree = et.parse(xmlfile)
   root = tree.getroot()
    
   return(root.xpath(appname)[0].text)
     



