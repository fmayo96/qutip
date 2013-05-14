# This file is part of QuTiP.
#
#    QuTiP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    QuTiP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QuTiP.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2011 and later, Paul D. Nation & Robert J. Johansson
#
###########################################################################
import os,sys
import qutip
if os.environ['QUTIP_GUI'] == "PYSIDE":
    from PySide import QtGui, QtCore

elif os.environ['QUTIP_GUI'] == "PYQT4":
    from PyQt4 import QtGui, QtCore

import numpy
import scipy
import matplotlib
import Cython
from qutip import version2int, __version__ as qutip_version

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

CD_BASE = os.path.dirname(__file__)

class Aboutbox(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("About QuTiP"))
        Form.resize(365, 505)

        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName(_fromUtf8("label"))

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(240, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(CD_BASE + "/logo.png")))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
 
        self.qutip_label = QtGui.QLabel(self.tab)
        self.qutip_label.setGeometry(QtCore.QRect(10, 10, 121, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.qutip_label.setFont(font)
        self.qutip_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qutip_label.setObjectName(_fromUtf8("qutip_label"))

        self.numpy_label = QtGui.QLabel(self.tab)
        self.numpy_label.setGeometry(QtCore.QRect(10, 40, 121, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.numpy_label.setFont(font)
        self.numpy_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numpy_label.setObjectName(_fromUtf8("numpy_label"))
        self.scipy_label = QtGui.QLabel(self.tab)
        self.scipy_label.setGeometry(QtCore.QRect(10, 60, 121, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.scipy_label.setFont(font)
        self.scipy_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scipy_label.setObjectName(_fromUtf8("scipy_label"))
        self.cython_label = QtGui.QLabel(self.tab)
        self.cython_label.setGeometry(QtCore.QRect(10, 80, 121, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.cython_label.setFont(font)
        self.cython_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cython_label.setObjectName(_fromUtf8("cython_label"))
        self.mpl_label = QtGui.QLabel(self.tab)
        self.mpl_label.setGeometry(QtCore.QRect(10, 100, 141, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.mpl_label.setFont(font)
        self.mpl_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mpl_label.setObjectName(_fromUtf8("mpl_label"))
        self.pyside_label = QtGui.QLabel(self.tab)
        self.pyside_label.setGeometry(QtCore.QRect(10, 130, 141, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.pyside_label.setFont(font)
        self.pyside_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pyside_label.setObjectName(_fromUtf8("pyside_label"))

        self.pyqt4_label = QtGui.QLabel(self.tab)
        self.pyqt4_label.setGeometry(QtCore.QRect(10, 150, 141, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pyqt4_label.setFont(font)
        self.pyqt4_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pyqt4_label.setObjectName(_fromUtf8("pyqt4_label"))

        self.pyobjc_label = QtGui.QLabel(self.tab)
        self.pyobjc_label.setGeometry(QtCore.QRect(10, 170, 141, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        if sys.platform == 'darwin':
            self.pyobjc_label.setFont(font)
            self.pyobjc_label.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.pyobjc_label.setObjectName(_fromUtf8("pyobjc_label"))

        self.qutip_version = QtGui.QLabel(self.tab)
        self.qutip_version.setGeometry(QtCore.QRect(160, 10, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.qutip_version.setFont(font)
        self.qutip_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qutip_version.setObjectName(_fromUtf8("qutip_version"))

        self.numpy_version = QtGui.QLabel(self.tab)
        self.numpy_version.setGeometry(QtCore.QRect(160, 41, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.numpy_version.setFont(font)
        self.numpy_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numpy_version.setObjectName(_fromUtf8("numpy_version"))

        self.scipy_version = QtGui.QLabel(self.tab)
        self.scipy_version.setGeometry(QtCore.QRect(160, 60, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.scipy_version.setFont(font)
        self.scipy_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scipy_version.setObjectName(_fromUtf8("scipy_version"))

        self.cython_version = QtGui.QLabel(self.tab)
        self.cython_version.setGeometry(QtCore.QRect(160, 80, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.cython_version.setFont(font)
        self.cython_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cython_version.setObjectName(_fromUtf8("cython_version"))

        self.mpl_version = QtGui.QLabel(self.tab)
        self.mpl_version.setGeometry(QtCore.QRect(160, 100, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.mpl_version.setFont(font)
        self.mpl_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mpl_version.setObjectName(_fromUtf8("mpl_version"))

        self.pyside_version = QtGui.QLabel(self.tab)
        self.pyside_version.setGeometry(QtCore.QRect(160, 130, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pyside_version.setFont(font)
        self.pyside_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pyside_version.setObjectName(_fromUtf8("pyside_version"))

        self.pyqt4_version = QtGui.QLabel(self.tab)
        self.pyqt4_version.setGeometry(QtCore.QRect(160, 150, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pyqt4_version.setFont(font)
        self.pyqt4_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pyqt4_version.setObjectName(_fromUtf8("pyqt4_version"))

        self.pyobjc_version = QtGui.QLabel(self.tab)
        self.pyobjc_version.setGeometry(QtCore.QRect(160, 170, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        if sys.platform == 'darwin':
            self.pyobjc_version.setFont(font)
            self.pyobjc_version.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.pyobjc_version.setObjectName(_fromUtf8("pyobjc_version"))

        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))

        self.devs = QtGui.QLabel(self.tab_2)
        self.devs.setGeometry(QtCore.QRect(10, 10, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.devs.setFont(font)
        self.devs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.devs.setObjectName(_fromUtf8("devs"))

        self.rob = QtGui.QLabel(self.tab_2)
        self.rob.setGeometry(QtCore.QRect(10, 40, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rob.setFont(font)
        self.rob.setOpenExternalLinks(True)
        self.rob.setObjectName(_fromUtf8("rob"))
        self.and_symbol = QtGui.QLabel(self.tab_2)
        self.and_symbol.setGeometry(QtCore.QRect(150, 40, 16, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.and_symbol.setFont(font)
        self.and_symbol.setObjectName(_fromUtf8("and_symbol"))

        self.paul = QtGui.QLabel(self.tab_2)
        self.paul.setGeometry(QtCore.QRect(170, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.paul.setFont(font)
        self.paul.setOpenExternalLinks(True)
        self.paul.setObjectName(_fromUtf8("paul"))

        self.conrib = QtGui.QLabel(self.tab_2)
        self.conrib.setGeometry(QtCore.QRect(10, 70, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.conrib.setFont(font)
        self.conrib.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.conrib.setObjectName(_fromUtf8("conrib"))

        self.contributors = QtGui.QLabel(self.tab_2)
        self.contributors.setGeometry(QtCore.QRect(10, 100, 301, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.contributors.setFont(font)
        self.contributors.setObjectName(_fromUtf8("contributors"))

        self.others = QtGui.QLabel(self.tab_2)
        self.others.setGeometry(QtCore.QRect(10, 150, 321, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.others.setFont(font)
        self.others.setObjectName(_fromUtf8("others"))
        self.others_1 = QtGui.QLabel(self.tab_2)
        self.others_1.setGeometry(QtCore.QRect(10, 170, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.others_1.setFont(font)
        self.others_1.setObjectName(_fromUtf8("others_1"))

        self.docs_link = QtGui.QLabel(self.tab_2)
        self.docs_link.setGeometry(QtCore.QRect(150, 170, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.docs_link.setFont(font)
        self.docs_link.setOpenExternalLinks(True)
        self.docs_link.setObjectName(_fromUtf8("docs_link"))

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 5, 0, 1, 1)
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        from qutip import _version
        if _version.release:
            version = _version.short_version
        else:
            version = 'HEAD'
        try:
            import PySide
            pyside_ver = PySide.__version__
        except:
            pyside_ver = 'None'
        try:
            import PyQt4.QtCore as qt4Core
            pyqt4_ver = qt4Core.PYQT_VERSION_STR
        except:
            pyqt4_ver = 'None'

        if sys.platform == 'darwin':
            try:
                import Foundation
                pyobjc = 'Yes'
            except:
                pyobjc = 'No'
        Form.setWindowTitle(_translate("Form", "About QuTiP", None))
        Form.setWindowIcon(QtGui.QIcon(CD_BASE + "/logo.png"))
        self.label.setText(_translate("Form", "QuTiP: The Quantum Toolbox in Python", None))
        self.label_3.setText(_translate("Form", "Copyright 2011 and later, P. D. Nation & J. R. Johansson", None))
        self.qutip_label.setText(_translate("Form", "QuTiP Version:", None))
        self.numpy_label.setText(_translate("Form", "NumPy Version:", None))
        self.scipy_label.setText(_translate("Form", "SciPy Version:", None))
        self.cython_label.setText(_translate("Form", "Cython Version:", None))
        self.mpl_label.setText(_translate("Form", "Matplotlib Version:", None))
        self.pyside_label.setText(_translate("Form", "PySide Version:", None))
        self.pyqt4_label.setText(_translate("Form", "PyQt4 Version:", None))
        if sys.platform == 'darwin':
            self.pyobjc_label.setText(_translate("Form", "PyObjC Version:", None))
        self.qutip_version.setText(_translate("Form", qutip_version, None))
        self.numpy_version.setText(_translate("Form", str(numpy.__version__), None))
        self.scipy_version.setText(_translate("Form", str(scipy.__version__), None))
        self.cython_version.setText(_translate("Form", str(Cython.__version__), None))
        self.mpl_version.setText(_translate("Form", str(matplotlib.__version__), None))
        self.pyside_version.setText(_translate("Form", pyside_ver, None))
        self.pyqt4_version.setText(_translate("Form", pyqt4_ver, None))
        if sys.platform == 'darwin':
            self.pyobjc_version.setText(_translate("Form", str(pyobjc), None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Version Info", None))
        self.devs.setText(_translate("Form", "Lead Developers:", None))
        self.rob.setText(_translate("Form", "<html><head/><body><p><a href=\"http://dml.riken.jp/~rob\"><span style=\" text-decoration: underline; color:#0000ff;\">Robert Johansson</span></a></p></body></html>", None))
        self.and_symbol.setText(_translate("Form", "&", None))
        self.paul.setText(_translate("Form", "<html><head/><body><p><a href=\"http://nqdl.korea.ac.kr\"><span style=\" text-decoration: underline; color:#0000ff;\">Paul Nation</span></a></p></body></html>", None))
        self.conrib.setText(_translate("Form", "Contributors:", None))
        self.contributors.setText(_translate("Form", "Arne Grimsmo, Markus Baden", None))
        self.others.setText(_translate("Form", "For a list of bug hunters and other", None))
        self.others_1.setText(_translate("Form", "supporters, see the", None))
        self.docs_link.setText(_translate("Form", "<html><head/><body><p><a href=\"http://qutip.googlecode.com/svn/doc/2.2.0/html/index.html\"><span style=\" text-decoration: underline; color:#0000ff;\">QuTiP Documentation</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Developers", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Aboutbox()
    ui.setupUi(Form)
    Form.activateWindow()
    Form.setFocus()
    Form.show()
    Form.raise_()
    app.exec_()

