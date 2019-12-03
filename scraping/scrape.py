# scrapes the default amount of data and writes to a file
import requests
import csv

with open('trades.psv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['item traded', 'price', 'volume', 'time', 'buy/sell', 'market/limit', 'misc'])
    response = requests.get("https://api.kraken.com/0/public/AssetPairs")
    for x in [x for x in response.json()['result']]:
        trades = requests.get("https://api.kraken.com/0/public/Trades",params={'pair': x}).json()['result'][x]
        for y in trades:
            writer.writerow([x, *y])

