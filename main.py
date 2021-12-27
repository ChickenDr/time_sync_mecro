import sys
import function
import threading
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./main_ui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 적용 버튼
        self.start.clicked.connect(self.start_connected)
        # 적용 내용
        self.detail.clicked.connect(self.detail_connected)
        # 취소 버튼
        self.cancle.clicked.connect(self.cancle_connected)
        
    def start_connected(self):
        try:
            self.stat.clear() # 상태  화면 청소
            
            url = self.open_url.text() # 타깃 url
            t_domain = self.target_domain.text() # 타깃 도메인
            t_time = self.target_time.time().toString('hh:mm') # 타깃 시간
            
            # 항목중 비어있는 것이 있을 때
            if (not url or not t_domain):
                self.stat.append('모든 항목을 입력 하세요')

            else:
                ip = function.time_sync(t_domain)
            
                self.set_text(ip)
                
                sync_time_mecro = threading.Thread(target = function.target_url_open, args=(t_time, url), daemon=True)
                sync_time_mecro.start()

        except:
            return False

    def cancle_connected(self):
        self.open_url.clear()
        self.target_domain.clear()
        function.flag.set()

    # 상태 창
    def set_text(self, ip):
        self.stat.append("타깃 ip")
        self.stat.append(ip)
        
        self.stat.append('타깃 time')
        self.stat.append(self.target_time.time().toString('hh:mm'))
        
        self.stat.append("타깃 url")
        self.stat.append(self.open_url.text())
    
    def detail_connected(self):
        QMessageBox.about(self, 'Detail', str(function.check_sync()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec_()