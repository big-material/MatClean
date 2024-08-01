import sys
from typing import Optional
import pandas as pd
from PySide6.QtCore import QDir
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem, QMessageBox, QHeaderView
import resources_rc
from pathlib import Path
from demo import Ui_Demo
from Utils import MatImputer, outlier_remove


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.df: Optional[pd.DataFrame] = None
        self.path: Optional[Path] = None
        self.ui = Ui_Demo()
        self.ui.setupUi(self)
        self.init_ui()
        # set stylesheet
        with open("ui.qss", "r") as f:
            self.setStyleSheet(f.read())
        QDir.addSearchPath('icon', 'theme')

    def init_ui(self):
        self.ui.imputation_combo_box.addItems(["MatImpute", "Mean", "Median"])
        # lineedit set not editable
        self.ui.file_path_label.setReadOnly(True)
        self.ui.file_choice_btn.clicked.connect(self.set_file)
        self.ui.missing_ratio_table.setColumnCount(2)
        self.ui.missing_ratio_table.setHorizontalHeaderLabels(["Column", "Missing Ratio"])
        # 设置表头等宽
        self.ui.missing_ratio_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.run_btn.clicked.connect(self.run_process)
        self.ui.outlier_ratio.setDisabled(True)
        self.ui.outiler_check_box.stateChanged.connect(self.outlier_state_changed)

    def set_file(self):
        # open file dialog
        file_dialog = QFileDialog()
        # csv and excel files
        file_dialog.setNameFilter("CSV Files (*.csv);;Excel Files (*.xlsx)")
        # show dialog
        file_dialog.exec()
        # get file path
        file_path = file_dialog.selectedFiles()
        if len(file_path) > 0:
            self.df = pd.read_csv(file_path[0])
            self.path = Path(file_path[0])
            self.ui.file_path_label.setText(file_path[0])
            # set the missing ratio table
            self.ui.missing_ratio_table.setRowCount(len(self.df.columns))
            for i, column in enumerate(self.df.columns):
                missing_ratio = self.df[column].isnull().sum() / len(self.df)
                self.ui.missing_ratio_table.setItem(i, 0, QTableWidgetItem(column))
                self.ui.missing_ratio_table.setItem(i, 1, QTableWidgetItem(str(missing_ratio)))
            self.ui.target_comboBox.addItems(self.df.columns.tolist())

    def run_process(self):
        if self.df is None:
            QMessageBox.warning(self, "警告⚠", "请先选择文件")
            return
        method = self.ui.imputation_combo_box.currentText()
        if method == "":
            QMessageBox.warning(self, "警告⚠", "请选择填充方法")
            return
        # fill missing values
        if method == "Mean":
            self.df = self.df.fillna(self.df.mean())
        elif method == "Median":
            self.df = self.df.fillna(self.df.median())
        else:
            matimputer = MatImputer()
            self.df = matimputer.transform(self.df)
        # remove outliers
        if self.ui.outiler_check_box.isChecked():
            ratio = self.ui.outlier_ratio.text()
            try:
                ratio = float(ratio)
            except ValueError:
                QMessageBox.warning(self, "警告⚠", "异常值比例必须为数字")
                return
            if ratio < 0 or ratio > 1:
                QMessageBox.warning(self, "警告⚠", "异常值比例必须在0-1之间")
                return
            if ratio > 0.1:
                QMessageBox.warning(self, "警告⚠", "异常值比例建议小于0.1")
            self.df = outlier_remove(self.df, target_col=self.ui.target_comboBox.currentText(), threshold=ratio)
        QMessageBox.information(self, "成功", f"处理{self.path.stem}成功！！！")
        self.df.to_csv(self.path.parent / f"{self.path.stem}_processed.csv", index=False)

    def outlier_state_changed(self):
        if self.ui.outiler_check_box.isChecked():
            self.ui.outlier_ratio.setDisabled(False)
        else:
            self.ui.outlier_ratio.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(1000, 800)
    window.setWindowIcon(QIcon("icon.ico"))
    window.show()
    sys.exit(app.exec())
