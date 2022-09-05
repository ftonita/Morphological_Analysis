from header import *
from mysql_utils import DataBase

class Ui_DialogAbout(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 240)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 300, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(32, 10, 256, 128))
        self.textBrowser.setAutoFillBackground(False)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+title+"</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;&gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;&gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;&gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;&gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">"+ AUTHOR +"</span></p></body></html>", None))

class showAboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_DialogAbout()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)


class Ui_DialogResult(object):
    def setupUi(self, Dialog, res):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 240)
        palette = QPalette()
        brush = QBrush(QColor(227, 195, 253, 199))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(227, 195, 253, 199))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        Dialog.setPalette(palette)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 60, 160, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.log_res = QTextBrowser(self.verticalLayoutWidget)
        self.log_res.setObjectName(u"log_res")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_res.sizePolicy().hasHeightForWidth())
        self.log_res.setSizePolicy(sizePolicy)
        self.log_res.setMinimumSize(QSize(0, 32))
        self.log_res.setMaximumSize(QSize(500, 32))

        self.verticalLayout.addWidget(self.log_res)

        self.pass_res = QTextBrowser(self.verticalLayoutWidget)
        self.pass_res.setObjectName(u"pass_res")
        sizePolicy.setHeightForWidth(self.pass_res.sizePolicy().hasHeightForWidth())
        self.pass_res.setSizePolicy(sizePolicy)
        self.pass_res.setMinimumSize(QSize(0, 32))
        self.pass_res.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout.addWidget(self.pass_res)

        self.service_res = QTextBrowser(Dialog)
        self.service_res.setObjectName(u"service_res")
        self.service_res.setGeometry(QRect(80, 20, 160, 32))
        sizePolicy.setHeightForWidth(self.service_res.sizePolicy().hasHeightForWidth())
        self.service_res.setSizePolicy(sizePolicy)
        self.service_res.setMinimumSize(QSize(0, 32))
        self.service_res.setMaximumSize(QSize(16777215, 32))

        self.service_res.setText(res.service)
        self.log_res.setText(res.login)
        self.pass_res.setText(res.password)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Info", u"Информация", None))

class showResultDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

    def showDialog(self, res):
        # Create an instance of the GUI
        self.ui = Ui_DialogResult()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self, res)

# ####################################

