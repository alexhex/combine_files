# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'st.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(610, 617)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 611, 81))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(11)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.get_dest_folder = QPushButton(self.gridLayoutWidget)
        self.get_dest_folder.setObjectName(u"get_dest_folder")
        self.get_dest_folder.setFont(font)

        self.gridLayout_2.addWidget(self.get_dest_folder, 0, 1, 1, 1)

        self.get_rsc_folder = QPushButton(self.gridLayoutWidget)
        self.get_rsc_folder.setObjectName(u"get_rsc_folder")
        self.get_rsc_folder.setFont(font)

        self.gridLayout_2.addWidget(self.get_rsc_folder, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 120, 611, 411))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mssg_brd = QTextBrowser(self.verticalLayoutWidget)
        self.mssg_brd.setObjectName(u"mssg_brd")
        self.mssg_brd.setFont(font)

        self.verticalLayout.addWidget(self.mssg_brd)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 570, 611, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rplc_btn = QPushButton(self.horizontalLayoutWidget)
        self.rplc_btn.setObjectName(u"rplc_btn")
        self.rplc_btn.setFont(font)

        self.horizontalLayout.addWidget(self.rplc_btn)

        self.reset_btn = QPushButton(self.horizontalLayoutWidget)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setFont(font)

        self.horizontalLayout.addWidget(self.reset_btn)

        self.horizontalLayoutWidget_2 = QWidget(Dialog)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 530, 611, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cp_clpbrd = QPushButton(self.horizontalLayoutWidget_2)
        self.cp_clpbrd.setObjectName(u"cp_clpbrd")
        self.cp_clpbrd.setFont(font)

        self.horizontalLayout_2.addWidget(self.cp_clpbrd)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayoutWidget_3 = QWidget(Dialog)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 80, 611, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.prpr_btn = QPushButton(self.horizontalLayoutWidget_3)
        self.prpr_btn.setObjectName(u"prpr_btn")
        self.prpr_btn.setFont(font)

        self.horizontalLayout_3.addWidget(self.prpr_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Please specify the destination folder", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Please specify the resource folder", None))
        self.get_dest_folder.setText(QCoreApplication.translate("Dialog", u"Specify", None))
        self.get_rsc_folder.setText(QCoreApplication.translate("Dialog", u"Specify", None))
        self.rplc_btn.setText(QCoreApplication.translate("Dialog", u"Replace", None))
        self.reset_btn.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.cp_clpbrd.setText(QCoreApplication.translate("Dialog", u"Copy Notes to Clipboard", None))
        self.prpr_btn.setText(QCoreApplication.translate("Dialog", u"Prepare", None))
    # retranslateUi

