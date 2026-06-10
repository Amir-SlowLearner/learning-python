from urllib.parse import urlencode

params = {"symbol":"BTCUSDT&ETHUSDT" , "price":"73000" , "qty":"1"}

query_string = urlencode(params)

print(query_string)           