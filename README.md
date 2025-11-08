# 💰 Crypto Price Automation & Excel Logger | اتوماسیون دریافت قیمت ارز دیجیتال

A Python script that automatically fetches cryptocurrency prices from the CoinGecko API at regular intervals and saves them into a CSV file.  
Supports multiple coins and appends new data automatically.

یک اسکریپت پایتون برای دریافت خودکار قیمت رمزارزها از API سایت CoinGecko و ذخیره آن‌ها در فایل CSV.  
چندین ارز را می‌توان دنبال کرد و اطلاعات جدید به صورت خودکار به فایل اضافه می‌شود.

---

## 🧠 Technologies Used | تکنولوژی‌های استفاده‌شده

- Python 3.10+ – زبان برنامه‌نویسی  
- requests – ارتباط با API و دریافت داده  
- pandas – پردازش و ذخیره داده‌ها در CSV  
- datetime / timezone – مدیریت تاریخ و زمان  
- time / os – کنترل فاصله زمانی و مدیریت فایل  

---

## ⚙️ How It Works | نحوه عملکرد

1️⃣ تعریف لیست ارزها (`bitcoin, ethereum, cardano, dogecoin, solana`) و واحد پول (`USD`).  
2️⃣ درخواست قیمت‌ها از CoinGecko API در فواصل زمانی مشخص (مثلاً هر 60 ثانیه).  
3️⃣ دریافت پاسخ و تبدیل آن به فرمت DataFrame با pandas.  
4️⃣ ذخیره داده‌ها در فایل CSV اصلی و اضافه کردن ردیف‌های جدید.  
5️⃣ مدیریت خطاها مانند قطع ارتباط اینترنت و عدم دسترسی به فایل.  

---

## 🧩 Key Code Structure | ساختار اصلی کد

```python
import requests
import pandas as pd
from datetime import datetime, timezone
import time
import os

main_file = "crypto_prices.csv"
coins = 'bitcoin,ethereum,cardano,dogecoin,solana'
vs_currency = 'usd'
interval = 60  # هر 60 ثانیه

while True:
    try:
        # درخواست قیمت‌ها از CoinGecko API
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {'ids': coins, 'vs_currencies': vs_currency}
        response = requests.get(url=url, params=params, timeout=10)
        data = response.json()

        now = datetime.now(timezone.utc)
        rows = []
        for coin in data:
            rows.append({'Datetime': now, 'Coin': coin, 'Price': data[coin][vs_currency]})
        
        df = pd.DataFrame(rows)
        # ذخیره در CSV و اضافه کردن ردیف‌های جدید
        df.to_csv(main_file, mode='a', index=False, header=not os.path.exists(main_file))

    except requests.exceptions.ConnectionError:
        time.sleep(10)  # انتظار در صورت قطع اینترنت
    
    time.sleep(interval)
