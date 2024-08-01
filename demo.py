# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton,
                               QTableWidget, QVBoxLayout)

class Ui_Demo(object):
    def setupUi(self, Demo):
        if not Demo.objectName():
            Demo.setObjectName(u"Demo")
        Demo.resize(596, 353)
        self.verticalLayout_2 = QVBoxLayout(Demo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(Demo)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Fira Code"])
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Demo)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.file_path_label = QLineEdit(Demo)
        self.file_path_label.setObjectName(u"file_path_label")

        self.horizontalLayout_4.addWidget(self.file_path_label)

        self.file_choice_btn = QPushButton(Demo)
        self.file_choice_btn.setObjectName(u"file_choice_btn")

        self.horizontalLayout_4.addWidget(self.file_choice_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Demo)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.missing_ratio_table = QTableWidget(Demo)
        self.missing_ratio_table.setObjectName(u"missing_ratio_table")

        self.horizontalLayout_2.addWidget(self.missing_ratio_table)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Demo)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.imputation_combo_box = QComboBox(Demo)
        self.imputation_combo_box.setObjectName(u"imputation_combo_box")

        self.horizontalLayout_3.addWidget(self.imputation_combo_box)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.outiler_check_box = QCheckBox(Demo)
        self.outiler_check_box.setObjectName(u"outiler_check_box")

        self.horizontalLayout_5.addWidget(self.outiler_check_box)

        self.label_5 = QLabel(Demo)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.target_comboBox = QComboBox(Demo)
        self.target_comboBox.setObjectName(u"target_comboBox")

        self.horizontalLayout_5.addWidget(self.target_comboBox)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Demo)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.outlier_ratio = QLineEdit(Demo)
        self.outlier_ratio.setObjectName(u"outlier_ratio")

        self.horizontalLayout.addWidget(self.outlier_ratio)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.run_btn = QPushButton(Demo)
        self.run_btn.setObjectName(u"run_btn")

        self.verticalLayout_2.addWidget(self.run_btn)


        self.retranslateUi(Demo)

        QMetaObject.connectSlotsByName(Demo)
    # setupUi

    def retranslateUi(self, Demo):
        Demo.setWindowTitle(QCoreApplication.translate("Demo", u"Form", None))
        self.title.setText(QCoreApplication.translate("Demo", u"Dataset Process", None))
        self.label_4.setText(QCoreApplication.translate("Demo", u"\u6587\u4ef6\u8def\u5f84(\u652f\u6301csv,excel)", None))
        self.file_choice_btn.setText(QCoreApplication.translate("Demo", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("Demo", u"\u7f3a\u5931\u503c\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("Demo", u"\u7f3a\u5931\u503c\u586b\u5145\u7b97\u6cd5", None))
        self.outiler_check_box.setText(QCoreApplication.translate("Demo", u"\u662f\u5426\u8fdb\u884c\u5f02\u5e38\u503c\u5254\u9664", None))
        self.label_5.setText(QCoreApplication.translate("Demo", u"\u76ee\u6807\u5217", None))
        self.label.setText(QCoreApplication.translate("Demo", u"\u5254\u9664\u5927\u5c0f(<= 0.1)", None))
        self.run_btn.setText(QCoreApplication.translate("Demo", u"Run!", None))
    # retranslateUi

