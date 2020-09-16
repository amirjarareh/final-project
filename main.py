#!/usr/bin/env python3
from PyQt5.QtCore    import pyqtSlot , pyqtSignal, QObject, QUrl
from PyQt5.QtQuick   import QQuickView
from PyQt5.QtWidgets import QApplication

import sys, _thread ,time


class QmlToPyQt(QObject):
        def __init__(self):
            QObject.__init__(self)

            # _thread.start_new_thread(QmlToPyQt.send_Data,(self,))
            # _thread.start_new_thread(QmlToPyQt.receive,(self,))
        
        @pyqtSlot(int)
        def realAnalyse(self,arg1):
            #arg1 if true =1 and false=1
            print(arg1)
        
        @pyqtSlot(int)
        def rtlMode(self,arg1):
            #arg1 if true =1 and false=1
            print(arg1)
        
        @pyqtSlot(int,int)
        def startCapture(self,arg1,arg2):
            #arg1 if true =1 and false=1 and arg2 = counter with initial 1
            print(arg1,arg2)

        @pyqtSlot(int,int)
        def recordVideo(self,arg1,arg2):
            #arg1 if true =1 and false=1 and arg2 = counter with initial 1
            print(arg1,arg2)

        @pyqtSlot(int)
        def startOfflineAnalyse(self,arg1):
            #arg1 if true =1 and false=1
            print(arg1)
        
        @pyqtSlot(int)
        def refreshfiles(self,arg1):
            #arg1 if true =1
            print(arg1)

        @pyqtSlot(int)
        def startMission(self,arg1):
            #arg1 if true =1
            print(arg1)
                                   

class MainWindow(QQuickView):
    def __init__(self):
        super().__init__()
        self.rootContext().setContextProperty("qmlToPyQt",qmlToPyQt)        
        self.setSource(QUrl('Ui/ControlProject.qml'))            
        self.show()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    qmlToPyQt = QmlToPyQt()
    w = MainWindow()
    sys.exit(app.exec_())
