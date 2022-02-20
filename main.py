# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : todo
# @Time  : 22/02/20 17:37
from PySide2.QtCore import QFile, QUrl
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileDialog, QMessageBox, QApplication


class BatchModify:
    def __init__(self):
        qfile_stats = QFile("./ui/batch_modify_file_name.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如： self.ui.button,self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.selectDirButton.clicked.connect(self.get_files_dir)

    def get_files_dir(self):
        q_url = QFileDialog.getExistingDirectoryUrl()
        files_dir = q_url.toString()
        print(files_dir)

    def handleCalc(self):
        info = self.ui.textEdit.toPlainText()
        count = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            count += line + '\n'

        QMessageBox.about(self.ui, '统计结果', count)


app = QApplication([])
batch_modify = BatchModify()
batch_modify.ui.show()
app.exec_()
