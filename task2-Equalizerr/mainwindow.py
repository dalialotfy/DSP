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
        MainWindow.resize(1593, 1007)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scroll_left_button = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_left_button.setGeometry(QtCore.QRect(10, 70, 31, 31))
        self.scroll_left_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_left_button.setIcon(icon)
        self.scroll_left_button.setObjectName("scroll_left_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label.setObjectName("label")
        self.set_min_frequency = QtWidgets.QSlider(self.centralwidget)
        self.set_min_frequency.setGeometry(QtCore.QRect(1120, 660, 241, 22))
        self.set_min_frequency.setOrientation(QtCore.Qt.Horizontal)
        self.set_min_frequency.setObjectName("set_min_frequency")
        self.zoom_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in_button.setGeometry(QtCore.QRect(170, 70, 31, 31))
        self.zoom_in_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("zoom in.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in_button.setIcon(icon1)
        self.zoom_in_button.setObjectName("zoom_in_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1250, 80, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(950, 660, 151, 16))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 80, 71, 16))
        self.label_3.setObjectName("label_3")
        # self.scroll_up_button_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.scroll_up_button_3.setGeometry(QtCore.QRect(90, 10, 31, 31))
        # self.scroll_up_button_3.setText("")
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap("../new ui/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.scroll_up_button_3.setIcon(icon2)
        # self.scroll_up_button_3.setObjectName("scroll_up_button_3")
        self.set_speed_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.set_speed_spinBox.setGeometry(QtCore.QRect(610, 70, 41, 31))
        self.set_speed_spinBox.setObjectName("set_speed_spinBox")
        self.spectrogram_area = QtWidgets.QLabel(self.centralwidget)
        self.spectrogram_area.setGeometry(QtCore.QRect(870, 110, 691, 481))
        # self.spectrogram_area.setWidgetResizable(True)
        self.spectrogram_area.setScaledContents(True)
        self.spectrogram_area.setObjectName("spectrogram_area")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 689, 279))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        # self.spectrogram_area.setWidget(self.scrollAreaWidgetContents_7)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 610, 81, 16))
        self.label_4.setObjectName("label_4")
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(290, 70, 31, 31))
        self.pause_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pause.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon3)
        self.pause_button.setObjectName("pause_button")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(250, 70, 31, 31))
        self.play_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("play.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon4)
        self.play_button.setObjectName("play_button")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 781, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 779, 189))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.input_channel = PlotWidget(self.scrollAreaWidgetContents_2)
        self.input_channel.setGeometry(QtCore.QRect(-1, -1, 781, 191))
        self.input_channel.setObjectName("input_channel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.zoom_out_button = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out_button.setGeometry(QtCore.QRect(210, 70, 31, 31))
        self.zoom_out_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoom out.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out_button.setIcon(icon5)
        self.zoom_out_button.setObjectName("zoom_out_button")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 630, 781, 191))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 779, 189))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.output_channel = PlotWidget(self.scrollAreaWidgetContents_4)
        self.output_channel.setGeometry(QtCore.QRect(0, -1, 781, 191))
        self.output_channel.setObjectName("output_channel")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.show_hide_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.show_hide_checkbox.setGeometry(QtCore.QRect(1470, 620, 91, 20))
        self.show_hide_checkbox.setObjectName("show_hide_checkbox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 101, 20))
        self.label_2.setObjectName("label_2")
        self.set_max_frequency = QtWidgets.QSlider(self.centralwidget)
        self.set_max_frequency.setGeometry(QtCore.QRect(1120, 620, 241, 22))
        self.set_max_frequency.setOrientation(QtCore.Qt.Horizontal)
        self.set_max_frequency.setObjectName("set_max_frequency")
        self.choose_pallette_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.choose_pallette_combobox.setGeometry(QtCore.QRect(1390, 80, 171, 22))
        self.choose_pallette_combobox.setObjectName("choose_pallette_combobox")
        self.choose_pallette_combobox.addItem("")
        self.choose_pallette_combobox.addItem("")
        self.choose_pallette_combobox.addItem("")
        self.choose_pallette_combobox.addItem("")
        self.choose_pallette_combobox.addItem("")
        # self.scrollArea_4 = QtWidgets.QLabel(self.centralwidget)
        # self.scrollArea_4.setGeometry(QtCore.QRect(870, 110, 691, 281))
        # # self.scrollArea_4.setWidgetResizable(True)
        # self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 689, 279))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.spectro1 = QtWidgets.QWidget(self.scrollAreaWidgetContents_6)
        self.spectro1.setGeometry(QtCore.QRect(0, -1, 691, 281))
        self.spectro1.setObjectName("spectro1")
        # self.scrollArea_4.setScaledContents(True)
        # self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.save_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon6)
        self.save_button.setObjectName("save_button")
        # self.label_9 = QtWidgets.QLabel(self.centralwidget)
        # self.label_9.setGeometry(QtCore.QRect(870, 510, 141, 16))
        # self.label_9.setObjectName("label_9")
        self.equalizer_area = QtWidgets.QScrollArea(self.centralwidget)
        self.equalizer_area.setGeometry(QtCore.QRect(10, 370, 781, 191))
        self.equalizer_area.setWidgetResizable(True)
        self.equalizer_area.setObjectName("equalizer_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 779, 189))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gain_slider_1 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_1.setGeometry(QtCore.QRect(20, 10, 22, 160))
        self.gain_slider_1.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_1.setObjectName("gain_slider_1")
        self.gain_slider_10 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_10.setGeometry(QtCore.QRect(740, 10, 22, 160))
        self.gain_slider_10.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_10.setObjectName("gain_slider_10")
        self.gain_slider_2 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_2.setGeometry(QtCore.QRect(100, 10, 22, 160))
        self.gain_slider_2.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_2.setObjectName("gain_slider_2")
        self.gain_slider_3 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_3.setGeometry(QtCore.QRect(180, 10, 22, 160))
        self.gain_slider_3.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_3.setObjectName("gain_slider_3")
        self.gain_slider_7 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_7.setGeometry(QtCore.QRect(500, 10, 22, 160))
        self.gain_slider_7.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_7.setObjectName("gain_slider_7")
        self.gain_slider_4 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_4.setGeometry(QtCore.QRect(260, 10, 22, 160))
        self.gain_slider_4.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_4.setObjectName("gain_slider_4")
        self.gain_slider_5 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_5.setGeometry(QtCore.QRect(340, 10, 22, 160))
        self.gain_slider_5.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_5.setObjectName("gain_slider_5")
        self.gain_slider_6 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_6.setGeometry(QtCore.QRect(420, 10, 22, 160))
        self.gain_slider_6.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_6.setObjectName("gain_slider_6")
        self.gain_slider_8 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_8.setGeometry(QtCore.QRect(580, 10, 22, 160))
        self.gain_slider_8.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_8.setObjectName("gain_slider_8")
        self.gain_slider_9 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.gain_slider_9.setGeometry(QtCore.QRect(660, 10, 22, 160))
        self.gain_slider_9.setOrientation(QtCore.Qt.Vertical)
        self.gain_slider_9.setObjectName("gain_slider_9")
        self.equalizer_area.setWidget(self.scrollAreaWidgetContents_3)
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.open_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("open.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_button.setIcon(icon7)
        self.open_button.setObjectName("open_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(870, 80, 141, 16))
        self.label_5.setObjectName("label_5")
        self.scroll_right_button = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_right_button.setGeometry(QtCore.QRect(50, 70, 31, 31))
        self.scroll_right_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_right_button.setIcon(icon8)
        self.scroll_right_button.setObjectName("scroll_right_button")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(950, 620, 151, 16))
        self.label_7.setObjectName("label_7")
        # self.show_hide_checkbox_2 = QtWidgets.QCheckBox(self.centralwidget)
        # self.show_hide_checkbox_2.setGeometry(QtCore.QRect(1470, 650, 91, 20))
        # self.show_hide_checkbox_2.setObjectName("show_hide_checkbox_2")
        self.scroll_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_up_button.setGeometry(QtCore.QRect(90, 70, 31, 31))
        self.scroll_up_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("up.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_up_button.setIcon(icon9)
        self.scroll_up_button.setObjectName("scroll_up_button")
        self.scroll_down_button = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_down_button.setGeometry(QtCore.QRect(130, 70, 31, 31))
        self.scroll_down_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_down_button.setIcon(icon10)
        self.scroll_down_button.setObjectName("scroll_down_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1593, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Project.setIcon(icon11)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        # self.actionClose = QtWidgets.QAction(MainWindow)
        # self.actionClose.setIcon(icon2)
        # self.actionClose.setObjectName("actionClose")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("undo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon12)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../new ui/redo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon13)
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
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon7)
        self.actionOpen.setObjectName("actionOpen")
        self.menufile.addAction(self.actionNew_Project)
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionSave_As)
        # self.menufile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionSelect_All)
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
        self.scroll_left_button.setShortcut(_translate("MainWindow", "Ctrl+l"))
        self.label.setText(_translate("MainWindow", "Input Signal"))
        self.zoom_in_button.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.label_6.setText(_translate("MainWindow", "Choose Color Pallette"))
        self.label_8.setText(_translate("MainWindow", "Set Maximum Frequency"))
        self.label_3.setText(_translate("MainWindow", "Set Speed"))
        # self.scroll_up_button_3.setShortcut(_translate("MainWindow", "Esc"))
        self.label_4.setText(_translate("MainWindow", "Output Signal"))
        self.pause_button.setShortcut(_translate("MainWindow", "Ctrl+x"))
        self.play_button.setShortcut(_translate("MainWindow", "Ctrl+p"))
        self.zoom_out_button.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.show_hide_checkbox.setText(_translate("MainWindow", "Hide"))
        self.label_2.setText(_translate("MainWindow", "Signal Equalizer"))
        self.choose_pallette_combobox.setItemText(0, _translate("MainWindow", "Pallette 1"))
        self.choose_pallette_combobox.setItemText(1, _translate("MainWindow", "Pallette 2"))
        self.choose_pallette_combobox.setItemText(2, _translate("MainWindow", "Pallette 3"))
        self.choose_pallette_combobox.setItemText(3, _translate("MainWindow", "Pallette 4"))
        self.choose_pallette_combobox.setItemText(4, _translate("MainWindow", "Pallette 5"))
        self.save_button.setShortcut(_translate("MainWindow", "Ctrl+s"))
        self.open_button.setShortcut(_translate("MainWindow", "Ctrl+o"))
        self.label_5.setText(_translate("MainWindow", "Spectrogram"))
        self.scroll_right_button.setShortcut(_translate("MainWindow", "Ctrl+r"))
        self.label_7.setText(_translate("MainWindow", "Set Minimum Frequency"))
        # self.show_hide_checkbox_2.setText(_translate("MainWindow", "Show"))
        self.scroll_up_button.setShortcut(_translate("MainWindow", "Ctrl+u"))
        self.scroll_down_button.setShortcut(_translate("MainWindow", "Ctrl+d"))      ####################
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Window"))
        self.actionNew_Project.setShortcut(_translate("MainWindow", "Ctrl+n"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        # self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+s"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+a"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionProject.setText(_translate("MainWindow", "Show/Hide Spectrogram"))
        # self.actionProject.setShortcut(_translate("MainWindow", "Ctrl+h"))
        self.actionAdd_Toolbar.setText(_translate("MainWindow", "Add Toolbar"))
        self.actionAdd_Files.setText(_translate("MainWindow", "Add Files"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionSupport.setText(_translate("MainWindow", "Support"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        # self.actionChannel1.setText(_translate("MainWindow", "New"))
        # self.actionChannel1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        # self.actionChannel2.setText(_translate("MainWindow", "Channel2"))
        # self.actionChannel2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        # self.actionChannel3.setText(_translate("MainWindow", "Channel3"))
        # self.actionChannel3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        # self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.show_hide_checkbox.setShortcut(_translate("MainWindow", "Ctrl+h"))
        # self.show_hide_checkbox_2.setShortcut(_translate("MainWindow", "Ctrl+v"))
        
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
