# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/omnisync.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.status_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_tab.sizePolicy().hasHeightForWidth())
        self.status_tab.setSizePolicy(sizePolicy)
        self.status_tab.setAccessibleName("")
        self.status_tab.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.status_tab.setObjectName("status_tab")
        self.status_progress = QtWidgets.QProgressBar(self.status_tab)
        self.status_progress.setGeometry(QtCore.QRect(20, 480, 751, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_progress.sizePolicy().hasHeightForWidth())
        self.status_progress.setSizePolicy(sizePolicy)
        self.status_progress.setProperty("value", 24)
        self.status_progress.setObjectName("status_progress")
        self.status_view = QtWidgets.QListView(self.status_tab)
        self.status_view.setGeometry(QtCore.QRect(11, 11, 751, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_view.sizePolicy().hasHeightForWidth())
        self.status_view.setSizePolicy(sizePolicy)
        self.status_view.setSizeIncrement(QtCore.QSize(0, 0))
        self.status_view.setBaseSize(QtCore.QSize(0, 0))
        self.status_view.setIconSize(QtCore.QSize(14, 16))
        self.status_view.setResizeMode(QtWidgets.QListView.Fixed)
        self.status_view.setObjectName("status_view")
        self.tabWidget.addTab(self.status_tab, "")
        self.accounts_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accounts_tab.sizePolicy().hasHeightForWidth())
        self.accounts_tab.setSizePolicy(sizePolicy)
        self.accounts_tab.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.accounts_tab.setObjectName("accounts_tab")
        self.account_list = QtWidgets.QListView(self.accounts_tab)
        self.account_list.setGeometry(QtCore.QRect(11, 11, 271, 451))
        self.account_list.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.account_list.setViewMode(QtWidgets.QListView.ListMode)
        self.account_list.setObjectName("account_list")
        self.formLayoutWidget = QtWidgets.QWidget(self.accounts_tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(300, 10, 474, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.account_folder_text = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_folder_text.sizePolicy().hasHeightForWidth())
        self.account_folder_text.setSizePolicy(sizePolicy)
        self.account_folder_text.setReadOnly(True)
        self.account_folder_text.setObjectName("account_folder_text")
        self.horizontalLayout_5.addWidget(self.account_folder_text)
        self.account_folder_change_button = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_folder_change_button.sizePolicy().hasHeightForWidth())
        self.account_folder_change_button.setSizePolicy(sizePolicy)
        self.account_folder_change_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.account_folder_change_button.setObjectName("account_folder_change_button")
        self.horizontalLayout_5.addWidget(self.account_folder_change_button)
        self.horizontalLayout_5.setStretch(0, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.selective_sync_check = QtWidgets.QCheckBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selective_sync_check.sizePolicy().hasHeightForWidth())
        self.selective_sync_check.setSizePolicy(sizePolicy)
        self.selective_sync_check.setObjectName("selective_sync_check")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.selective_sync_check)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.account_icon = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_icon.sizePolicy().hasHeightForWidth())
        self.account_icon.setSizePolicy(sizePolicy)
        self.account_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.account_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.account_icon.setText("")
        self.account_icon.setScaledContents(True)
        self.account_icon.setObjectName("account_icon")
        self.horizontalLayout_7.addWidget(self.account_icon)
        self.account_label = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_label.sizePolicy().hasHeightForWidth())
        self.account_label.setSizePolicy(sizePolicy)
        self.account_label.setMinimumSize(QtCore.QSize(300, 0))
        self.account_label.setMaximumSize(QtCore.QSize(300, 16777215))
        self.account_label.setText("")
        self.account_label.setObjectName("account_label")
        self.horizontalLayout_7.addWidget(self.account_label)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.selective_sync_box = QtWidgets.QGroupBox(self.accounts_tab)
        self.selective_sync_box.setEnabled(False)
        self.selective_sync_box.setGeometry(QtCore.QRect(310, 140, 441, 351))
        self.selective_sync_box.setCheckable(False)
        self.selective_sync_box.setObjectName("selective_sync_box")
        self.account_directory_tree = QtWidgets.QTreeView(self.selective_sync_box)
        self.account_directory_tree.setGeometry(QtCore.QRect(10, 60, 421, 281))
        self.account_directory_tree.setObjectName("account_directory_tree")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.selective_sync_box)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 421, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sync_new_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sync_new_check.sizePolicy().hasHeightForWidth())
        self.sync_new_check.setSizePolicy(sizePolicy)
        self.sync_new_check.setChecked(True)
        self.sync_new_check.setObjectName("sync_new_check")
        self.horizontalLayout.addWidget(self.sync_new_check)
        self.show_files_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_files_check.sizePolicy().hasHeightForWidth())
        self.show_files_check.setSizePolicy(sizePolicy)
        self.show_files_check.setChecked(True)
        self.show_files_check.setObjectName("show_files_check")
        self.horizontalLayout.addWidget(self.show_files_check)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.accounts_tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 470, 251, 34))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.account_add_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.account_add_button.setIcon(icon)
        self.account_add_button.setObjectName("account_add_button")
        self.horizontalLayout_6.addWidget(self.account_add_button)
        self.account_remove_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.account_remove_button.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.account_remove_button.setIcon(icon)
        self.account_remove_button.setObjectName("account_remove_button")
        self.horizontalLayout_6.addWidget(self.account_remove_button)
        self.tabWidget.addTab(self.accounts_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_tab.sizePolicy().hasHeightForWidth())
        self.settings_tab.setSizePolicy(sizePolicy)
        self.settings_tab.setObjectName("settings_tab")
        self.groupBox = QtWidgets.QGroupBox(self.settings_tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 751, 181))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(150, 30, 466, 151))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.formLayout_2.setContentsMargins(20, 20, 20, 20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.downloadSpeedLimitLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadSpeedLimitLabel.sizePolicy().hasHeightForWidth())
        self.downloadSpeedLimitLabel.setSizePolicy(sizePolicy)
        self.downloadSpeedLimitLabel.setObjectName("downloadSpeedLimitLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.downloadSpeedLimitLabel)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.download_limit = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.download_limit.setMaximum(999999999)
        self.download_limit.setObjectName("download_limit")
        self.horizontalLayout_9.addWidget(self.download_limit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.uploadSpeedLimitLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.uploadSpeedLimitLabel.setObjectName("uploadSpeedLimitLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uploadSpeedLimitLabel)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.upload_limit = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.upload_limit.setMaximum(999999999)
        self.upload_limit.setObjectName("upload_limit")
        self.horizontalLayout_10.addWidget(self.upload_limit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.maximumSimultaneousConnectionsLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.maximumSimultaneousConnectionsLabel.setObjectName("maximumSimultaneousConnectionsLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maximumSimultaneousConnectionsLabel)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.conn_limit = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.conn_limit.setMinimum(1)
        self.conn_limit.setObjectName("conn_limit")
        self.horizontalLayout_11.addWidget(self.conn_limit)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.tabWidget.addTab(self.settings_tab, "")
        self.about_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_tab.sizePolicy().hasHeightForWidth())
        self.about_tab.setSizePolicy(sizePolicy)
        self.about_tab.setObjectName("about_tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.about_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 751, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("../icons/omnisync.svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.setStretch(3, 1)
        self.tabWidget.addTab(self.about_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.ok_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ok_button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        self.apply_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.apply_button.setEnabled(False)
        self.apply_button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.apply_button.setCheckable(False)
        self.apply_button.setAutoExclusive(False)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_2.addWidget(self.apply_button)
        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OmniSync"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.status_tab), _translate("MainWindow", "Status"))
        self.label_3.setText(_translate("MainWindow", "Account:"))
        self.label_5.setText(_translate("MainWindow", "Folder:"))
        self.account_folder_change_button.setText(_translate("MainWindow", "..."))
        self.label_7.setText(_translate("MainWindow", "Selective Sync:"))
        self.selective_sync_check.setText(_translate("MainWindow", "Enable"))
        self.selective_sync_box.setTitle(_translate("MainWindow", "Se&lective Sync Settings"))
        self.sync_new_check.setText(_translate("MainWindow", "Sync new children of partial folders"))
        self.show_files_check.setText(_translate("MainWindow", "Show Files"))
        self.account_add_button.setText(_translate("MainWindow", "Add"))
        self.account_remove_button.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accounts_tab), _translate("MainWindow", "Accounts"))
        self.groupBox.setTitle(_translate("MainWindow", "Limits"))
        self.downloadSpeedLimitLabel.setText(_translate("MainWindow", "Download speed limit"))
        self.download_limit.setSuffix(_translate("MainWindow", " kB/s"))
        self.label_4.setText(_translate("MainWindow", "[0: unlimited]"))
        self.uploadSpeedLimitLabel.setText(_translate("MainWindow", "Upload speed limit"))
        self.upload_limit.setSuffix(_translate("MainWindow", " kB/s"))
        self.label_6.setText(_translate("MainWindow", "[0: unlimited]"))
        self.maximumSimultaneousConnectionsLabel.setText(_translate("MainWindow", "Max. simultaneous connections"))
        self.label_8.setText(_translate("MainWindow", "Default: 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Settings"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">OmniSync</span></p><p align=\"center\"><span style=\" font-size:8pt;\">version 1.0.0</span></p><p align=\"center\">Cloud-based file synchronization client for Google Drive and OneDrive</p><p align=\"center\"><br/>This program is free software and comes with ABSOLUTELY NO WARRANTY.<br/>You can redistribute it and/or modify it under the terms of the GNU General<br/>Public License as published by the Free Software Foundation, either<br/>version 3 of the License, or (at your option) any later version.</p><p align=\"center\">You should have received a copy of the GNU General Public License<br/>along with this program. If not, see <a href=\"http://www.gnu.org/licenses/\"><span style=\" text-decoration: underline; color:#2980b9;\">http://www.gnu.org/licenses/</span></a>.<br/></p><p align=\"center\">Copyright (C) 2016 André Brait</p><p align=\"center\"><a href=\"http://github.com/andrebrait/OmniSync\"><span style=\" text-decoration: underline; color:#2980b9;\">OmniSync page at GitHub</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_tab), _translate("MainWindow", "About"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))

