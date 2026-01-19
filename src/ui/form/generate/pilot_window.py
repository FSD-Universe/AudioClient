# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pilot_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from src.ui.component.selected_button import SelectedButton

class Ui_ClientWindow(object):
    def setupUi(self, ClientWindow):
        if not ClientWindow.objectName():
            ClientWindow.setObjectName(u"ClientWindow")
        ClientWindow.resize(512, 348)
        ClientWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Leelawadee UI"])
        font.setPointSize(10)
        ClientWindow.setFont(font)
        self.gridLayout_2 = QGridLayout(ClientWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.group_controllers = QGroupBox(ClientWindow)
        self.group_controllers.setObjectName(u"group_controllers")
        self.group_controllers.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_controllers.sizePolicy().hasHeightForWidth())
        self.group_controllers.setSizePolicy(sizePolicy)
        self.group_controllers.setFont(font)
        self.verticalLayout = QVBoxLayout(self.group_controllers)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.controller_list = QVBoxLayout()
        self.controller_list.setObjectName(u"controller_list")

        self.verticalLayout.addLayout(self.controller_list)

        self.spacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacer_2)


        self.gridLayout_2.addWidget(self.group_controllers, 0, 1, 3, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.group_com = QGroupBox(ClientWindow)
        self.group_com.setObjectName(u"group_com")
        self.group_com.setFont(font)
        self.gridLayout_3 = QGridLayout(self.group_com)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layout_coms = QGridLayout()
        self.layout_coms.setObjectName(u"layout_coms")
        self.button_com2_rx = SelectedButton(self.group_com)
        self.button_com2_rx.setObjectName(u"button_com2_rx")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_com2_rx.sizePolicy().hasHeightForWidth())
        self.button_com2_rx.setSizePolicy(sizePolicy1)

        self.layout_coms.addWidget(self.button_com2_rx, 1, 3, 1, 1)

        self.label_com2_freq = QLineEdit(self.group_com)
        self.label_com2_freq.setObjectName(u"label_com2_freq")
        sizePolicy1.setHeightForWidth(self.label_com2_freq.sizePolicy().hasHeightForWidth())
        self.label_com2_freq.setSizePolicy(sizePolicy1)

        self.layout_coms.addWidget(self.label_com2_freq, 1, 1, 1, 1)

        self.label_com1_freq = QLineEdit(self.group_com)
        self.label_com1_freq.setObjectName(u"label_com1_freq")
        sizePolicy1.setHeightForWidth(self.label_com1_freq.sizePolicy().hasHeightForWidth())
        self.label_com1_freq.setSizePolicy(sizePolicy1)

        self.layout_coms.addWidget(self.label_com1_freq, 0, 1, 1, 1)

        self.button_com2_tx = SelectedButton(self.group_com)
        self.button_com2_tx.setObjectName(u"button_com2_tx")
        sizePolicy1.setHeightForWidth(self.button_com2_tx.sizePolicy().hasHeightForWidth())
        self.button_com2_tx.setSizePolicy(sizePolicy1)

        self.layout_coms.addWidget(self.button_com2_tx, 1, 2, 1, 1)

        self.label_com2 = QLabel(self.group_com)
        self.label_com2.setObjectName(u"label_com2")
        sizePolicy.setHeightForWidth(self.label_com2.sizePolicy().hasHeightForWidth())
        self.label_com2.setSizePolicy(sizePolicy)
        self.label_com2.setMinimumSize(QSize(80, 0))
        font1 = QFont()
        font1.setFamilies([u"Leelawadee UI"])
        font1.setPointSize(12)
        self.label_com2.setFont(font1)

        self.layout_coms.addWidget(self.label_com2, 1, 0, 1, 1)

        self.label_com1 = QLabel(self.group_com)
        self.label_com1.setObjectName(u"label_com1")
        sizePolicy.setHeightForWidth(self.label_com1.sizePolicy().hasHeightForWidth())
        self.label_com1.setSizePolicy(sizePolicy)
        self.label_com1.setMinimumSize(QSize(80, 0))
        self.label_com1.setFont(font1)

        self.layout_coms.addWidget(self.label_com1, 0, 0, 1, 1)

        self.button_com1_tx = SelectedButton(self.group_com)
        self.button_com1_tx.setObjectName(u"button_com1_tx")
        sizePolicy1.setHeightForWidth(self.button_com1_tx.sizePolicy().hasHeightForWidth())
        self.button_com1_tx.setSizePolicy(sizePolicy1)

        self.layout_coms.addWidget(self.button_com1_tx, 0, 2, 1, 1)

        self.button_com1_rx = SelectedButton(self.group_com)
        self.button_com1_rx.setObjectName(u"button_com1_rx")
        sizePolicy1.setHeightForWidth(self.button_com1_rx.sizePolicy().hasHeightForWidth())
        self.button_com1_rx.setSizePolicy(sizePolicy1)

        self.layout_coms.addWidget(self.button_com1_rx, 0, 3, 1, 1)


        self.gridLayout_3.addLayout(self.layout_coms, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.group_com, 0, 0, 1, 1)

        self.group_info = QGroupBox(ClientWindow)
        self.group_info.setObjectName(u"group_info")
        self.gridLayout_4 = QGridLayout(self.group_info)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.com1_standby_v = QLabel(self.group_info)
        self.com1_standby_v.setObjectName(u"com1_standby_v")

        self.gridLayout_4.addWidget(self.com1_standby_v, 1, 1, 1, 1)

        self.com2_active = QLabel(self.group_info)
        self.com2_active.setObjectName(u"com2_active")

        self.gridLayout_4.addWidget(self.com2_active, 3, 0, 1, 1)

        self.com1_active_v = QLabel(self.group_info)
        self.com1_active_v.setObjectName(u"com1_active_v")

        self.gridLayout_4.addWidget(self.com1_active_v, 0, 1, 1, 1)

        self.com2_standby = QLabel(self.group_info)
        self.com2_standby.setObjectName(u"com2_standby")

        self.gridLayout_4.addWidget(self.com2_standby, 4, 0, 1, 1)

        self.com1_standby = QLabel(self.group_info)
        self.com1_standby.setObjectName(u"com1_standby")

        self.gridLayout_4.addWidget(self.com1_standby, 1, 0, 1, 1)

        self.sync_receive_flag = QCheckBox(self.group_info)
        self.sync_receive_flag.setObjectName(u"sync_receive_flag")
        self.sync_receive_flag.setChecked(True)

        self.gridLayout_4.addWidget(self.sync_receive_flag, 7, 0, 1, 2)

        self.com1_receive = QLabel(self.group_info)
        self.com1_receive.setObjectName(u"com1_receive")

        self.gridLayout_4.addWidget(self.com1_receive, 2, 0, 1, 1)

        self.com2_standby_v = QLabel(self.group_info)
        self.com2_standby_v.setObjectName(u"com2_standby_v")

        self.gridLayout_4.addWidget(self.com2_standby_v, 4, 1, 1, 1)

        self.sync_frequency = QCheckBox(self.group_info)
        self.sync_frequency.setObjectName(u"sync_frequency")
        self.sync_frequency.setChecked(True)

        self.gridLayout_4.addWidget(self.sync_frequency, 6, 0, 1, 2)

        self.com1_active = QLabel(self.group_info)
        self.com1_active.setObjectName(u"com1_active")

        self.gridLayout_4.addWidget(self.com1_active, 0, 0, 1, 1)

        self.com2_active_v = QLabel(self.group_info)
        self.com2_active_v.setObjectName(u"com2_active_v")

        self.gridLayout_4.addWidget(self.com2_active_v, 3, 1, 1, 1)

        self.com2_receive = QLabel(self.group_info)
        self.com2_receive.setObjectName(u"com2_receive")

        self.gridLayout_4.addWidget(self.com2_receive, 5, 0, 1, 1)

        self.com2_receive_v = QLabel(self.group_info)
        self.com2_receive_v.setObjectName(u"com2_receive_v")

        self.gridLayout_4.addWidget(self.com2_receive_v, 5, 1, 1, 1)

        self.com1_receive_v = QLabel(self.group_info)
        self.com1_receive_v.setObjectName(u"com1_receive_v")

        self.gridLayout_4.addWidget(self.com1_receive_v, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.group_info, 1, 0, 1, 1)


        self.retranslateUi(ClientWindow)

        QMetaObject.connectSlotsByName(ClientWindow)
    # setupUi

    def retranslateUi(self, ClientWindow):
        ClientWindow.setWindowTitle(QCoreApplication.translate("ClientWindow", u"PilotClient", None))
        self.group_controllers.setTitle(QCoreApplication.translate("ClientWindow", u"\u5728\u7ebf\u7ba1\u5236\u5458", None))
        self.group_com.setTitle(QCoreApplication.translate("ClientWindow", u"\u901a\u8baf\u9762\u677f", None))
        self.button_com2_rx.setText(QCoreApplication.translate("ClientWindow", u"RX", None))
        self.label_com2_freq.setText(QCoreApplication.translate("ClientWindow", u"---.---", None))
        self.label_com1_freq.setText(QCoreApplication.translate("ClientWindow", u"---.---", None))
        self.button_com2_tx.setText(QCoreApplication.translate("ClientWindow", u"TX", None))
        self.label_com2.setText(QCoreApplication.translate("ClientWindow", u"COM2:", None))
        self.label_com1.setText(QCoreApplication.translate("ClientWindow", u"COM1:", None))
        self.button_com1_tx.setText(QCoreApplication.translate("ClientWindow", u"TX", None))
        self.button_com1_rx.setText(QCoreApplication.translate("ClientWindow", u"RX", None))
        self.group_info.setTitle(QCoreApplication.translate("ClientWindow", u"\u901a\u8baf\u6570\u636e", None))
        self.com1_standby_v.setText(QCoreApplication.translate("ClientWindow", u"---.---", None))
        self.com2_active.setText(QCoreApplication.translate("ClientWindow", u"COM2", None))
        self.com1_active_v.setText(QCoreApplication.translate("ClientWindow", u"---.---", None))
        self.com2_standby.setText(QCoreApplication.translate("ClientWindow", u"COM2 Standby", None))
        self.com1_standby.setText(QCoreApplication.translate("ClientWindow", u"COM1 Standby", None))
        self.sync_receive_flag.setText(QCoreApplication.translate("ClientWindow", u"\u540c\u6b65\u673a\u6a21\u63a5\u6536\u6807\u5fd7\u4f4d", None))
        self.com1_receive.setText(QCoreApplication.translate("ClientWindow", u"COM1 Receive", None))
        self.com2_standby_v.setText(QCoreApplication.translate("ClientWindow", u"---.---", None))
        self.sync_frequency.setText(QCoreApplication.translate("ClientWindow", u"\u540c\u6b65\u673a\u6a21COM\u9891\u7387", None))
        self.com1_active.setText(QCoreApplication.translate("ClientWindow", u"COM1", None))
        self.com2_active_v.setText(QCoreApplication.translate("ClientWindow", u"---.---", None))
        self.com2_receive.setText(QCoreApplication.translate("ClientWindow", u"COM2 Receive", None))
        self.com2_receive_v.setText(QCoreApplication.translate("ClientWindow", u"\u5426", None))
        self.com1_receive_v.setText(QCoreApplication.translate("ClientWindow", u"\u5426", None))
    # retranslateUi

