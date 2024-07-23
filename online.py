import config
import json
import time
import websocket
import requests
import logging
import sys


websocket.enableTrace(False)
logging.getLogger('websocket').setLevel(logging.ERROR)

status = "online"
token = config.token
headers = {"Authorization": token, "Content-Type": "application/json"}
userinfo = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]


def custom_print(message):
    print(message)

custom_print("Başlatılıyor... ")
time.sleep(2)  
custom_print("""Başlatılıyor... 
| |   / /_ __/ / /_________ 
| | /| / / / / / / __/ ___/ _ \\
| |/ |/ / /_/ / / /_/ / / __/
|__/|__/\__, /_/\__/_/  \___/ 
    /____/   """)

time.sleep(2)  

def keep_online(token, status):
    ws = websocket.WebSocketApp("wss://gateway.discord.gg/?v=9&encoding=json",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def on_message(ws, message):
    pass  

def on_error(ws, error):
    pass

def on_close(ws, close_status_code, close_msg):
    custom_print("### Hesap Kapatıldı. ###")

def on_open(ws):
    auth = {"op": 2, "d": {"token": token, "properties": {"$os": "Windows 11", "$browser": "Google Chrome", "$device": "Windows"}, "presence": {"status": status, "afk": False}}, "s": None, "t": None}
    ws.send(json.dumps(auth))

def run_keep_online():
    custom_print(f"Hesaba Başarılıyla Bağlanıldı {username}#{discriminator} ({userid}).")
    while True:
        keep_online(token, status)
        time.sleep(30)

run_keep_online()
