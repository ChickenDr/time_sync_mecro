import os
import sys
import win32com.shell.shell as shell
import re

def extractIp(ip):
    result = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip ) #IP 추출 정규식
    return result

def get_domain_ip(url):
    ip = os.popen('nslookup ' + url).read()
    getIp = extractIp(ip) #정규식으로 ip만 뽑기.
        
    return getIp[1]

def time_sync(url):
    target_url = get_domain_ip(url)
    
    if shell.IsUserAnAdmin():
        sync = os.system('w32tm /config /manualpeerlist:' + target_url + ' /syncfromflags:manual /update')
        check_time_sync = os.popen('w32tm /query /configuration').read()
        print(check_time_sync)
        return True

    else:
        return False
    

print(time_sync('https://www.naver.com/'))
