# -*- coding: utf-8 -*-
'''
(c) 2016 Boundless, http://boundlessgeo.com
This code is licensed under the GPL 2.0 license.
'''
import os
from visitor import VisitorDom, Visitor

class Qml2Sld10VisitorDom(VisitorDom):
    ''' Visitor class with all method to manage/visit XML structures
    '''
    def visit_Document(self, node):
        self.genericVisit(node)
    
    def visit_DocumentType(self, node):
        self.genericVisit(node)
    
    def visit_Element(self, node):
        self.genericVisit(node)
 
    def visit_Text(self, node):
        self.genericVisit(node)
 
class Qml2Sld10VisitorQml(Visitor):
    ''' this visitor class have all method to manage QMLs present in testdata/rt_mapserver_exporetr
    '''
    def visit_document(self, node):
        self.genericVisit(node)
    
    def visit_qgis(self, node):
        self.genericVisit(node)
    
    def visit_text(self, node):
        self.genericVisit(node)
 
    def visit_edittypes(self, node):
        self.genericVisit(node)
 
    def visit_edittype(self, node):
        self.genericVisit(node)
 
    def visit_widgetv2config(self, node):
        self.genericVisit(node)
 
    def visit_renderer_v2(self, node):
        self.genericVisit(node)
  
    def visit_categories(self, node):
        self.genericVisit(node)
  
    def visit_category(self, node):
        self.genericVisit(node)
  
    def visit_symbols(self, node):
        self.genericVisit(node)
  
    def visit_symbol(self, node):
        self.genericVisit(node)
  
    def visit_layer(self, node):
        self.genericVisit(node)
  
    def visit_prop(self, node):
        self.genericVisit(node)
  
    def visit_source_symbol(self, node):
        self.genericVisit(node)
  
    def visit_rotation(self, node):
        self.genericVisit(node)
  
    def visit_sizescale(self, node):
        self.genericVisit(node)
  
    def visit_labeling(self, node):
        self.genericVisit(node)
  
    def visit_customproperties(self, node):
        self.genericVisit(node)
  
    def visit_property(self, node):
        self.genericVisit(node)
  
    def visit_blendMode(self, node):
        self.genericVisit(node)
  
    def visit_featureBlendMode(self, node):
        self.genericVisit(node)
  
    def visit_layerTransparency(self, node):
        self.genericVisit(node)
  
    def visit_displayfield(self, node):
        self.genericVisit(node)
  
    def visit_label(self, node):
        self.genericVisit(node)
  
    def visit_labelattributes(self, node):
        self.genericVisit(node)
  
    def visit_family(self, node):
        self.genericVisit(node)
  
    def visit_size(self, node):
        self.genericVisit(node)
  
    def visit_bold(self, node):
        self.genericVisit(node)
  
    def visit_italic(self, node):
        self.genericVisit(node)
  
    def visit_underline(self, node):
        self.genericVisit(node)
  
    def visit_strikeout(self, node):
        self.genericVisit(node)
  
    def visit_color(self, node):
        self.genericVisit(node)
  
    def visit_x(self, node):
        self.genericVisit(node)
  
    def visit_y(self, node):
        self.genericVisit(node)
  
    def visit_offset(self, node):
        self.genericVisit(node)
  
    def visit_angle(self, node):
        self.genericVisit(node)
  
    def visit_alignment(self, node):
        self.genericVisit(node)
  
    def visit_buffercolor(self, node):
        self.genericVisit(node)
  
    def visit_buffersize(self, node):
        self.genericVisit(node)
  
    def visit_bufferenabled(self, node):
        self.genericVisit(node)
   
    def visit_multilineenabled(self, node):
        self.genericVisit(node)
   
    def visit_selectedonly(self, node):
        self.genericVisit(node)
   
    def visit_SingleCategoryDiagramRenderer(self, node):
        self.genericVisit(node)
   
    def visit_DiagramCategory(self, node):
        self.genericVisit(node)
   
    def visit_fontProperties(self, node):
        self.genericVisit(node)
   
    def visit_attribute(self, node):
        self.genericVisit(node)
   
    def visit_DiagramLayerSettings(self, node):
        self.genericVisit(node)
   
    def visit_annotationform(self, node):
        self.genericVisit(node)
   
    def visit_excludeAttributesWMS(self, node):
        self.genericVisit(node)
   
    def visit_excludeAttributesWFS(self, node):
        self.genericVisit(node)
   
    def visit_attributeactions(self, node):
        self.genericVisit(node)
   
    def visit_editform(self, node):
        self.genericVisit(node)
   
    def visit_editforminit(self, node):
        self.genericVisit(node)
   
    def visit_editforminitcodesource(self, node):
        self.genericVisit(node)
   
    def visit_editforminitfilepath(self, node):
        self.genericVisit(node)
   
    def visit_editforminitcode(self, node):
        self.genericVisit(node)
   
    def visit_cdata_section(self, node):
        self.genericVisit(node)
   
    def visit_featformsuppress(self, node):
        self.genericVisit(node)
   
    def visit_editorlayout(self, node):
        self.genericVisit(node)
   
    def visit_widgets(self, node):
        self.genericVisit(node)
   
    def visit_conditionalstyles(self, node):
        self.genericVisit(node)
   
    def visit_rowstyles(self, node):
        self.genericVisit(node)
   
    def visit_fieldstyles(self, node):
        self.genericVisit(node)
   
    def visit_layerGeometryType(self, node):
        self.genericVisit(node)
   
    def visit_ranges(self, node):
        self.genericVisit(node)
   
    def visit_range(self, node):
        self.genericVisit(node)
   
    def visit_colorramp(self, node):
        self.genericVisit(node)
   
    def visit_invertedcolorramp(self, node):
        self.genericVisit(node)
   
    def visit_mode(self, node):
        self.genericVisit(node)
   
    def visit_labelformat(self, node):
        self.genericVisit(node)
   
if __name__ == '__main__':
    import xml.dom.minidom as md
    
    # set here the qml to browse 
    testqml = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tests', 'testdata', 'rt_mapserver_exporter', '01-single-point.qml')
    
    # Open XML document using minidom parser
    DOMTree = md.parse(testqml)
    v = Qml2Sld10VisitorQml()
    v.visit(DOMTree)
#     for tag in v.tags.keys():
#         print tag, v.tags[tag]
