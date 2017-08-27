#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication, QDialog,QWidget, QFileDialog, QPushButton, QLineEdit, QGridLayout
import sys
import os


class FileDialog(QDialog):
    def __init__(self):        
        super(FileDialog,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Caffe测试程序")
        self.setGeometry(400,400,600,200)

        self.fileButtonProto = QPushButton("请选择模型配置文件：(.prototxt)")
        self.fileLineEditProto = QLineEdit()
        self.fileButtonProto.clicked.connect(lambda:self.openProtoFile(self.fileLineEditProto.text()))
        
        self.fileButtonModel = QPushButton("请选择模型：(.caffemodel)")
        self.fileLineEditModel = QLineEdit()
        self.fileButtonModel.clicked.connect(lambda:self.openModelFile(self.fileLineEditModel.text()))

        self.fileButtonImage = QPushButton("请选择测试图片：(.bmp)")
        self.fileLineEditImage = QLineEdit()
        self.fileButtonImage.clicked.connect(lambda:self.openImageFile(self.fileLineEditImage.text()))

        self.fileButtonLmdb = QPushButton("请选择lmdb数据所在文件夹")
        self.fileLineEditLmdb = QLineEdit()
        self.fileButtonLmdb.clicked.connect(lambda:self.openLmdbFile(self.fileLineEditLmdb.text()))

        self.fileButtonExcute = QPushButton("执行")
        self.fileButtonExcute.clicked.connect(self.excute)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.fileButtonProto,0,0)
        self.mainLayout.addWidget(self.fileLineEditProto,0,1)

        self.mainLayout.addWidget(self.fileButtonModel,1,0)
        self.mainLayout.addWidget(self.fileLineEditModel,1,1)

        self.mainLayout.addWidget(self.fileButtonImage,2,0)
        self.mainLayout.addWidget(self.fileLineEditImage,2,1)

        self.mainLayout.addWidget(self.fileButtonLmdb,3,0)
        self.mainLayout.addWidget(self.fileLineEditLmdb,3,1)

        self.mainLayout.addWidget(self.fileButtonExcute,4,0)

        self.setLayout(self.mainLayout)

    def openProtoFile(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getOpenFileName(self,"Open Proto File",filePath,'*.prototxt')
        else:
            path = QFileDialog.getOpenFileName(self,"Open Proto File","D:\\caffe-windows\\examples\\cifar10",'*.prototxt')        
        self.fileLineEditProto.setText(str(path[0]))

    def openModelFile(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getOpenFileName(self,"Open Model File",filePath,'*.caffemodel')
        else:
            path = QFileDialog.getOpenFileName(self,"Open Model File","D:\\caffe-windows\\examples\\cifar10",'*.caffemodel')
        self.fileLineEditModel.setText(str(path[0]))

    def openImageFile(self,filePath):
        if os.path.exists(filePath):
            path = QFileDialog.getOpenFileName(self,"Open Image File",filePath,'*.bmp')
        else:
            path = QFileDialog.getOpenFileName(self,"Open Image File","D:\\caffe-windows\\examples\\cifar10",'*.bmp')

        if path != '':
            self.fileLineEditImage.setText(str(path[0]))
            self.fileButtonLmdb.setEnabled(False) 
            self.fileLineEditLmdb.setReadOnly(True)

    def openLmdbFile(self,filePath):
        import os
        os.popen("")
        
        if os.path.exists(filePath):
           path = QFileDialog.getExistingDirectory(self,"请选择lmdb数据所在文件夹",filePath) 
        else:
           path = QFileDialog.getExistingDirectory(self,"请选择lmdb数据所在文件夹","D:\\caffe-windows\\examples\\cifar10") 
        if path != '':
            self.fileLineEditLmdb.setText(str(path))
            self.fileButtonImage.setEnabled(False) 
            self.fileLineEditImage.setReadOnly(True)

    def excute(self):
        if self.fileButtonImage.isEnabled():
            print self.fileLineEditImage.displayText()

        elif self.fileButtonLmdb.isEnabled():
            print self.fileLineEditLmdb.displayText()

        else:
            print 'Invalid path for test images or Lmdb files!'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialog()
    ex.show()
    sys.exit(app.exec_()) 