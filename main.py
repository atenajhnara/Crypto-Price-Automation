
#******اتوماسیون گرفتن قیمت ارز دیجیتال و ذخیره در فایل اکسل*******

import requests
import pandas as pd
from datetime import datetime, timezone
import time
import os

main_file="crypto_prices.csv"
coins='bitcoin,ethereum,cardano,dogecoin,solana'
vs_currency='usd'
interval=60
while True:
    try:
        url='https://api.coingecko.com/api/v3/simple/price'
        params={'ids':coins,'vs_currencies':vs_currency}
        response=requests.get(url=url,params=params,timeout=10)
        data=response.json()

        now=datetime.now(timezone.utc)
        rows=[]
        for coin in data:
            rows.append({'Datatime':now,'Coin':coin,'Price':data[coin][vs_currency]})
    
        df=pd.DataFrame(rows)
        try:
            df.to_csv(main_file,mode='a',index=False,header=not os.path.exists(main_file))
        except PermissionError:
            temp_file=f"crypto_prices_{int(time.time())}.csv"
            df.to_csv(temp_file,index=False)

    except requests.exceptions.ConnectionError:
        time.sleep(10)
        
    time.sleep(interval)


