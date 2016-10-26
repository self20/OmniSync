# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_wizard(object):
    def setupUi(self, add_wizard):
        add_wizard.setObjectName("add_wizard")
        add_wizard.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_wizard.sizePolicy().hasHeightForWidth())
        add_wizard.setSizePolicy(sizePolicy)
        add_wizard.setMinimumSize(QtCore.QSize(640, 480))
        add_wizard.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("omnisync.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_wizard.setWindowIcon(icon)
        add_wizard.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        add_wizard.setModal(True)
        add_wizard.setOptions(QtWidgets.QWizard.NoBackButtonOnLastPage|QtWidgets.QWizard.NoBackButtonOnStartPage|QtWidgets.QWizard.NoCancelButtonOnLastPage)
        self.selection_page = QtWidgets.QWizardPage()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selection_page.sizePolicy().hasHeightForWidth())
        self.selection_page.setSizePolicy(sizePolicy)
        self.selection_page.setTitle("")
        self.selection_page.setObjectName("selection_page")
        self.option_list = QtWidgets.QListView(self.selection_page)
        self.option_list.setGeometry(QtCore.QRect(10, 1, 581, 341))
        self.option_list.setViewMode(QtWidgets.QListView.ListMode)
        self.option_list.setUniformItemSizes(True)
        self.option_list.setSelectionRectVisible(False)
        self.option_list.setObjectName("option_list")
        add_wizard.addPage(self.selection_page)
        self.auth_page = QtWidgets.QWizardPage()
        self.auth_page.setTitle("")
        self.auth_page.setObjectName("auth_page")
        self.webView = QtWebKitWidgets.QWebView(self.auth_page)
        self.webView.setGeometry(QtCore.QRect(10, 10, 581, 331))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        add_wizard.addPage(self.auth_page)
        self.last_page = QtWidgets.QWizardPage()
        self.last_page.setSubTitle("")
        self.last_page.setObjectName("last_page")
        add_wizard.addPage(self.last_page)

        self.retranslateUi(add_wizard)
        QtCore.QMetaObject.connectSlotsByName(add_wizard)

    def retranslateUi(self, add_wizard):
        _translate = QtCore.QCoreApplication.translate
        add_wizard.setWindowTitle(_translate("add_wizard", "OmniSync - Add account"))
        self.selection_page.setSubTitle(_translate("add_wizard", "Which type of account would you like to add?"))
        self.auth_page.setSubTitle(_translate("add_wizard", "Authentication"))
        self.last_page.setTitle(_translate("add_wizard", "Success!<br/><br/>The selected account was added. "))

from PyQt5 import QtWebKitWidgets
