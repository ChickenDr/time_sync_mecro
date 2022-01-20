<div align = "center">
  <h1> time_sync_mecro </h1>
</div>

<div align = "center">
선착순으로 신청할 일이 생겨서 만든 프로그램.<br>완전 매크로처럼 신청까지 모두해주진 않지만 정확한 시간에 창을 띄우기만해도 반은 먹지 않을까 하는 생각에 만들어 보았다.
</div>

<br>
<br>

1. 목표 도메인과, 띄울 창 url을 입력하면 ping을 보내 정규식으로 ip를 가져온다.
```python
def extractIp(ip):
    result = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip ) #IP 추출 정규식
    return result

# 도메인 ip
def get_domain_ip(url):
    ip = os.popen('ping -n 1 ' + url).read()
    getIp = extractIp(ip) #정규식으로 ip만 뽑기.
        
    return getIp[1]
```

<br>

2. 윈도우 os 명령으로 시간 공급자를 목표 서버로 맞춤
```python
# 시간 동기화
def time_sync(url):
    target_url = get_domain_ip(url)
    
    if shell.IsUserAnAdmin():
        os.system('net start w32time')
        os.system('w32tm /config /manualpeerlist:' + target_url + ' /syncfromflags:manual /update')
        return target_url

    else:
        return False
```

<br>

3. 목표 시간에 맞게 창을 띄움 sleep값을 조정 해주면 더 정밀히 가능 
```python
def target_url_open(target_time, target_url):
    global flag
    flag = threading.Event()

    while(not flag.is_set()):
        if(time.strftime('%H:%M') == target_time):
            webbrowser.open(target_url)
            break
        
        time.sleep(0.02)
        print(time.strftime('%H:%M:%S'))
```

