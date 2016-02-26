# -*- coding: utf-8 -*-
'''
(c) 2016 Boundless, http://boundlessgeo.com
This code is licensed under the GPL 2.0 license.
'''
import os
from visitor import Visitor 

class Qml2Sld10VisitorQml(Visitor):
    ''' this visitor class have all method to manage SLDs present in testdata/rt_mapserver_exporetr
    '''
    def visit_document(self, node):
        self.genericVisit(node)
    
    def visit_StyledLayerDescriptor(self, node):
        self.genericVisit(node)
    
    def visit_NamedLayer(self, node):
        self.genericVisit(node)
 
    def visit_text(self, node):
        self.genericVisit(node)
 
    def visit_se_Name(self, node):
        self.genericVisit(node)
 
    def visit_UserStyle(self, node):
        self.genericVisit(node)
 
    def visit_se_FeatureTypeStyle(self, node):
        self.genericVisit(node)
  
    def visit_se_Rule(self, node):
        self.genericVisit(node)
  
    def visit_se_Description(self, node):
        self.genericVisit(node)
  
    def visit_se_Title(self, node):
        self.genericVisit(node)
  
    def visit_ogc_Filter(self, node):
        self.genericVisit(node)
  
    def visit_ogc_PropertyIsEqualTo(self, node):
        self.genericVisit(node)
  
    def visit_ogc_PropertyName(self, node):
        self.genericVisit(node)
  
    def visit_ogc_Literal(self, node):
        self.genericVisit(node)
  
    def visit_se_PolygonSymbolizer(self, node):
        self.genericVisit(node)
  
    def visit_se_Fill(self, node):
        self.genericVisit(node)
  
    def visit_se_GraphicFill(self, node):
        self.genericVisit(node)
  
    def visit_se_Graphic(self, node):
        self.genericVisit(node)
  
    def visit_se_Mark(self, node):
        self.genericVisit(node)
  
    def visit_se_WellKnownName(self, node):
        self.genericVisit(node)
  
    def visit_se_SvgParameter(self, node):
        self.genericVisit(node)
  
    def visit_se_Stroke(self, node):
        self.genericVisit(node)
  
    def visit_se_Size(self, node):
        self.genericVisit(node)
  
    def visit_se_Rotation(self, node):
        self.genericVisit(node)
  
    def visit_VendorOption(self, node):
        self.genericVisit(node)
  
    def visit_se_Displacement(self, node):
        self.genericVisit(node)
  
    def visit_se_DisplacementX(self, node):
        self.genericVisit(node)
  
    def visit_se_DisplacementY(self, node):
        self.genericVisit(node)

    def visit_se_LineSymbolizer(self, node):
        self.genericVisit(node)

    def visit_se_PointSymbolizer(self, node):
        self.genericVisit(node)

    def visit_se_ExternalGraphic(self, node):
        self.genericVisit(node)
  
    def visit_se_OnlineResource(self, node):
        self.genericVisit(node)
  
    def visit_se_Format(self, node):
        self.genericVisit(node)

    def visit_se_MarkIndex(self, node):
        self.genericVisit(node)

    def visit_ogc_And(self, node):
        self.genericVisit(node)
  
    def visit_ogc_PropertyIsGreaterThan(self, node):
        self.genericVisit(node)
  
    def visit_ogc_PropertyIsLessThanOrEqualTo(self, node):
        self.genericVisit(node)
   
if __name__ == '__main__':
    import xml.dom.minidom as md
     
    testqml = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tests', 'testdata', 'rt_mapserver_exporter', '14-label-positioning.sld')
     
    # Open XML document using minidom parser
    DOMTree = md.parse(testqml)
    
    v = Qml2Sld10VisitorQml()
    v.visit(DOMTree)
#     for tag in v.tags.keys():
#         print tag, v.tags[tag]