import requests 
import pandas as pd

swaps_url = 'https://www.okx.com/api/v5/public/open-interest?instType=SWAP'

data = requests.get(swaps_url)

data = data.json()
ids = []
oi = []
coms = []

for x in data['data']:
    ids.append(x['instId'])
    oi.append(int(x['oi']))

data = {'Ticker': ids,
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