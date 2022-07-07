import json
import websocket
import pprint

# SOCKET="wss://ws-feed-public.sandbox.exchange.coinbase.com"
SOCKET="wss://ws-feed.exchange.coinbase.com"

def on_open(ws):
    print("Websocket connection opened!")
    ws.send(json.dumps({
        "type": "subscribe",
        "product_ids": ["ETH-USD"],
        "channels": ["ticker_batch"]
    }))

def on_close(ws):
    print("Websocket connection closed!")

def on_error(ws, error):
    print("There was an error with the websocket: " + str(error))

def on_message(ws, message):
    print("Received message")
    json_message = json.loads(message)
    pprint.pprint(json_message)



ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
ws.run_forever()