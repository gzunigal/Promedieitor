from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot
import sys
from ui_ayuda import Ui_Ayuda

# Se hereda de la clase QtGui.QDialog
class PopVar(QtGui.QDialog):
	# Se define el constructor de la clase __init__
	def __init__(self):
		# Se llama al constructor de la clase padre
		QtGui.QDialog.__init__(self)
		# Se crea la instancia de Ui_Dialog
		self.ventana = Ui_Ayuda()
		self.ventana.setupUi(self)
		
		self.ventana.buttonBox.connect(self.ventana.buttonBox, SIGNAL("accepted()"),self, SLOT("accept()"))
