
"""
/***************************************************************************
 LandSurfaceTemperatureDialog
                                 A QGIS plugin
 This tool extracts Land Surface Temperature from satellite imagery
                             -------------------
        begin                : 2021-9-15
        git sha              : $Format:%p$
        email                : s38l3320@student.rmit.edu.au
 ***************************************************************************/
"""

import os

from PyQt5 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'lst_tool_dialog_base.ui'))


class LandSurfaceTemperatureDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
   
        super(LandSurfaceTemperatureDialog, self).__init__(parent)
     
        self.setupUi(self)
