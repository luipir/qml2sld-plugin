# -*- coding: utf-8 -*-
'''
(c) 2016 Boundless, http://boundlessgeo.com
This code is licensed under the GPL 2.0 license.
'''

from PyQt4 import QtGui, QtCore

class Qml2SldPlugin:

	def __init__(self, iface):
		self.iface = iface
		self.toolbar = None

	def unload(self):
		self.iface.removePluginMenu(u"Qml2Sld", self.action)
		del self.action
		if self.toolbar:
			self.toolbar.setVisible(False)
			del self.toolbar
 
	def initGui(self):
		self.action = QtGui.QAction("Start Qml2Sld", self.iface.mainWindow())
		self.iface.addPluginToMenu(u"Qml2Sld", self.action)
