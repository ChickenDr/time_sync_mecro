import sys
import function
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./main_ui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 적용 버튼
        self.start.clicked.connect(self.start_connected)

        # 취소 버튼
        # self.cancle.clicked.connect()
        
    def start_connected(self):
        t_dmain = self.target_domain.text()
        
        self.stat.clear() #화면 청소
        
        # 시간 동기화
        if function.time_sync(t_dmain):
            self.stat.append("동기화 도메인")
            self.stat.append(t_dmain)
        else:
            self.stat.append('권한 상승에 실패하였거나 도메인이 올바르지 않습니다.')
            
        
        self.stat.append("오픈할 url")
        self.stat.append(self.open_url.text())
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec_()