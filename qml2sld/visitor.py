# -*- coding: utf-8 -*-
'''
(c) 2016 Boundless, http://boundlessgeo.com
This code is licensed under the GPL 2.0 license.
'''
class Visitor:
    def __init__(self):
        ''' this init is only useful to count tags and print the visited nodes
        in hierarchic way. It's not useful at all into the visitor pattern'''
        self.level = 0
        self.tags = {}
    
    def visit(self, node):
        name = self.__adaptNodeName(node.nodeName)
        methodName = 'visit_' + name
        visitMethod = getattr(self, methodName, None)
        if visitMethod is None:
            visitMethod = self.visit_generic
        return visitMethod(node)

    def visit_generic(self, node):
        ''' method called if nodeName is not recognised. Means no visit_<nodName> method
        is present in the visitor implementation class
        '''
        name = self.__adaptNodeName(node.nodeName)
        raise RuntimeError('No {} method'.format('visit_' + name))

    def genericVisit(self, node):
        ''' method to print the tag and its level. It's not useful at all in the visitor pattern '''
        # count tags
        try:
            self.tags[node.nodeName] += 1
        except:
            self.tags[node.nodeName] = 1
        # strip textual leaf tags if empty
        if node.nodeName == '#text':
            if node.nodeValue.strip() == '':
                return
        # print tag with 4space indentation
        print node.nodeName.rjust(len(node.nodeName) + (self.level-1)*4)
        # go to the next inner level
        self.level += 1
        for child in node.childNodes:
            self.visit(child)
        # return back
        self.level -= 1

    def __adaptNodeName(self, nodeName):
        ''' strip invalid chars to allow creating a valid function name '''
        name = nodeName
        name = name.replace('#', '')
        name = name.replace('-', '_')
        name = name.replace(':', '_')
        return name

# visitor to parse DOM class types 
class VisitorDom:
    def __init__(self):
        ''' this init is only useful print the visited nodes
        in hierarchic way. It's not useful at all into the visitor pattern'''
        self.level = 0
    
    def visit(self, node):
        ''' visitor pattern method to associate to the nodeName it's relative
        visitor method called visit_<instanceClassName>. 
        '''
        methodName = 'visit_' + node.__class__.__name__
        visitMethod = getattr(self, methodName, None)
        if visitMethod is None:
            visitMethod = self.visit_generic
        return visitMethod(node)

    def visit_generic(self, node):
        ''' method called if className is not recognised. Means no visit_<className> method
        is present in the visitor implementation class
        '''
        raise RuntimeError('No {} method'.format('visit_' + node.__class__.__name__))

    def genericVisit(self, node):
        ''' method to print the className and its level. It's not useful at all in the visitor pattern '''
        name = node.nodeName
        print name.rjust(len(name)+self.level)
        self.level += 1
        for child in node.childNodes:
            self.visit(child)
        self.level -= 1
