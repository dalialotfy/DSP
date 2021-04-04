# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 850)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("open.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 10, 31, 31))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 70, 31, 31))
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 70, 31, 31))
        self.pushButton_6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 70, 31, 31))
        self.pushButton_7.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoom out.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 70, 31, 31))
        self.pushButton_8.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zoom in.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 70, 31, 31))
        self.pushButton_9.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("play.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(170, 70, 31, 31))
        self.pushButton_10.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pause.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon8)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 1071, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1069, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 160, 1071, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1050, 0, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.Channel1 = PlotWidget(self.scrollAreaWidgetContents)
        self.Channel1.setGeometry(QtCore.QRect(0, 0, 1051, 161))
        self.Channel1.setObjectName("Channel1")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 360, 1071, 181))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1069, 179))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalScrollBar_4 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_4)
        self.horizontalScrollBar_4.setGeometry(QtCore.QRect(0, 160, 1071, 16))
        self.horizontalScrollBar_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_4.setObjectName("horizontalScrollBar_4")
        self.verticalScrollBar_4 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_4)
        self.verticalScrollBar_4.setGeometry(QtCore.QRect(1050, 0, 16, 160))
        self.verticalScrollBar_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_4.setObjectName("verticalScrollBar_4")
        self.Channel2 = PlotWidget(self.scrollAreaWidgetContents_4)
        self.Channel2.setGeometry(QtCore.QRect(0, -1, 1051, 161))
        self.Channel2.setObjectName("Channel2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(130, 320, 31, 31))
        self.pushButton_11.setText("")
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 320, 31, 31))
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(50, 320, 31, 31))
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(210, 320, 31, 31))
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(90, 320, 31, 31))
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(170, 320, 31, 31))
        self.pushButton_16.setText("")
        self.pushButton_16.setIcon(icon8)
        self.pushButton_16.setObjectName("pushButton_16")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 610, 1071, 181))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1069, 179))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.horizontalScrollBar_5 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_5)
        self.horizontalScrollBar_5.setGeometry(QtCore.QRect(0, 160, 1071, 16))
        self.horizontalScrollBar_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_5.setObjectName("horizontalScrollBar_5")
        self.verticalScrollBar_5 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_5)
        self.verticalScrollBar_5.setGeometry(QtCore.QRect(1050, 0, 16, 160))
        self.verticalScrollBar_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_5.setObjectName("verticalScrollBar_5")
        self.Channel3 = PlotWidget(self.scrollAreaWidgetContents_5)
        self.Channel3.setGeometry(QtCore.QRect(0, 0, 1051, 161))
        self.Channel3.setObjectName("Channel3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(130, 570, 31, 31))
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon6)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 570, 31, 31))
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon3)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(50, 570, 31, 31))
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon4)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(210, 570, 31, 31))
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon7)
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 550, 81, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(90, 570, 31, 31))
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon5)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(170, 570, 31, 31))
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon8)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 70, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(250, 320, 151, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(250, 570, 151, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuOpen = QtWidgets.QMenu(self.menufile)
        self.menuOpen.setIcon(icon)
        self.menuOpen.setObjectName("menuOpen")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Project.setIcon(icon9)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setIcon(icon1)
        self.actionClose.setObjectName("actionClose")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("undo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon10)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("redo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon11)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionProject = QtWidgets.QAction(MainWindow)
        self.actionProject.setObjectName("actionProject")
        self.actionAdd_Toolbar = QtWidgets.QAction(MainWindow)
        self.actionAdd_Toolbar.setObjectName("actionAdd_Toolbar")
        self.actionAdd_Files = QtWidgets.QAction(MainWindow)
        self.actionAdd_Files.setObjectName("actionAdd_Files")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSupport = QtWidgets.QAction(MainWindow)
        self.actionSupport.setObjectName("actionSupport")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionChannel1 = QtWidgets.QAction(MainWindow)
        self.actionChannel1.setObjectName("actionChannel1")
        self.actionChannel2 = QtWidgets.QAction(MainWindow)
        self.actionChannel2.setObjectName("actionChannel2")
        self.actionChannel3 = QtWidgets.QAction(MainWindow)
        self.actionChannel3.setObjectName("actionChannel3")
        self.menuOpen.addAction(self.actionChannel1)
        self.menuOpen.addAction(self.actionChannel2)
        self.menuOpen.addAction(self.actionChannel3)
        self.menufile.addAction(self.actionNew_Project)
        self.menufile.addAction(self.menuOpen.menuAction())
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionSave_As)
        self.menufile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuView.addAction(self.actionProject)
        self.menuView.addAction(self.actionAdd_Toolbar)
        self.menuProject.addAction(self.actionAdd_Files)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionSupport)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Esc"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "Ctrl+E, Ctrl+1"))
        self.pushButton_6.setShortcut(_translate("MainWindow", "Ctrl+=, Ctrl+1"))
        self.pushButton_7.setShortcut(_translate("MainWindow", "Ctrl+-, Ctrl+1"))
        self.pushButton_9.setShortcut(_translate("MainWindow", "Ctrl+P, Ctrl+1"))
        self.pushButton_9.setEnabled(False)
        self.pushButton_10.setShortcut(_translate("MainWindow", "Ctrl+Z, Ctrl+1"))
        self.label.setText(_translate("MainWindow", "Channel :1"))
        self.pushButton_14.setShortcut(_translate("MainWindow", "Ctrl+P,Ctrl+2"))
        self.pushButton_14.setEnabled(False)
        self.pushButton_16.setShortcut(_translate("MainWindow", "Ctrl+Z, Ctrl+2"))
        self.pushButton_12.setShortcut(_translate("MainWindow", "Ctrl+E,Ctrl+2"))
        self.pushButton_13.setShortcut(_translate("MainWindow", "Ctrl+=,Ctrl+2"))
        self.pushButton_15.setShortcut(_translate("MainWindow", "Ctrl+-,Ctrl+2"))
        self.label_2.setText(_translate("MainWindow", "Channel :2"))
        self.pushButton_20.setShortcut(_translate("MainWindow", "Ctrl+P, Ctrl+3"))
        self.pushButton_20.setEnabled(False)
        self.pushButton_22.setShortcut(_translate("MainWindow", "Ctrl+Z, Ctrl+3"))
        self.pushButton_18.setShortcut(_translate("MainWindow", "Ctrl+E, Ctrl+3"))
        self.pushButton_19.setShortcut(_translate("MainWindow", "Ctrl+=, Ctrl+3"))
        self.pushButton_21.setShortcut(_translate("MainWindow", "Ctrl+-, Ctrl+3"))
        self.label_3.setText(_translate("MainWindow", "Channel :3"))
        self.pushButton.setText(_translate("MainWindow", "Generate Spectrogram"))
        self.pushButton.setShortcut(_translate("MainWindow", "Ctrl+G, Ctrl+1"))
        self.pushButton_23.setText(_translate("MainWindow", "Generate Spectrogram"))
        self.pushButton_23.setShortcut(_translate("MainWindow", "Ctrl+G, Ctrl+2"))
        self.pushButton_24.setText(_translate("MainWindow", "Generate Spectrogram"))
        self.pushButton_24.setShortcut(_translate("MainWindow", "Ctrl+G, Ctrl+3"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_Project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Esc"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionProject.setText(_translate("MainWindow", "Project"))
        self.actionAdd_Toolbar.setText(_translate("MainWindow", "Add Toolbar"))
        self.actionAdd_Files.setText(_translate("MainWindow", "Add Files"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionSupport.setText(_translate("MainWindow", "Support"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionChannel1.setText(_translate("MainWindow", "Channel1"))
        self.actionChannel1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionChannel2.setText(_translate("MainWindow", "Channel2"))
        self.actionChannel2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionChannel3.setText(_translate("MainWindow", "Channel3"))
        self.actionChannel3.setShortcut(_translate("MainWindow", "Ctrl+3"))
from pyqtgraph import PlotWidget