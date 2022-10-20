import requests
import pandas as pd
from tqdm import tqdm, trange
import time

symbols = ['BTC-USD', 'ETH-USD', 'LINK-USD', 'FIL-USD', 'SHIB-USD', 'UNI-USD', 'ATOM-USD', 'DOT-USD',
           'EOS-USD', 'ADA-USD', 'LTC-USD', 'YFI-USD', 'SUSHI-USD', 'AAVE-USD', 'BCH-USD', 'BSV-USD',
           'XRP-USD', 'ETC-USD', 'TRX-USD', 'QTUM-USD', 'ALGO-USD', 'VET-USD', 'DOGE-USD', 'COMP-USD',
           'OMG-USD', 'CRV-USD', 'STORJ-USD', 'NEAR-USD', 'SOL-USD', 'MATIC-USD', 'SAND-USD', 'MANA-USD', 
           'AVAX-USD', 'GALA-USD', 'BNB-USD', 'FTM-USD']
oi = []

with tqdm(total = len(symbols)) as pbar:
    for symbol in symbols:
        socket = f"https://api.hbdm.com/swap-api/v1/swap_open_interest?contract_code={symbol}"
        data = requests.get(socket)

        data = data.json()

        for x in data['data']:
            oi.append(int(x['volume']))
        pbar.update(1)
        
mysymbs = []
for symbol in symbols:
    mysymbs.append(symbol + ' Perpetual')
    
data = {'Ticker': mysymbs,
        'Open Interest': oi}

pd.set_option('display.max_rows', None)
df = pd.DataFrame(data)
df = df.sort_values(by='Open Interest', ascending=False)
df.reset_index(drop = True, inplace=True)
i = 0
while i < len(df):
    df['Open Interest'][i] = "{:,}".format(df['Open Interest'][i])
    i += 1
print(df)
