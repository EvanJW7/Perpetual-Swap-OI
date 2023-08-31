import requests
import pandas as pd
from tqdm import tqdm, trange
import time

symbols = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT',
           'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT',
           'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT', 'COMPUSDT',
           'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT',
           'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'SRMUSDT', 'EGLDUSDT', 'SOLUSDT',
           'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT',
           'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'CVCUSDT',
           'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'BTCBUSD', 'CHZUSDT',
           'SANDUSDT', 'ANKRUSDT', 'LITUSDT', 'UNFIUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'COTIUSDT', 'CHRUSDT',
           'MANAUSDT', 'ALICEUSDT', 'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 
           'MTLUSDT', 'OGNUSDT', 'NKNUSDT', 'DGBUSDT', '1000SHIBUSDT', 'BAKEUSDT', 'GTCUSDT', 'ETHBUSD', 'BTCDOMUSDT', 
           'BNBBUSD', 'ADABUSD', 'XRPBUSD', 'IOTXUSDT', 'DOGEUSDT', 'AUDIOUSDT', 'RAYUSDT', 'C98USDT', 'MASKUSDT', 'ATAUSDT', 
           'SOLBUSD', 'FTTBUSD', 'DYDXUSDT', '1000XECUSDT', 'GALAUSDT', 'CELOUSDT', 'ARUSDT', 'KLAYUSDT', 'ARPAUSDT', 
           'CTSIUSDT', 'LPTUSDT', 'ENSUSDT', 'PEOPLEUSDT', 'ANTUSDT', 'ROSEUSDT', 'DUSKUSDT', 'FLOWUSDT', 'IMXUSDT', 
           'API3USDT', 'GMTUSDT', 'APEUSDT', 'BNXUSDT', 'WOOUSDT', 'FTTUSDT', 'JASMYUSDT', 'DARUSDT', 'GALUSDT', 'AVAXUSDT', 
           'NEARBUSD', 'GMTBUSD', 'APEBUSD', 'GALBUSD', 'FTMBUSD', 'DODOBUSD', 'ANCBUSD', 'GALABUSD', 'TRXBUSD',
           '1000LUNCBUSD', 'LUNA2BUSD', 'OPUSDT', 'DOTBUSD', 'TLMBUSD', 'ICPBUSD', 'WAVESBUSD', 'LINKBUSD', 'SANDBUSD', 
           'LTCBUSD', 'MATICBUSD','CVXBUSD', 'FILBUSD', '1000SHIBBUSD', 'ETCBUSD', 'LDOBUSD', 'UNIBUSD', 'AUCTIONBUSD', 
           'INJUSDT', 'STGUSDT', 'FOOTBALLUSDT', 'SPELLUSDT', '1000LUNCUSDT', 'LUNA2USDT', 'AMBBUSD', 'PHBBUSD', 'LDOUSDT', 
           'CVXUSDT', 'ICPUSDT']
oi = []        

with tqdm(total = len(symbols)) as pbar:
    for symbol in symbols:
        try:
            url = f'https://fapi.binance.com/futures/data/openInterestHist?symbol={symbol}&period=5m&limit=1'
            data = requests.get(url)
            data = data.json()
            mydict = {}
            for x in data:
                mydict.update(x)
            oi.append(round(float(mydict['sumOpenInterest'])))
        except:
            print("Not a valid symbol: " + symbol)
            continue
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

