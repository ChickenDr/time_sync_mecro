import os
import sys
import time
import re
import threading
import webbrowser
import win32com.shell.shell as shell

def extractIp(ip):
    result = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip ) #IP 추출 정규식
    return result

# 도메인 ip
def get_domain_ip(url):
    ip = os.popen('ping -n 1 ' + url).read()
    getIp = extractIp(ip) #정규식으로 ip만 뽑기.
        
    return getIp[1]

# 동기화 결과
def check_sync():
    check_time_sync = os.popen('w32tm /query /configuration').read()
    return check_time_sync

# 시간 동기화
def time_sync(url):
    target_url = get_domain_ip(url)
    
    if shell.IsUserAnAdmin():
        os.system('net start w32time')
        os.system('w32tm /config /manualpeerlist:' + target_url + ' /syncfromflags:manual /update')
        return target_url

    else:
        return False

def target_url_open(target_time, target_url):
    global flag
    flag = threading.Event()

    while(not flag.is_set()):
        if(time.strftime('%H:%M') == target_time):
            webbrowser.open(target_url)
            break
        
        time.sleep(0.02)
        print(time.strftime('%H:%M:%S'))
