import json, websocket, time, re, requests
from datetime import datetime

# MADE BY COXY57 ON DISCORD
# MADE BY COXY57 ON DISCORD
# MADE BY COXY57 ON DISCORD
# MADE BY COXY57 ON DISCORD
# MADE BY COXY57 ON DISCORD
# MADE BY COXY57 ON DISCORD
# MADE BY COXY57 ON DISCORD

x = "MADE BY coxy57 ON DISCORD"
y = "MADE BY coxy57 ON DISCORD"
z = "MADE BY coxy57 ON DISCORD"

# put discord webhook url here
WEBHOOK = ""



class rblxGoldHandler(websocket.WebSocketApp):
    def __init__(self):
        super().__init__(
            url="wss://api.rbxgold.com/socket.io/?EIO=4&transport=websocket",
            on_message=self.on_message,
            on_open=self.on_open)
        self.rain_started = False
    def on_message(self,ws,message):
        if not all(v in globals() for v in ("x","y","z")): return
        if 'rain-stream' in message:
            pattern = r'\[({.*})\]'
            msg = json.loads(re.search(pattern,message).group(1)[:-2])
            get_rain_amt = int(msg['evAmount']) + msg['tipAmount']
            if msg['status'] == "in progress" and self.rain_started == False:
                # send to webhook if you want
                self.rain_started = True
                data = {'content': f'@everyone Rain has started.\nAmount: {get_rain_amt}', 'username': 'Rbxgold Rain'}
                requests.post(WEBHOOK, json=data)
            elif msg['status'] == "pending" and self.rain_started == True:
                    self.rain_started = False
                    data = {'content': f'@everyone Rain has ended.\nAmount: {get_rain_amt}', 'username': 'Rbxgold Rain'}
                    requests.post(WEBHOOK, json=data)
            else:
                pass
    def on_open(self,ws):
        ws.send('40')
        time.sleep(1)
        ws.send('42["rain-join"]')


r = rblxGoldHandler()
r.run_forever()

# MADE BY COXY ON DISCORD
# MADE BY COXY ON DISCORD
# MADE BY COXY ON DISCORD
# MADE BY COXY ON DISCORD
# MADE BY COXY ON DISCORD
# MADE BY COXY ON DISCORD
# MADE BY COXY ON DISCORD
